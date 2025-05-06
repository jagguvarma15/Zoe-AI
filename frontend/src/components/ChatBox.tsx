import { useState, useEffect } from "react"
import axios from "axios"

interface Message {
  sender: "user" | "bot"
  text: string
}

interface ChatResponse {
  response: string
}

export default function ChatBox() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState("")
  const sessionId = "demo-session" // Later: generate UUID per session

  // 🧠 Load chat history on mount
  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const res = await axios.get<Message[]>(`http://localhost:8000/history`, {
          params: { session_id: sessionId }
        })
        setMessages(res.data)
      } catch (err) {
        console.error("Failed to fetch history", err)
      }
    }
    fetchHistory()
  }, [])

  const sendMessage = async () => {
    if (!input.trim()) return
    const userMessage: Message = { sender: "user", text: input }
    setMessages(prev => [...prev, userMessage])
    setInput("")

    try {
      const res = await axios.post<ChatResponse>("http://localhost:8000/chat", {
        message: userMessage.text,
        session_id: sessionId
      })

      const botMessage: Message = { sender: "bot", text: res.data.response }
      setMessages(prev => [...prev, botMessage])
    } catch (err) {
      setMessages(prev => [...prev, { sender: "bot", text: "Error connecting to server." }])
    }
  }

  return (
    <div className="max-w-xl mx-auto space-y-4 mt-8">
      <div className="h-[400px] overflow-y-auto bg-white rounded shadow p-4 space-y-2">
        {messages.map((msg, idx) => (
          <div key={idx} className={`text-${msg.sender === "user" ? "right" : "left"}`}>
            <div className={`inline-block px-4 py-2 rounded-xl ${msg.sender === "user" ? "bg-blue-100" : "bg-gray-200"}`}>
              {msg.text}
            </div>
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          className="flex-1 border px-4 py-2 rounded shadow"
          placeholder="Ask Zoe..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button className="bg-indigo-600 text-white px-4 rounded" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  )
}
