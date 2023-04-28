import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Holder from './components/Holder'
import Holder2 from './components/Holder2'
import VideoHolder from './components/VideoHolder'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
      <div className="App">
        <Routes>
            <Route path='/' element={<Holder2 />} />
            <Route path='/videos' element={<VideoHolder />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
