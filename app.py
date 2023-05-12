import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Define a function to predict the salary based on the input features
def predict_salary(experience, test_score, interview_score):
    # Convert the input to a numpy array
    input_features = np.array([[experience, test_score, interview_score]])
    # Use the trained model to make a prediction
    prediction = model.predict(input_features)[0]
    return prediction

# Define the Streamlit app
def main():
    # Set the title and the header
    st.title("Salary Predictor")
    st.header("Enter the following details to predict the salary:")

    # Create input fields for the three features
    experience = st.slider("Experience", 0, 12, 5)
    test_score = st.slider("Test Score", 0, 100, 50)
    interview_score = st.slider("Interview Score", 0, 10, 5)

    # Display a button to make the prediction
    if st.button("Predict Salary"):
        # Call the predict_salary function to make the prediction
        prediction = predict_salary(experience, test_score, interview_score)
        # Display the prediction
        st.success(f"Predicted Salary is $ {prediction:.2f}")

if __name__ == "__main__":
    main()
