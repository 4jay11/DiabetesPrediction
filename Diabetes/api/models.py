from django.db import models
#'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'
# Create your models here.
class Diabetes(models.Model):
    Pregnancies=models.FloatField(max_length=20)
    Glucose=models.FloatField(max_length=20)
    BloodPressure=models.FloatField(max_length=20)
    SkinThickness=models.FloatField(max_length=20)
    Insulin=models.FloatField(max_length=20)
    BMI=models.FloatField(max_length=20)
    DiabetesPedigreeFunction=models.FloatField(max_length=20)
    Age=models.FloatField(max_length=20)