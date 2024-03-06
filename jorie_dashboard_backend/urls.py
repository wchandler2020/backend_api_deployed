
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('user.urls')),
    # path('charts-data/', include('charts_data.urls')),
    path('tinymce/', include('tinymce.urls'))
,]

