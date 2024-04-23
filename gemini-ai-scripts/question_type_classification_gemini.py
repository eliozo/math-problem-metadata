from google.cloud import aiplatform

# Replace with your project ID and endpoint name
project_id = "your-project-id"
endpoint_name = "projects/.../endpoints/your-endpoint-name"

# Authenticate (if necessary, refer to Vertex AI documentation)

# Initialize Vertex AI client
aiplatform.init(project=project_id, location="REGION")  # Replace with your region

# Load the Gemini model
endpoint = aiplatform.Endpoint(endpoint_name=endpoint_name)
model = endpoint.predict()

def generate_text(prompt):
  """Sends a text prompt to Gemini and returns the generated text."""
  response = model.generate_content(requests=[{"prompt": prompt}])
  return response.predictions[0].generated_text

def chat(message):
  """Sends a message to Gemini for conversation and returns the response."""
  chat = model.chat()
  response = chat.send_message(message)
  return response.generated_text

# Example usage
text_prompt = "Write a story about a robot who dreams of becoming a musician."
text_response = generate_text(text_prompt)
print(f"Text prompt response: {text_response}")

chat_message = "What is your favorite type of music?"
chat_response = chat(chat_message)
print(f"Chat response: {chat_response}")