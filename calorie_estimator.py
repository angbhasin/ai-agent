import os
import base64
import io
from dotenv import load_dotenv
from PIL import Image
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set")

# Initialize the Gemini API client
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")  # or gemini-1.5-pro

def image_to_base64(img):
    """Convert an image to a base64 URL."""
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    return 'data:image/jpeg;base64,' + base64.b64encode(buffered.getvalue()).decode("utf-8")

def estimate_calories(prompt, img):
    """Estimate calories using the Gemini API."""
    message = HumanMessage(content=[
        {'type': 'text', 'text': prompt},
        {'type': 'image_url', 'image_url': image_to_base64(img)}
    ])
    response = model.stream([message])

    # Collect and return the response
    buffer = []
    for chunk in response:
        buffer.append(chunk.content)
    return ''.join(buffer)

if __name__ == "__main__":
    # Define the prompt for calorie estimation
    prompt = "Estimate the total calories for the food items in this image."

    # Load an image with PIL
    image_path = "apple.jpg"  # Replace with your image path
    img = Image.open(image_path)

    # Call the Gemini API to estimate calories
    try:
        calorie_estimation = estimate_calories(prompt, img)
        print(f"Calorie Estimation: {calorie_estimation}")
    except Exception as e:
        print(f"An error occurred: {e}")