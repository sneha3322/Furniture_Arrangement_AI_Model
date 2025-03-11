import os
import json
import random
import numpy as np
import tensorflow as tf
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Define base directory and model path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'furniture_api', 'furniture_placement_model.h5')

# Load trained model
custom_objects = {"mse": tf.keras.losses.MeanSquaredError()}
try:
    model = tf.keras.models.load_model(MODEL_PATH, custom_objects=custom_objects)
except Exception:
    model = None  # Prevent crashing if model fails to load

@csrf_exempt
def predict_furniture(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            room_data = np.array(data["room"]).flatten()

            # Ensure input matches model requirements
            padded_data = np.pad(room_data, (0, max(0, 100 - len(room_data))), 'constant')
            padded_data = padded_data.reshape(1, -1)

            # Predict furniture placement (x, y, width, height)
            predictions = model.predict(padded_data).reshape(-1, 4)

            # Post-processing to prevent overlap and ensure in-bounds placement
            placements = []
            occupied = set()

            for p in predictions:
                x = max(0, min(7, int(p[0])))  # Ensuring x stays within grid limits (7 max for width 3)
                y = max(0, min(7, int(p[1])))  # Ensuring y stays within grid limits (7 max for height 3)
                width = max(1, min(3, int(p[2])))
                height = max(1, min(3, int(p[3])))

                # Ensure furniture doesn't overlap by checking occupied spaces
                while any((x2 <= x < x2 + w2 and y2 <= y < y2 + h2) for x2, y2, w2, h2 in occupied):
                    x = (x + random.randint(1, 3)) % 8  # Recalculate within safe bounds
                    y = (y + random.randint(1, 3)) % 8

                occupied.add((x, y, width, height))
                placements.append({"x": x, "y": y, "width": width, "height": height})

            return JsonResponse({"Optimized_furniture_placement": placements}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)