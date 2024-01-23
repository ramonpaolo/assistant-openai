from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
from os import getenv
import uvicorn

load_dotenv()

import chat
from models import BodyMessage, User

app = FastAPI()

assistant_id = getenv("ASSISTANT_ID")

if __name__ == "__main__":
  isDevelopment = getenv("APP_ENV") == "development"

  uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=isDevelopment)

  if assistant_id == None:
    assistant_id = chat.createAssistant()


@app.get("/health_check")
def get_health_check() -> object:
  return {
    "status": "ok"
  }

@app.post("/chat")
def create_chat(User: User) -> object:
  threadId = chat.createThreadWithBasicData(f"Hello! My name is {User.name} and I have interest in this service!")

  return JSONResponse(jsonable_encoder({
    "status": "success",
    "message": "created thread with success",
    "data": {
      "thread_id": threadId,
    },
  }), 201)

@app.post("/chat/{threadId}")
def publish_message(threadId: str, Body: BodyMessage) -> object:
  messageId = chat.createMessage(threadId, Body.message)
  runId = chat.executeMessage(assistant_id, threadId)
  
  return JSONResponse(jsonable_encoder({
    "status": "success",
    "message": "message published with success",
    "data": {
      "thread_id": threadId,
      "message_id": messageId,
      "run_id": runId,
    },
  }), 201)

@app.get("/chat/{threadId}")
def get_message(threadId: str, run_id: str) -> object:
  message = chat.retriveMessage(threadId, run_id)

  return JSONResponse(jsonable_encoder({
    "status": "success",
    "message": "message get with success",
    "data": {
      "run_id": run_id,
      "message": message,
    },
  }), 200)