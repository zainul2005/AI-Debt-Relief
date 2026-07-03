import "./Navbar.css";

export default function Navbar() {
  return (
    <header className="navbar">

      <div className="navbar-left">

        <h1>Dashboard Overview</h1>

        <p>
          Your financial snapshot at a glance
        </p>

      </div>

      <div className="navbar-right">

        <button className="notification-btn">
          🔔
        </button>

        <button className="profile-btn">
          👤 My Profile
        </button>

      </div>

    </header>
  );
}