from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetch_weather_data, name='fetch_weather_data'),
    path('', views.display_weather_data, name='display_weather_data'),
    path('getUltraSrtNcst', views.getUltraSrtNcst_weather_data, name='getUltraSrtNcst_weather_data'),
    path('getUltraSrtFcst_weather_data', views.getUltraSrtFcst_weather_data, name='getUltraSrtFcst_weather_data'),
    path('getVilageFcst_weather_data', views.getVilageFcst_weather_data, name='getVilageFcst_weather_data'),


]
