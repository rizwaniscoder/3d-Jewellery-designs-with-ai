
import streamlit as st
import openai
import requests
import json
import os

# Retrieve OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Retrieve CSM API key from environment variable
csm_api_key = os.getenv("CSM_API_KEY")

  
# Initialize image_url and session_code
image_url = ""
session_code = ""

# Streamlit app
def main():
    global image_url, session_code  # Declare image_url and session_code as global variables
    st.title("Automated Jewellery 3D Model Generator")

    # Step 1: Jewellery Image Prompt Generation
    st.header("Step 1: Jewellery Image Prompt Generation")
    user_prompt = st.text_input("Enter your prompt:")
    st.write("- Select styles for your jewellery design:")
    style_options = ["Modern", "Minimalist", "Classic", "Vintage", "Bohemian", "Art Deco", "Gothic", "Ethnic", "Geometric", "Nature-inspired", "Futuristic", "Industrial", "Romantic", "Abstract", "Retro", "Avant-Garde", "Sporty", "Elegant", "Casual", "Eclectic"]
    selected_styles = st.multiselect("Select Styles:", style_options, key="style_multiselect")

    # Initialize generated_prompt
    generated_prompt = ""

    combined_prompt = f"{user_prompt} the image must have a white background and the styles should include {', '.join(selected_styles).lower()}"
    
    if st.button("Generate Prompt", key="generate_prompt_button"):
        generated_prompt = generate_jewellery_prompt(combined_prompt)
        st.success(f"Generated Prompt: {generated_prompt}")

    # Step 2: DALL·E 3 Image Generation
    st.header("Step 2: DALL·E 3 Image Generation")
    image_prompt = st.text_input("Generated Image Prompt:", value=generated_prompt, key="image_prompt")
    custom_image_prompt = st.text_input("Customize Image Prompt (Optional):", key="custom_image_prompt")
    
    if st.button("Generate Image", key="generate_image_button"):
        try:
            if custom_image_prompt:
                image_url = generate_image(custom_image_prompt)
            else:
                image_url = generate_image(image_prompt)
            st.image(image_url, caption="Generated Image", use_column_width=True)
        except KeyError as e:
            st.error(f"Error: {e}. Please check your image prompt and try again.")

    # Step 3: 3D Model Generation with CSM
    st.header("Step 3: 3D Model Generation with CSM")
    csm_image_url = st.text_input("Enter image URL for 3D model generation:", value=image_url, key="csm_image_url")
    if st.button("Generate 3D Model", key="generate_3d_model_button"):
        if csm_image_url:  # Check if the input is not empty
            csm_response = generate_3d_model(csm_image_url)
            if "session_code" in csm_response["data"]:
                session_code = csm_response["data"]["session_code"]
                st.success(f"3D Model Generation Request Sent. Session Code: {session_code}")
                st.json(csm_response)
                check_3d_model_status(session_code)
            else:
                st.error("Error: Session code not found in the response.")
        else:
            st.error("Please provide a non-empty image URL for 3D model generation.")

# Function to generate jewellery image prompt
def generate_jewellery_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"]

# Function to generate image using DALL·E 3
def generate_image(image_prompt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response["data"][0]["url"]
    return image_url

# Function to generate 3D model using CSM
def generate_3d_model(image_url):
    url = "https://api.csm.ai:5566/image-to-3d-sessions"
    payload = json.dumps({
        "image_url": image_url
    })
    headers = {
        'x-api-key': csm_api_key,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

# Function to check 3D model status and fetch the model URL
def check_3d_model_status(session_code):
    url = f"https://api.csm.ai:5566/image-to-3d-sessions/{session_code}"
    headers = {'x-api-key': csm_api_key}
    st.info("Checking 3D Model Generation Status...")
    while True:
        response = requests.get(url, headers=headers)
        data = response.json().get("data", {})
        status = data.get("status")
        if status == "finished":
            st.success("3D Model Generation Completed.")
            st.json(data)
            break
        elif status == "failed":
            st.error("3D Model Generation Failed.")
            break

if __name__ == "__main__":
    main()
