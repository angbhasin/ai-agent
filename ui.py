import streamlit as st
from PIL import Image
from calorie_estimator import estimate_calories

# Streamlit UI
st.title("Calorie Estimation App")
st.write("Upload an image of food, and the app will estimate the total calories.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Create two columns
    col1, col2 = st.columns(2)

    # Display the uploaded image in the left column
    with col1:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", width=300)  # Set width to 300 pixels

    # Display the calorie estimation in the right column
    with col2:
        st.write("Analyzing the image...")
        # Define the prompt for calorie estimation
        prompt = "Estimate the total calories for the food items in this image."

        # Call the calorie estimation function
        try:
            calorie_estimation = estimate_calories(prompt, img)
            st.success(f"Calorie Estimation: {calorie_estimation}")
        except Exception as e:
            st.error(f"An error occurred: {e}")