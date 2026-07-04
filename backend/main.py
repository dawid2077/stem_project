from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel,Field
from typing import Literal,List
import asyncio

#Defined App
app = FastAPI(
    title="Flutter AI Backend",
    description="A minimalist starting point for AI streaming",
    version="1.0.0"
)


#Flutter things for functionality
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, specify your Flutter app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#Pydantic data structures
class Message(BaseModel):
    role: Literal["user","assistant","system"]
    content: str =Field(
        min_length=1,
        max_length=4096,
        description="The prompt that will be sent to the Ai",
        examples=[
            "Najlepszy uniwersytet w polsce z kierunkiem Matematyka",
            "Czy Na studia informatyczne na Uś trzeba mature rozserzona z angielskiego i matematki?"
            ]
    )
class ChatHistory(BaseModel):
    conversation: list[Message]


#here will be the logic for  calling llm and streaming the response
async def llm_call(chat_data: ChatHistory):
    yield


#here i will uswae text/event-stream and SSE logic

@app.post(
        "/chat/stream",
        summary="Stream Ai Response and Accepts Prompts",
        description='Here is the logic for user prompts and llm responses. It accepts the messages from Flutter'
          )
async def stream_chat(chat_data: ChatHistory):
    return StreamingResponse(
        llm_call(chat_data),
        media_type="text/event-stream"
    )