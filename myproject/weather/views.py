import requests
from django.http import HttpResponse
from .models import Location, Category, Observation, Forecast, ShortForecast
import json
from django.db import transaction

def fetch_weather_data(request):
    # This view now simply returns a text message
    return HttpResponse("Fetching weather data is not implemented yet.", content_type="text/plain")

def display_weather_data(request):
    # This view now simply returns a text message
    return HttpResponse("Displaying weather data is not implemented yet.", content_type="text/plain")

#초단기실황
def getUltraSrtNcst_weather_data(request):
    # This view now simply returns a text message
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
    params = {
        "serviceKey": "kBGz1W6eyDnkBzIla5QrYE9jkynAvlBGqfa6L2/3J9jvQSv/VlpqfushXv9EP5VJC25zfhdbPvoSPw2zY9LFaQ==",  # 실제 서비스키를 입력해야 합니다.
        "pageNo": "1",
        "numOfRows": "1000",
        "dataType": "JSON",
        "base_date": "20240326",  
        "base_time": "1200",  
        "nx": "55",
        "ny": "127"
    }
    response = requests.get(url, params=params)
    # 응답 데이터 JSON으로 변환
    data = response.json()
    location, _ = Location.objects.get_or_create(nx=params['nx'], ny=params['ny'])
    
    items = data['response']['body']['items']['item']
    for item in items:
        # 카테고리 정보 가져오기 또는 생성
        category, _ = Category.objects.get_or_create(name=item['category'])

        # 이 부분을 update_or_create 메소드로 변경
        with transaction.atomic():
            observation, created = Observation.objects.update_or_create(
                location=location, 
                category=category, 
                defaults={
                    'baseDate': item['baseDate'], 
                    'baseTime': item['baseTime'], 
                    'obsrValue': item['obsrValue']
                }
            )
    
    pretty_data = json.dumps(data, indent=4, ensure_ascii=False)
    return HttpResponse(str(pretty_data), content_type="application/json")

#초단기예보조회
def getUltraSrtFcst_weather_data(request):
    # This view now simply returns a text message
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
    params = {
        "serviceKey": "kBGz1W6eyDnkBzIla5QrYE9jkynAvlBGqfa6L2/3J9jvQSv/VlpqfushXv9EP5VJC25zfhdbPvoSPw2zY9LFaQ==",  # 실제 서비스키를 입력해야 합니다.
        "pageNo": "1",
        "numOfRows": "1000",
        "dataType": "JSON",
        "base_date": "20240326",  
        "base_time": "1300",  
        "nx": "55",
        "ny": "127"
    }
    response = requests.get(url, params=params)
    # 응답 데이터 JSON으로 변환
    data = response.json()
    location, _ = Location.objects.get_or_create(nx=params['nx'], ny=params['ny'])
    
    items = data['response']['body']['items']['item']
    for item in data['response']['body']['items']['item']:
        location, _ = Location.objects.get_or_create(nx=item['nx'], ny=item['ny'])
        category, _ = Category.objects.get_or_create(name=item['category'])

        # Update or create a new entry
        forecast, created = ShortForecast.objects.update_or_create(
            location=location,
            category=category,
            baseDate=item['baseDate'],
            baseTime=item['baseTime'],
            fcstDate=item['fcstDate'],
            fcstTime=item['fcstTime'],
            defaults={
                'fcstValue': item['fcstValue']
            }
        )
    
    pretty_data = json.dumps(data, indent=4, ensure_ascii=False)
    return HttpResponse(str(pretty_data), content_type="application/json")

#단기예보조회
def getVilageFcst_weather_data(request):
    # This view now simply returns a text message
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
    params = {
        "serviceKey": "kBGz1W6eyDnkBzIla5QrYE9jkynAvlBGqfa6L2/3J9jvQSv/VlpqfushXv9EP5VJC25zfhdbPvoSPw2zY9LFaQ==",  
        "pageNo": "1",
        "numOfRows": "1000",
        "dataType": "JSON",
        "base_date": "20240326",  
        "base_time": "0500",  
        "nx": "55",
        "ny": "127"
    }

    response = requests.get(url, params=params)
    # 응답 데이터 JSON으로 변환
    data = response.json()
    location, _ = Location.objects.get_or_create(nx=params['nx'], ny=params['ny'])
    
    items = data['response']['body']['items']['item']
    for item in items:
        category, _ = Category.objects.get_or_create(name=item['category'])
        Forecast.objects.create(
            location=location,
            category=category,
            baseDate=item['baseDate'],
            baseTime=item['baseTime'],
            fcstDate=item['fcstDate'],
            fcstTime=item['fcstTime'],
            fcstValue=item['fcstValue']
        )
    
    pretty_data = json.dumps(data, indent=4, ensure_ascii=False)
    return HttpResponse(str(pretty_data), content_type="application/json")

