import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Get Gemini API key
GEMINI_API_KEYS = []
for i in range(1, 14):
    key = os.getenv(f'GEMINI_API_KEY_{i}')
    if key:
        GEMINI_API_KEYS.append(key)

main_key = os.getenv('GEMINI_API_KEY')
if main_key:
    GEMINI_API_KEYS.append(main_key)

if not GEMINI_API_KEYS:
    print("No GEMINI_API_KEY found")
    exit()

# List all available models
api_key = GEMINI_API_KEYS[0]
client = genai.Client(api_key=api_key)

print("Available Gemini models:")
print("=" * 50)

try:
    models = client.models.list()
    for model in models:
        print(f"Name: {model.name}")
        if hasattr(model, 'supported_generation_methods'):
            print(f"  Methods: {model.supported_generation_methods}")
        if hasattr(model, 'description'):
            print(f"  Description: {model.description}")
        print()
except Exception as e:
    print(f"Error listing models: {e}")