import { useState } from "react";

export default function Filters({ onChange }) {
  const [perf, setPerf] = useState("");
  const [rated, setRated] = useState("");
  const [limit, setLimit] = useState(10);

  const applyFilters = () => {
    onChange({
      perfType: perf || undefined,
      rated:
        rated === ""
          ? undefined
          : rated === "true",
      limit,
    });
  };

  return (
    <div className="filters">
      <select value={perf} onChange={(e) => setPerf(e.target.value)}>
        <option value="">Все режимы</option>
        <option value="blitz">Blitz</option>
        <option value="rapid">Rapid</option>
        <option value="classical">Classical</option>
      </select>

      <select value={rated} onChange={(e) => setRated(e.target.value)}>
        <option value="">Все игры</option>
        <option value="true">Rated</option>
        <option value="false">Casual</option>
      </select>

      <select value={limit} onChange={(e) => setLimit(+e.target.value)}>
        <option value={5}>5</option>
        <option value={10}>10</option>
        <option value={20}>20</option>
        <option value={50}>50</option>
      </select>

      <button onClick={applyFilters}>
        Применить фильтры
      </button>
    </div>
  );
}
