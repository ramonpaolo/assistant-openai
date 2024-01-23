from fastapi import FastAPI

from chat import createThread, createMessage, executeMessage, retriveMessage
from models import BodyMessage

app = FastAPI()

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
  runId = executeMessage("asst_uVB4evcqqMVbev3nrKR909PP", threadId)
  
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