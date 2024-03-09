from django.shortcuts import render
import json
from dotenv import load_dotenv
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .data import Data
from .tableau_utils import fetch_data
import concurrent.futures
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
class TableauDataView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self, client_name):
        print('client name: ', client_name)
        obj = Data()
        data = obj.get_data(client_name)
        data_id_list = data[0]
        chart_data = data[1]

        ortho_one_data = []

        # Using ThreadPoolExecutor to fetch data concurrently for data_id_list
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(fetch_data, (data_id for row in data_id_list for data_id in row)))

        # Transform results to one array containing three dictionaries for data_id_list
        for i, row in enumerate(data_id_list):
            dict_row = {f"item_{j + 1}": json.loads(results.pop(0)) for j in range(len(row))}
            ortho_one_data.append(dict_row)
        
        # Fetch data for chart_data
        chart_data_results = []
        for chart_id in chart_data:
            # Convert fetched data to JSON before appending to chart_data_results
            chart_data_results.append(json.loads(fetch_data(chart_id)))

        # Return JSON response with ortho_one_data, combined data_id_list, and chart data
        return ({'client_data': ortho_one_data, 'chart_data_results': chart_data_results})
