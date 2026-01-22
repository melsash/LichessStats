import GameCard from "./GameCard";

export default function GameList({ games }) {
  if (!games.length) {
    return <p className="muted">Игр пока нет</p>;
  }

  return (
    <div className="game-list">
      {games.map((g) => (
        <GameCard key={g.id} game={g} />
      ))}
    </div>
  );
}
