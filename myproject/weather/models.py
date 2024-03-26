from django.db import models

class Location(models.Model):
    nx = models.IntegerField()
    ny = models.IntegerField()

    class Meta:
        unique_together = ('nx', 'ny')

    def __str__(self):
        return f"Location ({self.nx}, {self.ny})"

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Observation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    baseDate = models.CharField(max_length=8)
    baseTime = models.CharField(max_length=4)
    obsrValue = models.CharField(max_length=15)

    class Meta:
        unique_together = ('location', 'category')

class Forecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    baseDate = models.CharField(max_length=8)
    baseTime = models.CharField(max_length=4)
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=4)
    fcstValue = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.category} Forecast for {self.fcstDate} at {self.fcstTime}"
    
# class UltraShortForecast(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE, unique=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     baseDate = models.CharField(max_length=8)
#     baseTime = models.CharField(max_length=4)
#     obsrValue = models.CharField(max_length=15)

#     def __str__(self):
#         return f"Ultra Short Term Forecast at {self.location} on {self.baseDate} {self.baseTime}"
    
class ShortForecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    baseDate = models.CharField(max_length=8)
    baseTime = models.CharField(max_length=4)
    fcstDate = models.CharField(max_length=8)
    fcstTime = models.CharField(max_length=4)
    fcstValue = models.CharField(max_length=15)

    class Meta:
        unique_together = ('location', 'category', 'baseDate', 'baseTime', 'fcstDate', 'fcstTime')
        
    def __str__(self):
        return f"{self.category} Forecast for {self.fcstDate} at {self.fcstTime}"
