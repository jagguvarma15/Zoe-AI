import { useState } from "react"
import axios from "axios"

interface UploadResponse {
  info: {
    chunks: number
  }
}

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null)
  const [status, setStatus] = useState("")

  const handleUpload = async () => {
    if (!file) return
    const formData = new FormData()
    formData.append("file", file)

    try {
      const res = await axios.post<UploadResponse>("http://localhost:8000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })

      setStatus(`✅ Indexed ${res.data.info.chunks} chunks.`)
    } catch (err) {
      setStatus("❌ Upload failed.")
    }
  }

  return (
    <div className="max-w-xl mx-auto bg-white p-4 rounded shadow mt-8">
      <label className="block mb-2 text-sm font-medium">Upload a PDF or text file</label>
      <input
        type="file"
        accept=".pdf,.txt"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="mb-3"
      />
      <button
        className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700"
        onClick={handleUpload}
      >
        Upload & Index
      </button>
      <p className="mt-2 text-sm">{status}</p>
    </div>
  )
}
