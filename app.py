from flask import Flask, request, render_template_string
import pickle

# Create Flask app instance
app = Flask(__name__)

# Load the KNN model
with open('models/svm_model.sav', 'rb') as knn_file:
    knn_model = pickle.load(knn_file)

# Define the HTML template as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Cost Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }
        h2 {
            color: #333;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            text-align: left;
        }
        input[type="number"],
        input[type="submit"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: white;
            cursor: pointer;
            border: none;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        h3 {
            color: #333;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Predict Medical Charges</h2>
        <form action="/predict" method="POST">
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required><br>

            <label for="gender">Gender (0: Female, 1: Male):</label>
            <input type="number" id="gender" name="gender" required><br>

            <label for="bmi">BMI:</label>
            <input type="number" id="bmi" name="bmi" step="0.1" required><br>

            <label for="children">Number of Children:</label>
            <input type="number" id="children" name="children" required><br>

            <label for="smoker">Smoker (0: No, 1: Yes):</label>
            <input type="number" id="smoker" name="smoker" required><br>

            <label for="region">Region (0: Northwest, 1: Southeast, 2: Southwest, 3: Northeast):</label>
            <input type="number" id="region" name="region" required><br>

            <input type="submit" value="Predict Medical Cost">
        </form>

        {% if prediction_text %}
            <h3>{{ prediction_text }}</h3>
        {% endif %}
    </div>
</body>
</html>
'''

# Define the home route
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Define the predict route to take input and predict medical costs
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    age = int(request.form['age'])
    gender = int(request.form['gender'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])  # Use label encoding

    # Create a list of inputs as per the model's requirement
    input_features = [[age, gender, bmi, children, smoker, region]]

    # Make prediction using the KNN model
    predicted_cost = knn_model.predict(input_features)

    # Render the result in HTML
    return render_template_string(HTML_TEMPLATE, prediction_text=f'Predicted Medical Cost: ${predicted_cost[0]:.2f}')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
