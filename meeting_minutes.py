from opeanai import OpenAI

client = OpenAI(
  os.environ.get("OPENAI_API_KET")
  api_key="My API Key"
  )
from docx import Document

def transkrybuj_glos(audio_file_path):
  with open(audio_file_path, 'rb') as audio_file:
    transkrybcja = client.audio.transcriptions.create("whisper-1",audio_file)
  return transkrybcja['text']
