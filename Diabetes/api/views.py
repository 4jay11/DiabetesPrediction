from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from .serializers import DiabetesSerializer
from rest_framework import status

# Load the dataset and train the model
data = pd.read_csv("E:/MLP/Diabetes/Model/diabetes dataset.csv")  # Update with your file path
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
model = DecisionTreeClassifier()
model.fit(x, y)

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        serializer = DiabetesSerializer(data=request.data)
        if serializer.is_valid():
            input_data = tuple(serializer.validated_data.values())
            input_numpy = np.asarray(input_data).reshape(1, -1)
            out = model.predict(input_numpy)
            # Handle the case where 'out' is not assigned in all execution paths
            prediction = "Having diabetes" if out == 1 else "Not having diabetes"
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
