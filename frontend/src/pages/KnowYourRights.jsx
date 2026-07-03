import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../App.css";

function KnowYourRights() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main">

        <Navbar />

        <div className="profile">

          <h2>Know Your Rights</h2>

          <ul
            style={{
              color:"#cbd5e1",
              lineHeight:"2",
              marginTop:"20px"
            }}
          >

            <li>Borrowers have the right to receive fair treatment.</li>

            <li>Recovery agents cannot threaten or harass borrowers.</li>

            <li>You can negotiate loan settlements with lenders.</li>

            <li>You have the right to receive written settlement documents.</li>

            <li>Personal financial information must remain confidential.</li>

            <li>Borrowers can request loan restructuring when eligible.</li>

          </ul>

        </div>

      </div>

    </div>
  );
}

export default KnowYourRights;