from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import *

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/',LogoutView.as_view(), name='logout'),
    path('profile-detail/', ProfileDetailView.as_view(), name='profile-detail'),
    path('tableau-data/', TableauDataView.as_view(), name='tableau_data'),
    path('dashboard/', dashboard),
    path('hasotp/', HasOTPView.as_view(), name='hasotp'),
    path('otp/', OTPView.as_view(), name='otp'),
    path('otp/<str:token>/', TOTPVerifyView.as_view(), name='otp'),
    path('verified/', VerifiedView.as_view(), name='verify'),
    path('', getRoutes),
]



