# Car Price Prediction

This repository contains code for a car price prediction web application. The application utilizes two machine learning models - Linear Regression and Lasso Regression - to predict the selling price of a car based on various features. The application is built using Python, Flask for the web framework, and scikit-learn for the machine learning models.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Model Training](#model-training)
  - [Web Application](#web-application)
- [Acknowledgements](#acknowledgements)

## Project Overview

The goal of this project is to predict the selling price of a car based on features such as present price, kilometers driven, ownership, fuel type, seller type, transmission type, and the year of the car model. Two regression models are used: Linear Regression and Lasso Regression.

## Directory Structure
<br/>
car-price-prediction/<br/>
│<br/>
├── car_prediction_model.py<br/>
├── app.py<br/>
├── templates/<br/>
│ ├── index.html<br/>
│ └── result.html<br/>
├── static/<br/>
│ └── styles.css<br/>
├── README.md<br/>
└── requirements.txt<br/></br>

- `car_prediction_model.py`: Script to train the Linear Regression and Lasso Regression models.
- `app.py`: Flask application script to serve the web application.
- `templates/`: Directory containing HTML templates for the web application.
- `static/`: Directory containing static files such as CSS.
- `README.md`: Documentation file for the project.
- `requirements.txt`: List of Python dependencies required for the project.

## Setup and Installation

### Prerequisites

Ensure you have the following installed on your machine:
- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-price-prediction.git
   cd car-price-prediction

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv 
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Download the car dataset and place it in the project directory. Update the file path in car_prediction_model.py accordingly.

## Usage
### Model Training:

To train the models and save them to disk, run the car_prediction_model.py script:<br/>
python car_prediction_model.py



This will create two model files:linear_regression_model.pkl and lasso_regression_model.pkl, along with model_features.pkl.

Web Application:
To start the web application, run the app.py script:


## Model Training
- The `car_prediction_model.py` script performs the following steps:
  - Loads the car dataset from a CSV file.
  - Preprocesses the dataset, including encoding categorical variables.
  - Splits the dataset into training and testing sets.
  - Trains a Linear Regression model and a Lasso Regression model.
  - Saves the trained models and the feature list to disk.
  - Visualizes the actual vs. predicted prices for both models.

## Web Application
- The web application (`app.py`) allows users to input car details and get price predictions from both the Linear Regression and Lasso Regression models. The app consists of:
  - `index.html`: Form for users to input car details.
  - `result.html`: Displays the predicted prices from both models.

### Routes
- `/`: Renders the home page with the input form.
- `/predict`: Handles form submission, processes input data, and renders the result page with predictions.

## Acknowledgements
- This project uses the following libraries and frameworks:
  - Pandas
  - Matplotlib
  - Seaborn
  - scikit-learn
  - Flask
  - Joblib

Feel free to contribute to the project by opening issues or submitting pull requests.





