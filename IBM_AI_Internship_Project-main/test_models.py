import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY", "")
if api_key:
    genai.configure(api_key=api_key)
    try:
        for model in genai.list_models():
            print(model.name)
    except Exception as e:
        print("Model listing error:", e)
else:
    print("No GEMINI_API_KEY set in environment. Skipping model listing test.")