from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from langgraph_app.agent import run_agent
from file_upload import process_file

app = FastAPI()

# Enable CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(message: str, session_id: str):
    return run_agent(message, session_id)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    result = await process_file(file)
    return {"status": "uploaded", "info": result}

from chat_history_store import add_message, get_history

@app.post("/chat")
async def chat_endpoint(message: str, session_id: str):
    add_message(session_id, "user", message)
    result = run_agent(message, session_id)
    add_message(session_id, "bot", result["response"])
    return result

@app.get("/history")
async def history(session_id: str):
    return get_history(session_id)
