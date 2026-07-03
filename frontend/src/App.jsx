import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import FinancialHealth from "./pages/FinancialHealth";
import SettlementPredictor from "./pages/SettlementPredictor";
import NegotiationEmail from "./pages/NegotiationEmail";
import KnowYourRights from "./pages/KnowYourRights";
import History from "./pages/History";

function App() {
  return (
    <Routes>

      <Route
        path="/"
        element={<Dashboard />}
      />

      <Route
        path="/financial-health"
        element={<FinancialHealth />}
      />

      <Route
        path="/settlement-predictor"
        element={<SettlementPredictor />}
      />

      <Route
        path="/negotiation-email"
        element={<NegotiationEmail />}
      />

      <Route
        path="/know-your-rights"
        element={<KnowYourRights />}
      />

      <Route
        path="/history"
        element={<History />}
      />

    </Routes>
  );
}

export default App;