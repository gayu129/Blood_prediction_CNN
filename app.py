from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/upload/'

# Ensure upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load the pre-trained model
model_path = 'blood_group_model.h5'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found!")

model = load_model(model_path)

# Image dimensions
img_size = (224, 224)

# Blood group classes
classes = ['AB-', 'O+', 'B-', 'B+', 'A-', 'A+', 'O-', 'AB+']

# Prediction function
def predict_blood_group(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize(img_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    blood_group = classes[class_index]
    return blood_group

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded!"
        
        file = request.files['image']
        
        if file.filename == '':
            return "No image selected!"
        
        if file:
            # Save the uploaded file
            from werkzeug.utils import secure_filename

            filename = secure_filename(file.filename)  # Ensures a safe filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
            
            # Make prediction
            prediction = predict_blood_group(image_path)
            
            return render_template('index.html', prediction=prediction, image_path=image_path)
    
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

