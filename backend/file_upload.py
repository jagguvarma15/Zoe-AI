from fastapi import UploadFile
import os
import shutil
from rag.document_loader import process_and_index

async def process_file(file: UploadFile):
    temp_path = f"./temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_and_index(temp_path)
    os.remove(temp_path)
    return result
