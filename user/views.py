from dotenv import load_dotenv
from django.shortcuts import render
from user.models import User, Profile
from .tableau_utils import fetch_data
from .serializer import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    RegisterUserSerializer,
    ProfileSerializer
)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying, flatten_dict_column
import json
import concurrent.futures
import re
from user.data import Data as client_data


load_dotenv()  # take environment variables from .env.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/token/logout/',
        '/api/profile-detail/',
        '/api/dashboard/',
        '/api/tableau-data/',
        
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        # Serialize the user data
        user_serializer = UserSerializer(request.user)
        user_data = user_serializer.data
        response = f'Hi {user_data["username"]} welcome back'
        
        # Include all fields from UserSerializer in the response
        context = {'user': user_data, 'response': response, **user_data}
        
        return Response(context, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        response = f'Hi, {request.user}, your text is {text}'
        return Response({'response': response}, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Get the profile data for the current user
            profile = request.user.profile
            # Serialize the profile data
            serializer = ProfileSerializer(profile)
            # Return the serialized data as JSON
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            # Handle the case where the profile does not exist for the user
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle other exceptions
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

# class TableauDataView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         data = client_data.get_data(2)
#         data_id_list = data[0]
#         chart_data = data[1]

#         # Combine data_id_list and chart_data into a single dictionary
#         data_dict = {'data_id_list': data_id_list, 'chart_data': chart_data}

#         ortho_one_data = []

#         # Using ThreadPoolExecutor to fetch data concurrently for data_id_list
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             results = list(executor.map(fetch_data, (data_id for row in data_id_list for data_id in row)))

#         # Transform results to one array containing three dictionaries for data_id_list
#         for i, row in enumerate(data_id_list):
#             dict_row = {f"item_{j + 1}": json.loads(results.pop(0)) for j in range(len(row))}
#             ortho_one_data.append(dict_row)
        
#         # Fetch data for chart_data
#         chart_data_results = []
#         for chart_id in chart_data:
#             # Convert fetched data to JSON before appending to chart_data_results
#             chart_data_results.append(json.loads(fetch_data(chart_id)))

#         # Return JSON response with ortho_one_data, combined data_id_list, and chart data
#         return Response({'ortho_one_data': ortho_one_data, 'chart_data_results': chart_data_results}, status=status.HTTP_200_OK)

    
    


    



