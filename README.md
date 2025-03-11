# Furniture_Arrangement_AI_Model
This project predicts optimized furniture placement based on room dimensions and constraints using a deep learning model. The backend is implemented using Django, and the AI model is trained in Google Colab.


## 1. Project Overview :
The application takes room constraints as input and outputs an optimized furniture placement using deep learning.\
The model is trained in Google Colab and exported as an H5 file for Django integration.\
The Django REST API serves predictions based on the trained model.

## 2. How to Run the Application :
1️⃣ Open Google Colab and Train the Model\
a) Open Google Colab and upload furniture_placement_model.ipynb.\
b) Run all cells to train the model.\
c) Download the trained model file (furniture_placement_model.h5) after training.\
d) Move the file to the Django backend folder (furniture_api/) on your local machine.

2️⃣ Set Up Django Backend \
Step 1:  Open VS Code and Clone the Repository\
a) Open VS Code.\
2) Open Terminal (View -> Terminal).\
3) Clone the project and move into the folder:\
   git clone https://github.com/sneha3322/Furniture_Arrangement_AI_Model \
   cd furniture_api \
Step 2: Add Trained Model\
a) Train the model in Google Colab (furniture_placement_model.ipynb).\
b) Download the furniture_placement_model.h5 file.\
c) Move it inside the furniture_api/ folder.\
Step 3: Run Django Server\
a) Apply database migrations:\
   python manage.py migrate\
b) Run the Django development server:\
   python manage.py runserver\
c) If successful, you will see output like:\
   http://127.0.0.1:8000/

3️⃣ Test the API in Postman \
a) Open Postman\
b) Select POST request\
c) Enter URL:  http://127.0.0.1:8000/api/predict/ \
d) Go to Body → Raw → JSON and enter sample input \
    for ex: \
    {  \
    "room": [0, 1, 0, 0, 2, 0, 0, 1, 0, 0,
             0, 1, 0, 0, 2, 0, 0, 1, 0, 0,
             1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 
             1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 
             0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 
             1, 0, 0, 0, 2, 1, 0, 0, 0, 0,  
             0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 
             1, 0, 0, 2, 1, 0, 0, 0, 0, 0]
}
e) Click send
f) You should receive a response like,
   {
    "Optimized_furniture_placement": [
        {
            "x": 3,
            "y": 2,
            "width": 2,
            "height": 2
        },
        {
            "x": 2,
            "y": 5,
            "width": 2,
            "height": 1
        },
        {
            "x": 7,
            "y": 4,
            "width": 3,
            "height": 3
        },
        {
            "x": 7,
            "y": 7,
            "width": 3,
            "height": 3
        },
        {
            "x": 2,
            "y": 1,
            "width": 3,
            "height": 3
        }
    ]
}

4️⃣ To stop the Server 
Press ->  CTRL + C

## Conclusion :
This project successfully predicts optimized furniture placements in a room using AI. It takes room data as input and provides an efficient layout while considering obstacles and spacing rules.

Key Highlights:
1) Uses a trained deep learning model for furniture arrangement
2) Built with Django for easy API access
3) Ensures proper spacing and no overlap

In the future, this can be improved by supporting different room sizes, adding more furniture types, and improving placement accuracy. This project shows how AI can help in designing better room layouts. 











