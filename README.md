# Automated Jewellery 3D Model Generator

![Image]('presentation generator 1.png')

This Streamlit application enables users to generate 3D models of jewellery designs automatically. It utilizes OpenAI's language models for generating image prompts and DALL·E 3 for image generation. Additionally, it integrates with the CSM API for 3D model generation.

## Features

- **Jewellery Image Prompt Generation**: Generate prompts for jewellery design images.
- **DALL·E 3 Image Generation**: Generate jewellery design images using DALL·E 3 based on the provided prompts.
- **3D Model Generation with CSM**: Generate 3D models of jewellery designs using the CSM API.
- **Customization**: Customize prompts for image generation.

## Prerequisites

Before running the application, make sure you have the following:

- Python installed on your machine
- Streamlit library
- OpenAI API key
- CSM API key (for 3D model generation)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/automated-jewellery-3d-model-generator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd automated-jewellery-3d-model-generator
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    streamlit run main.py
    ```

2. **Access the application:**

    Open your web browser and go to `http://localhost:8501`.

3. **Provide API keys:**

    - Enter your OpenAI API key and CSM API key in the provided text inputs.

4. **Generate Jewellery Image Prompt:**

    - Enter your prompt and select styles for the jewellery design.

5. **Generate DALL·E 3 Image:**

    - Click the "Generate Image" button to generate the jewellery design image based on the provided prompt.

6. **Generate 3D Model with CSM:**

    - Enter the image URL for 3D model generation and click the "Generate 3D Model" button.

7. **Check 3D Model Status:**

    - The application will check the status of 3D model generation and display the result once completed.

## License

This project is licensed under the [MIT License](LICENSE).
