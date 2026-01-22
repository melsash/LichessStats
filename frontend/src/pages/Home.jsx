import { useEffect, useState } from "react";
import { fetchGames } from "../api/lichess";
import GameList from "../components/GameList";
import Loader from "../components/Loader";
import Filters from "../components/Filters";

const API_BASE = "http://localhost:8000";

export default function Home() {
  const [authenticated, setAuthenticated] = useState(false);
  const [checkingAuth, setCheckingAuth] = useState(true);

  const [games, setGames] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [filters, setFilters] = useState({ limit: 10 });

  useEffect(() => {
    fetch(`${API_BASE}/auth/status`, {
      credentials: "include",
    })
      .then((res) => res.json())
      .then((data) => setAuthenticated(data.authenticated))
      .finally(() => setCheckingAuth(false));
  }, []);

  const login = () => {
    window.location.href = `${API_BASE}/auth/login`;
  };

  const loadGames = async (params = filters) => {
  setLoading(true);
  setError(null);

  try {
    const data = await fetchGames(params);

    if (!data.games || data.games.length === 0) {
      setGames([]);
    } else {
      setGames(data.games);
    }
  } catch (e) {
    setError(e.message || "Ошибка загрузки игр");
  } finally {
    setLoading(false);
  }
};

  useEffect(() => {
   if (authenticated) {
      loadGames(filters);
    }
  }, [authenticated]);



  if (checkingAuth) {
    return <div className="container">Проверка авторизации…</div>;
  }

  return (
    <div className="container">

      {!authenticated ? (
        <>
          <p>Войдите через Lichess, чтобы загрузить игры</p>
          <button onClick={login}>Войти через Lichess</button>
        </>
      ) : (
        <>
          <p className="success">Вы вошли через Lichess</p>

           <Filters
            onChange={(f) => {
            setFilters(f);
            loadGames(f);
            }}
            />

          <button onClick={() => loadGames()}>Загрузить игры</button>

         {loading && <Loader text="Загружаем игры…" />}

        {!loading && games.length === 0 && !error && (
        <p className="muted">Нет игр по выбранным фильтрам</p>
        )}

        {error && <p className="error">{error}</p>}

        {games.length > 0 && <GameList games={games} />}

        </>
      )}
    </div>
  );
}
