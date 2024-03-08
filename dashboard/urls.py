from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import TableauDataView

urlpatterns = [
    path('tableau-data/', TableauDataView.as_view(), name='tableau_data'),
]