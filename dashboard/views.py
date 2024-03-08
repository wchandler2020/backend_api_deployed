from django.shortcuts import render
import json
from dotenv import load_dotenv
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from user.data import Data as client_data
from .tableau_utils import fetch_data
import concurrent.futures

# Create your views here.

class TableauDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = client_data.get_data(2)
        data_id_list = data[0]
        chart_data = data[1]

        # Combine data_id_list and chart_data into a single dictionary
        data_dict = {'data_id_list': data_id_list, 'chart_data': chart_data}

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
        return Response({'ortho_one_data': ortho_one_data, 'chart_data_results': chart_data_results}, status=status.HTTP_200_OK)
