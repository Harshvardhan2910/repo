from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS correctly
import joblib
import pickle


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

with open('XGBoost.pkl', 'rb') as file:
    model = pickle.load(file)

# @app.route('/predict', methods=['POST'])
# def predict():
    # data = request.json
    # try:
    #     # Log the input data to ensure it's being received
    #     print("Received data:", data)

    #     # Prepare input for the model
    #     input_features = [
    #         int(data['nitrogen']),
    #         int(data['phosphorus']),
    #         int(data['potassium']),
    #         float(data['temperature']),
    #         float(data['humidity']),
    #         float(data['pH']),
    #         float(data['rainfall'])
    #     ]

    #     # Log the input features to check if they are correct
    #     print("Input features:", input_features)

    #     # Make the prediction
    #     prediction = model.predict([input_features])

    #     # Log the prediction to ensure the model works
    #     print("Model prediction:", prediction)
        

    #     return jsonify({'prediction': prediction[0]})
    # except Exception as e:
    #     # Print any errors for debugging
    #     print("Error during prediction:", str(e))
    #     return jsonify({'error': str(e)})



crop_mapping = {
0: 'apple',
1: 'banana',
2: 'blackgram',
3: 'chickpea',
4: 'coconut',
5: 'coffee',
6: 'cotton',
7: 'grapes',
8: 'jute',
9: 'kidneybeans',
10: 'lentil',
11: 'maize',
12: 'mango',
13: 'mothbeans',
14: 'mungbean',
15: 'muskmelon',
16: 'orange',
17: 'papaya',
18: 'pigeonpeas',
19: 'pomegranate',
20: 'rice',
21: 'watermelon'

}


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        # Log the input data to ensure it's being received
        print("Received data:", data)

        # Prepare input for the model
        input_features = [
            int(data['nitrogen']),
            int(data['phosphorus']),
            int(data['potassium']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['pH']),
            float(data['rainfall'])
        ]

        # Log the input features to check if they are correct
        print("Input features:", input_features)

        # Make the prediction
        prediction = model.predict([input_features])

        # Log the prediction to ensure the model works
        print("Model prediction:", prediction)

        # Convert prediction to a standard type
        predicted_crop = crop_mapping.get(prediction[0], "Unknown Crop") # Convert to int if it's an integer
        # If your model predicts crop names, you may need to convert to string or retrieve from a mapping

        return jsonify({'prediction': predicted_crop})
    except Exception as e:
        # Print any errors for debugging
        print("Error during prediction:", str(e))
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)