# Insurance Cost Predictor
This project is a web-based application that predicts medical insurance costs for individuals based on their input features like age, gender, BMI, number of children, smoking status, and residential area. The machine learning models used for this task are K-Nearest Neighbors (KNN) and Support Vector Machine (SVM).

## Table of Contents
* Overview
* Features
* Data
* Installation
* How to Use
* Modeling Details
* Technologies Used
* Contributing
* License

## Overview
This project aims to predict medical insurance costs for a person based on certain attributes using machine learning models. The web interface is built using Flask, and users can input their details to get an estimate of their medical charges. The KNN and SVM models have been trained using a dataset containing the following features:

* Age of the primary beneficiary
* Gender (Male/Female)
* BMI (Body Mass Index)
* Number of dependents
* Smoking status (Yes/No)
* Region (Northeast, Southeast, Southwest, Northwest)
* Medical charges (target variable)

## Features
* Web-based form for entering user data.
* Predict medical charges based on user inputs.
* Option to select between two machine learning models (KNN and SVM).
* Simple, user-friendly interface.

## Data
The dataset used in this project is a health insurance dataset that includes features such as age, gender, BMI, number of children, smoking status, region, and medical charges. The data is preprocessed and label-encoded where necessary.

## Modeling Details
Two machine learning models have been used in this project:

* K-Nearest Neighbors (KNN): A simple, instance-based learning algorithm that predicts values based on the k-nearest neighbors to a data point.
* Support Vector Machine (SVM): A regression model that finds the hyperplane best separating the data points into different categories and makes predictions accordingly.
Model Selection:

* The models were evaluated based on metrics like Mean Squared Error (MSE) and R-squared.
* KNN is chosen for simpler data with fewer variations, while SVM tends to handle complex relationships better.

## Technologies Used
* Python: Programming language used for model development.
* Flask: Web framework used to create the application interface.
* Scikit-learn: Machine learning library used for implementing KNN and SVM.
* HTML/CSS: Used for designing the web interface.
* Pandas, NumPy: For data manipulation and preprocessing.

## License
Project done by Saranya Madala 
