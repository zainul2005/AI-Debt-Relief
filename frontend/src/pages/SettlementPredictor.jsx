import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import "../App.css";

function SettlementPredictor() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main">

        <Navbar />

        <h2 style={{marginBottom:"25px"}}>
          Settlement Prediction
        </h2>

        <div className="stats">

          <StatsCard
            title="Predicted Settlement"
            value="65%"
            color="#2563eb"
          />

          <StatsCard
            title="Suggested Offer"
            value="₹3,25,000"
            color="#22c55e"
          />

          <StatsCard
            title="Savings"
            value="₹1,75,000"
            color="#10b981"
          />

          <StatsCard
            title="Success Chance"
            value="High"
            color="#f59e0b"
          />

        </div>

        <div className="profile">

          <h2>AI Recommendation</h2>

          <p
            style={{
              color:"#cbd5e1",
              lineHeight:"1.8"
            }}
          >
            Based on the borrower's financial profile,
            income, expenses, and outstanding debt,
            the AI recommends negotiating a settlement
            around 65% of the outstanding amount.
          </p>

        </div>

      </div>

    </div>
  );
}

export default SettlementPredictor;