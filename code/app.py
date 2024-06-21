from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
lin_reg_model = joblib.load('linear_regression_model.pkl')
las_reg_model = joblib.load('lasso_regression_model.pkl')
model_features = joblib.load('model_features.pkl')


if 'Year' not in model_features:
    model_features.append('Year')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    data_df = pd.DataFrame([data])
    
    data_df = data_df.astype({
        "Present_Price": float,
        "Kms_Driven": int,
        "Owner": int,
        "Fuel_Type": int,
        "Seller_Type": int,
        "Transmission": int,
        "Year": int  
    })
    
    data_df = data_df[model_features]
    
    lin_reg_prediction = lin_reg_model.predict(data_df)
    las_reg_prediction = las_reg_model.predict(data_df)
    
    return render_template('result.html', 
                           lin_reg_prediction=lin_reg_prediction[0], 
                           las_reg_prediction=las_reg_prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
