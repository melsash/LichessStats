import { useEffect, useState } from "react";
import Header from "./components/Header";
import Home from "./pages/Home";
import "./styles/main.css";

export default function App() {
  const [status, setStatus] = useState("Проверяем backend...");

  useEffect(() => {
    fetch("http://localhost:8000")
      .then(() => setStatus("Backend доступен"))
      .catch(() => setStatus("Backend не отвечает"));
  }, []);

  return (
    <div>
      <div style={{ padding: "16px", opacity: 0.8 }}>
        <p>{status}</p>
      </div>
       <Header />
      <Home />
    </div>
  );
}
