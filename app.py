import streamlit as st
import cohere
from PIL import Image

# === COHERE SETUP ===
cohere_api_key = "vzSUUNFPnI6IBHil4qwn0rQxVDegkZaHL9cZNNiR"  # Replace with your real key
co = cohere.Client(cohere_api_key)

# === STREAMLIT UI CONFIG ===
st.set_page_config(page_title="Cohere Food Calorie Analyzer")
st.header("🍽️ Cohere Calorie Checker (Text-Based)")

# === INPUT FIELDS ===
user_description = st.text_area("Describe the food items you see in the image (e.g., '2 samosas, 1 Coke, and salad'):")

uploaded_file = st.file_uploader("Upload the image (optional, just for display)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# === PROMPT TEMPLATE ===
calorie_prompt_template = """
You're a professional nutritionist. Based on the following food description, provide the total estimated calories and a breakdown:

Format:
1. Item - estimated calories
2. Item - estimated calories

Also, give a final total.

Food Description: {description}
"""

submit = st.button("Analyze Calories")

# === MAIN LOGIC ===
if submit and user_description:
    full_prompt = calorie_prompt_template.format(description=user_description)
    
    response = co.generate(
        model='command',
        prompt=full_prompt,
        max_tokens=200,
        temperature=0.6
    )
    
    st.subheader("🍔 Nutritional Breakdown:")
    st.write(response.generations[0].text.strip())