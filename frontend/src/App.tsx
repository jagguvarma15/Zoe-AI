import ChatBox from './components/ChatBox'
import FileUpload from './components/FileUpload'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-4xl font-bold text-center text-indigo-600 mb-6">Zoe AI</h1>
      <FileUpload />
      <ChatBox />
    </div>
  )
}
