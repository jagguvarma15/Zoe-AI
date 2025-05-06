from collections import defaultdict
from typing import Dict, List

# In-memory store: replace with SQLite or Redis for production
chat_store: Dict[str, List[Dict[str, str]]] = defaultdict(list)

def add_message(session_id: str, sender: str, text: str):
    chat_store[session_id].append({
        "sender": sender,
        "text": text
    })

def get_history(session_id: str) -> List[Dict[str, str]]:
    return chat_store[session_id]
