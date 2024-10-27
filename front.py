import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("health_risk_model.pkl", "rb") as f:
    model = pickle.load(f)

risk_mapping = {
    1: "Low Risk: Diabetic",
    2: "Moderate Risk: Pneumonia",
    3: "High Risk: Cancer"
}

# Streamlit app function
def main():
    st.title("Health Risk Prediction by BMI")
    st.write("Enter your details to predict health risk based on BMI.")

    # Input fields
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Gender", options=["Female", "Male"])
    smoking_status = st.selectbox("Smoking Status", options=["Non-smoker", "Smoker"])
    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, step=0.5)
    height = st.number_input("Height (m)", min_value=10.0, max_value=200.5, step=0.01)

    # Calculate BMI
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your calculated BMI is: {bmi:.2f}")
    else:
        bmi = 0

    # Encode categorical inputs
    gender_encoded = 1 if gender == "Male" else 0
    smoking_status_encoded = 1 if smoking_status == "Smoker" else 0

    # Predict health risk
    if st.button("Predict Health Risk"):
        if bmi > 0:
            # Prepare the input data in the expected order
            input_data = np.array([[age, gender_encoded, smoking_status_encoded, bmi]])
            # risk_prediction = model.predict(input_data)
            encoded_prediction = model.predict(input_data)[0]
            risk_prediction = risk_mapping.get(encoded_prediction, "Unknown Risk")
            st.write(f"Predicted Health Risk: {risk_prediction}")
            
        else:
            st.write("Please enter a valid height.")

if __name__ == "__main__":
    main()
