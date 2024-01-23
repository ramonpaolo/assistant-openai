from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

from chat import createThread, createMessage, executeMessage, retriveMessage, createAssistant
from models import BodyMessage

app = FastAPI()

assistant_id = getenv("ASSISTANT_ID")

if __name__ == "main":
  if assistant_id == None:
    assistant_id = createAssistant()

@app.post("/chat")
def create_chat() -> object:
  threadId = createThread()
  
  return {
    "status": "success",
    "message": "created thread with success",
    "data": {
      "thread_id": threadId,
    },
  }

@app.post("/chat/{threadId}")
def publish_message(threadId: str, Body: BodyMessage) -> object:
  messageId = createMessage(threadId, Body.message)
  runId = executeMessage(assistant_id, threadId)
  
  return {
    "status": "success",
    "message": "message published with success",
    "data": {
      "thread_id": threadId,
      "message_id": messageId,
      "run_id": runId,
    },
  }

@app.get("/chat/{threadId}")
def get_message(threadId: str, run_id: str) -> object:
  message = retriveMessage(threadId, run_id)

  return {
    "status": "success",
    "message": "message get with success",
    "data": {
      "run_id": run_id,
      "message": message,
    },
  }