import { useState } from 'react'

import './App.css'
import MainLayout from './components/MainLayout'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <MainLayout />
    </>
  )
}

export default App
