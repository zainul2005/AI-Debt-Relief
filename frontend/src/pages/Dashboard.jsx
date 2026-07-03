import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import LoanTable from "../components/LoanTable";
import "../App.css";

function Dashboard() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main">

        <Navbar />

        {/* Statistics Cards */}

        <div className="stats">

          <StatsCard
            title="Monthly Surplus"
            value="₹35,000"
            color="#10b981"
          />

          <StatsCard
            title="Outstanding Loan"
            value="₹5,00,000"
            color="#3b82f6"
          />

          <StatsCard
            title="Total EMI"
            value="₹18,000"
            color="#ef4444"
          />

          <StatsCard
            title="Debt Ratio"
            value="30%"
            color="#f59e0b"
          />

          <StatsCard
            title="Stress Level"
            value="LOW"
            color="#22c55e"
          />

        </div>

        {/* Financial Profile */}

        <div className="profile">

          <h2>Financial Profile</h2>

          <div className="profileGrid">

            <div>
              <label>Monthly Income</label>
              <h3>₹60,000</h3>
            </div>

            <div>
              <label>Monthly Expenses</label>
              <h3>₹25,000</h3>
            </div>

            <div>
              <label>Lump Sum Available</label>
              <h3>₹1,00,000</h3>
            </div>

            <div>
              <label>Total Loans</label>
              <h3>3</h3>
            </div>

            <div>
              <label>Settlement Prediction</label>
              <h3>65%</h3>
            </div>

            <div>
              <label>Financial Health</label>
              <h3>Healthy</h3>
            </div>

          </div>

        </div>

        {/* Active Loans */}

        <div className="loanSection">

          <h2>Active Loans</h2>

          <LoanTable />

        </div>

      </div>

    </div>
  );
}

export default Dashboard;