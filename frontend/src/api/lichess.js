const API_URL = "http://127.0.0.1:8000";

export async function fetchGames({ limit = 10, rated = null }) {
  const params = new URLSearchParams({ limit });

  if (rated !== null) {
    params.append("rated", rated);
  }

  const res = await fetch(
    `http://localhost:8000/games?${params.toString()}`,
    { credentials: "include" }
  );

  if (!res.ok) {
    throw new Error("Ошибка загрузки игр");
  }

  return res.json();
}
