import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../App.css";

function History() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main">

        <Navbar />

        <div className="profile">

          <h2>History</h2>

          <table
            style={{
              width:"100%",
              marginTop:"20px",
              borderCollapse:"collapse"
            }}
          >

            <thead>

              <tr>

                <th>Date</th>

                <th>Module</th>

                <th>Status</th>

              </tr>

            </thead>

            <tbody>

              <tr>

                <td>01-Jul-2026</td>

                <td>Settlement Prediction</td>

                <td>Completed</td>

              </tr>

              <tr>

                <td>02-Jul-2026</td>

                <td>Negotiation Email</td>

                <td>Generated</td>

              </tr>

              <tr>

                <td>03-Jul-2026</td>

                <td>Financial Health</td>

                <td>Analyzed</td>

              </tr>

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}

export default History;