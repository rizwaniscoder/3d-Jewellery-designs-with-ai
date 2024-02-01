**Automated Jewellery 3D Model Generator**

Welcome to the Automated Jewellery 3D Model Generator! This GitHub repository combines the creative power of OpenAI's GPT-3.5 Turbo and DALL·E 3 models along with the 3D modeling capabilities of the CSM API to bring your unique jewellery designs to life.

Prerequisites
OpenAI API Key: Make sure you have your OpenAI API key set as an environment variable named OPENAI_API_KEY.
CSM API Key: Set your CSM API key as an environment variable named CSM_API_KEY.
Usage
Step 1: Jewellery Image Prompt Generation
Enter your prompt in the provided text input.
Select styles for your jewellery design from the available options.
Click the "Generate Prompt" button to create a tailored prompt for image generation.
Step 2: DALL·E 3 Image Generation
The generated prompt is automatically populated, or you can customize it further.
Optionally, provide a custom image prompt for more control.
Click the "Generate Image" button to see the magic happen.
Step 3: 3D Model Generation with CSM
The generated image or a custom image URL is automatically populated.
Click the "Generate 3D Model" button to initiate the 3D model generation process.
Sit back and relax while the CSM API works its magic.
Once completed, the 3D model and related information will be displayed.
Functions
generate_jewellery_prompt(prompt)
Generates a jewellery image prompt using GPT-3.5 Turbo.

generate_image(image_prompt)
Generates an image using the DALL·E 3 model based on the provided prompt.

generate_3d_model(image_url)
Initiates the generation of a 3D model using the CSM API, given an image URL.

check_3d_model_status(session_code)
Checks the status of 3D model generation and displays the result when completed.
