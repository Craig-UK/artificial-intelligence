import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Holder from './components/Holder'
import Holder2 from './components/Holder2'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <Holder2 />
    </div>
  )
}

export default App
