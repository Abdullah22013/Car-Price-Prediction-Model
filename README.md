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

car-price-prediction/
│
├── car_prediction_model.py
├── app.py
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── styles.css
├── README.md
└── requirements.txt

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
