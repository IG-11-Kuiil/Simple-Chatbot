import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = next(iter(uploaded))
from google import genai
client = genai.Client(vertexai=True, project="autonomous-tube-464110-b3", location="us-central1")
MODEL = "gemini-2.0-flash"
history = []
