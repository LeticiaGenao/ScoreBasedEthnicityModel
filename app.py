from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and the encoder
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect and convert scores to float
        math_score = float(request.form['math_score'])
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])

        # Prepare features for prediction
        final_features = np.array([[math_score, reading_score, writing_score]])

        # Predict using the loaded model
        prediction = model.predict(final_features)
        output_label = encoder.inverse_transform(prediction)[0]  # Transform numeric prediction back to original label

        prediction_text = f'Predicted Race/Ethnicity Group: {output_label}'

    except ValueError:
        prediction_text = "Please ensure all inputs are valid numbers."
    except Exception as e:
        prediction_text = f"An error occurred: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
