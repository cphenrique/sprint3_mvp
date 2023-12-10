import { useEffect, useState } from "react"
import Analista from "../components/Analista"
import axios from 'axios'

export default function Analistas() {
  const [analistaList, setAnalistList] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/get_analistas')
      .then(res => setAnalistList(res.data.analistas))
      .catch(error => console.log(error))
  }, [])

  return (
    <div>
      <header>
      </header>

      <section className="banner">
      </section>

      <section className="main-products">
        {analistaList.map((p, index) => (
          <Analista key={index} analista={p} />
        ))}
      </section>
      
      <footer></footer>
    
    </div>
  )
}