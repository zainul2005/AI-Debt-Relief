import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import "../App.css";

function FinancialHealth() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main">

        <Navbar />

        <h2 style={{marginBottom:"25px"}}>
          Financial Health Analysis
        </h2>

        <div className="stats">

          <StatsCard
            title="Financial Health"
            value="82%"
            color="#22c55e"
          />

          <StatsCard
            title="Debt Ratio"
            value="30%"
            color="#f59e0b"
          />

          <StatsCard
            title="Monthly Surplus"
            value="₹35,000"
            color="#10b981"
          />

          <StatsCard
            title="Risk Level"
            value="LOW"
            color="#3b82f6"
          />

        </div>

        <div className="profile">

          <h2>Financial Summary</h2>

          <div className="profileGrid">

            <div>
              <label>Total Income</label>
              <h3>₹60,000</h3>
            </div>

            <div>
              <label>Total Expenses</label>
              <h3>₹25,000</h3>
            </div>

            <div>
              <label>Total Savings</label>
              <h3>₹35,000</h3>
            </div>

            <div>
              <label>Outstanding Loan</label>
              <h3>₹5,00,000</h3>
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default FinancialHealth;