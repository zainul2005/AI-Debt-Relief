import "./StatsCard.css";

export default function StatsCard({
  title,
  value,
  color
}) {
  return (
    <div
      className="statsCard"
      style={{
        borderTop: `3px solid ${color}`,
      }}
    >
      <p>{title}</p>

      <h2>{value}</h2>
    </div>
  );
}