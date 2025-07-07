 # Blood Group Classification Web App

    This project is a Flask-based web application that predicts human blood groups from uploaded images using a pre-trained deep learning model.

    ## Features

    - Upload an image of a blood sample.
    - Predicts the blood group (A+, A-, B+, B-, AB+, AB-, O+, O-) using a Keras model.
    - Displays the prediction and the uploaded image.

    ## Requirements

    - Python 3.7+
    - Flask
    - TensorFlow (with Keras)
    - Pillow (PIL)
    - NumPy
    - Werkzeug

    ## Installation

    1. **Clone the repository:**
        ```bash
        git clone https://github.com/yourusername/blood-group-classification.git
        cd blood-group-classification
        ```

    2. **Install dependencies:**
        ```bash
        pip install -r requirements.txt
        ```

    3. **Add the model:**
        - Place your trained model file named `blood_group_model.h5` in the project root directory.

    4. **Create upload directory (if not auto-created):**
        ```bash
        mkdir -p static/upload
        ```

    ## Usage

    1. **Run the application:**
        ```bash
        python app.py
        ```

    2. **Open your browser and go to:**
        ```
        http://127.0.0.1:5000/
        ```

    3. **Upload an image** and view the predicted blood group.



    
