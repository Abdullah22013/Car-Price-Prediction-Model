import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics
import joblib

# loading the dataset from csv to panda dataframe
car_dataset = pd.read_csv(r'C:\ACADEMIC\Projects\Machine learning\car price prediction\archive\cardata.csv')

#reading the first  5 rows of dataset

#print(car_dataset.head())

# checking the columns and rows of dataset
#print(car_dataset.shape)

#checking the overall information about the dataset
#print(car_dataset.info())

#checking the number of missing or empty spaces in each column

#print(car_dataset.isnull().sum())

#checking the distribution of categorical data

#print(car_dataset.Fuel_Type.value_counts())
#print(car_dataset.Seller_Type.value_counts())
#print(car_dataset.Transmission.value_counts())

#encoding 'Fuel_Type' column
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}}, inplace=True)

#encoding 'Seller_Type' column
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}}, inplace=True)

#encoding 'Transmission' column
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}}, inplace=True)

print(car_dataset.head())

#Now splitting the data and target ,, data is all the info except the car name and selling price whereas the target is Selling price
X = car_dataset.drop(['Car_Name','Selling_Price'], axis=1)
Y = car_dataset['Selling_Price']

#print(X)
#print(Y)

# Splitting Training and Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=2)

# Model Training
# 1. Linear Regression
#print("\n\n Using linear regression \n\n")
lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train, Y_train)

joblib.dump(lin_reg_model, 'linear_regression_model.pkl')


# Model Evaluation
# Prediction on Training data
training_data_prediction = lin_reg_model.predict(X_train)

# R squared error
error_score = metrics.r2_score(Y_train, training_data_prediction)
#print("The R squared error is: ", error_score)

# Visualize the actual and predicted prices
plt.scatter(Y_train, training_data_prediction)
plt.xlabel('Actual prices (Y_train)')
plt.ylabel('Predicted prices (training_data_prediction)')
plt.title('Actual prices vs Predicted Price using linear regression')
plt.show()

# Prediction on Test data
test_data_prediction = lin_reg_model.predict(X_test)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
#print("The R squared error is: ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel('Actual prices (Y_test)')
plt.ylabel('Predicted prices (test_data_prediction)')
plt.title('Actual prices vs Predicted Price using linear regression')
plt.show()


# 2. Lasso Regression


#print("\n\n Using lasso regression now \n\n")


las_reg_model = Lasso()
las_reg_model.fit(X_train, Y_train)

joblib.dump(las_reg_model, 'lasso_regression_model.pkl')

# Prediction on Training data
training_data_prediction = las_reg_model.predict(X_train)

# R squared error
error_score = metrics.r2_score(Y_train, training_data_prediction)
#print("The R squared error is: ", error_score)

plt.scatter(Y_train, training_data_prediction)
plt.xlabel('Actual prices (Y_train)')
plt.ylabel('Predicted prices (training_data_prediction)')
plt.title('Actual prices vs Predicted Price using lasso regression')
plt.show()

# Prediction on Test data
test_data_prediction = las_reg_model.predict(X_test)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
#print("The R squared error is: ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel('Actual prices (Y_test)')
plt.ylabel('Predicted prices (test_data_prediction)')
plt.title('Actual prices vs Predicted Price using lasso regression')
plt.show()

joblib.dump(X_train.columns, 'model_features.pkl')