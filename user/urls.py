from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/',LogoutView.as_view(), name='logout'),
    path('profile-detail/', ProfileDetailView.as_view(), name='profile-detail'),
    path('tableau-data/', TableauDataView.as_view(), name='tableau_data'),
    # path('register/', RegisterView.as_view(), name='auth_reegister'),
    path('dashboard/', dashboard),
    # path('test/',  testView),
    path('', getRoutes),
]

