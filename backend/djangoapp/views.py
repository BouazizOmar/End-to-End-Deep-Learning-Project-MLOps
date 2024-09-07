from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os
from CNNClassifier.utils.common import decode_image
from CNNClassifier.pipeline.prediction import PredictionPipeline
import json

os.putenv("LANG", "en_US.UTF_8")
os.putenv("LC_ALL", "en_US.UTF_8")

# Initialize the classifier globally
filename = "inputImage.jpg"
classifier = PredictionPipeline(filename)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
    return render(request, os.path.join(BASE_DIR, '..', 'frontend', 'build', 'index.html'))

@csrf_exempt
def train_route(request):
    if request.method == 'POST':
        os.system("python main.py")
        return JsonResponse({"message": "Training done successfully!"})
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def predict_route(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({"error": "No image uploaded"}, status=400)

        # Get the image file from request.FILES
        image = request.FILES['image']

        # Define the directory where images will be saved
        upload_dir = 'uploads'
        
        # Ensure the directory exists, create it if not
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Define a path to save the uploaded image
        filename = os.path.join(upload_dir, image.name)

        # Save the image to the defined path
        with open(filename, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # Initialize the PredictionPipeline with the saved image filename
        prediction_pipeline = PredictionPipeline(filename)
        result = prediction_pipeline.predict()

        # Return the prediction result (ensure safe=False if result is a list or non-dict)
        return JsonResponse(result, safe=False)

    return JsonResponse({"error": "Invalid method"}, status=405)