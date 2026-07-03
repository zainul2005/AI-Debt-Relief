import "./StatsCard.css";

function StatsCard({
  title,
  value,
  color
}) {
  return (
    <div
      className="stats-card"
      style={{
        borderTop: `4px solid ${color}`
      }}
    >
      <h4>{title}</h4>

      <h2
        style={{
          color: color
        }}
      >
        {value}
      </h2>

      <p>
        Updated Today
      </p>
    </div>
  );
}

export default StatsCard;