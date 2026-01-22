export default function GameCard({ game }) {
  const resultClass =
    game.result === "win"
      ? "win"
      : game.result === "loss"
      ? "loss"
      : "draw";

  return (
    <div className={`game-card ${resultClass}`}>
      <div className="game-card-header">
        <strong>{game.opponent.username}</strong>
        <span className="result">{game.result.toUpperCase()}</span>
      </div>

      <div className="game-card-meta">
        <span>{game.perf}</span>
        <span>Rating: {game.opponent.rating}</span>
      </div>

      <a
        href={game.url}
        target="_blank"
        rel="noreferrer"
        className="game-link"
      >
        Открыть партию →
      </a>
    </div>
  );
}
