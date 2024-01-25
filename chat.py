from openai import OpenAI

client = OpenAI()

def createAssistant() -> str:
  content = ""
  
  with open("context.txt", "r") as f:
    content = f.read()
    f.close()
  
  assistant = client.beta.assistants.create(instructions=content,  name="Test Assistant", model="gpt-3.5-turbo-16k")
  
  return assistant.id

def createMessage(threadId: str, msg: str) -> str:
  message = client.beta.threads.messages.create(
    thread_id=threadId,
    role="user",
    content=msg,
  )

  return message.id

def createThread() -> str:
  thread = client.beta.threads.create()

  return thread.id

def createThreadWithBasicData(instruction: str) -> str:
  thread = client.beta.threads.create(messages=[{
    "role": "user",
    "content": instruction,
  }])

  return thread.id

def executeMessage(assistantId: str, threadId: str) -> str:
  run = client.beta.threads.runs.create(assistant_id=assistantId, thread_id=threadId)

  return run.id

def retriveMessage(threadId: str, runId: str) -> str:
  try:
    run = client.beta.threads.runs.retrieve(thread_id=threadId, run_id=runId, timeout=10)

    if run.completed_at:
      messages = client.beta.threads.messages.list(thread_id=threadId)
      last_message = messages.data[0]

      return last_message.content[0].text.value
  except:
    print('some error ocurred when try to retrive execution of message!')
