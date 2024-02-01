from os import getenv
from json import dumps, loads

import logging

import chat

logger = logging.getLogger()
logger.setLevel("INFO")

if getenv("APP_ENV") != "production":
  from dotenv import load_dotenv
  load_dotenv()

assistant_id = getenv("ASSISTANT_ID")

def get_health_check() -> object:
  return {"statusCode": 201, "body": dumps({
    "status": "ok"
  })}

def create_chat(event, _) -> object:
  context = ""
  threadId = ""

  User = loads(event["body"])

  if User["name"] != "" and User["name"] != None:
    context = f"Hello! My name is {User['name']} and I have interest in this service!"
    threadId = chat.createThreadWithBasicData(context)
  else:
    threadId = chat.createThread()

  logger.info({
    "message": "chat created with success!",
    "data": {
      "with_context": context != "",
      "context": context,
    },
  })

  return {"statusCode": 201, "body": dumps({
    "status": "success",
    "message": "created thread with success",
    "data": {
      "thread_id": threadId,
    },
  }),
  "headers": {
    "Content-Type": "application/json"
  },}

def publish_message(event, _) -> object:
  threadId = event["pathParameters"]["threadId"]
  message = loads(event["body"])["message"]

  messageId = chat.createMessage(threadId, message)
  runId = chat.executeMessage(assistant_id, threadId)

  logger.info({
    "message": "message published with success",
    "data": {
      "thread_id": threadId,
      "message_id": messageId,
      "run_id": runId,
      "message": message,
    },
  })
  
  return {"statusCode": 201, "body": dumps({
    "status": "success",
    "message": "message published with success",
    "data": {
      "thread_id": threadId,
      "message_id": messageId,
      "run_id": runId,
    },
  }),
  "headers": {
    "Content-Type": "application/json"
  },}

def get_message(event, _) -> object:
  threadId = event["pathParameters"]["threadId"]
  runId = event["queryStringParameters"]["run_id"]

  message = chat.retriveMessage(threadId, runId)

  if message == None:
    logger.info({
      "message": "message not already yet",
      "data": {
        "thread_id": threadId,
        "run_id": runId,
      },
    })
  else:
    logger.info({
      "message": "get message with success",
      "data": {
        "thread_id": threadId,
        "run_id": runId,
        "message": message,
      },
    })

  return {"statusCode": 200, "body": dumps({
    "status": "success",
    "message": "message get with success",
    "data": {
      "run_id": runId,
      "message": message,
    },
  }), "headers": {
    "Content-Type": "application/json"
  }}
