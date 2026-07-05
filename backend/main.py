from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel,Field
from typing import Literal,List
from dotenv import load_dotenv
import asyncio
import os
from openai import AsyncOpenAI


#loaduje zmienne z .env
load_dotenv(dotenv_path="../.env")
openrouter_api_key=os.getenv("OPENROUTER_API_KEY")

#Defined App
app = FastAPI(
    title="Flutter AI Backend",
    description="A minimalist starting point for AI streaming",
    version="1.0.0"
)
#initiated the client using OpenAi sdk
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_api_key
)
#tu dajemy używany model z openrouter
model="openai/gpt-4o-mini"


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
    #czeka na utworzenie polaczenia i tu definiujemy strukture
    stream = await client.chat.completions.create(
        model=model,
        messages=[m.model_dump() for m in chat_data.conversation],
        stream=True, #ustawiamy tu model
    )
    async for chunk in stream:
        content=chunk.choices[0].delta.content
        if content:
            yield f"data: {content} \n\n"


#here i will uswae text/event-stream and SSE logic

@app.post(
        "/chat/stream",
        summary="Stream Ai Response and Accepts Prompts",
        description='Here is the logic for user prompts and llm responses. It accepts the messages from Flutter'
          )
async def stream_chat(chat_data: ChatHistory) -> StreamingResponse:
    return StreamingResponse(
        llm_call(chat_data),
        media_type="text/event-stream"
    )