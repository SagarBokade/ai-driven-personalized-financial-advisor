API Documentation for AI-Driven Personalized Financial Advisor

1. Overview
    This project uses APIs to fetch real-time financial data and interact with the Large Language Model (LLM) for generating personalized financial advice. Below are the essential API details to get started.

2. API Usage Instructions
    
    1. Set Up API Access:
    Obtain your API key from the relevant provider (e.g., Hugging Face).
    Add the API key in the project code where required, such as the InferenceClient initialization.
        Example in Python:

        llm_client = InferenceClient(
            model=repo_id,
            timeout=120,
            token='your_api_key_here'
        )

    2. Required Libraries:
        Ensure the following libraries are installed:
            Flask
            huggingface_hub
            datetime

    Install them using:
        "pip install Flask huggingface_hub"
    
    3. Run the API:
    Launch the Flask application:
        "python app.py"
    Access the chatbot via http://127.0.0.1:5000/.

3. Key Notes

    Authentication:
        You must use a valid API key for the Hugging Face Phi-3.5-mini-instruct model. Replace your_api_key_here with your actual key.

    Error Handling:
        If you encounter errors:
            Check the internet connection for API access.
            Ensure the API key is valid and has not expired.

    Timeouts:
        The API timeout is set to 120 seconds. You can adjust it in the InferenceClient settings.

4. Troubleshooting
    Issue: API key not recognized
        Solution: Verify and replace the key in the code.

    Issue: Model not responding
        Solution: Check the internet connection and ensure the model repository is accessible on Hugging Face.

    Issue: Dependency errors
        Solution: Ensure all required libraries are installed using pip install.

This document ensures that users understand how to configure and use the APIs integrated into your project. Let me know if you need further customization! 
