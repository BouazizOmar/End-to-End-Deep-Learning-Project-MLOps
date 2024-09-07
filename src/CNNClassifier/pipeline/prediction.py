import os
import numpy as np
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        model_path = os.path.join(base_dir, "artifacts", "training", "model.h5")
        base_dir = os.path.normcase(base_dir)        
        print("Base dir: ", base_dir)  
        print(f"Model path: {model_path}")
        print(f"Current working directory: {os.getcwd()}")

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")

        model = load_model(model_path)

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = "Normal"
            return [{"image": prediction}]
        else:
            prediction = "Adenocarcioma Cancer"
            return [{"image": prediction}]
