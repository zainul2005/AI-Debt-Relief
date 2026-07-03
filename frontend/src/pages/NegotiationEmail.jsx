import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import "../App.css";

function NegotiationEmail() {
  return (
    <div className="app">

      <Sidebar />

      <div className="main">

        <Navbar />

        <div className="profile">

          <h2>AI Negotiation Email</h2>

          <textarea
            rows="15"
            style={{
              width:"100%",
              background:"#1f2937",
              color:"white",
              border:"none",
              padding:"20px",
              borderRadius:"10px",
              marginTop:"20px"
            }}
            defaultValue={`Subject: Request for Loan Settlement

Dear Sir/Madam,

I am currently facing financial hardship and respectfully request a settlement on my outstanding loan.

I am committed to resolving my obligations and kindly request your consideration for a reduced settlement amount or EMI restructuring.

Thank you for your understanding.

Sincerely,
Borrower`}
          />

          <button
            style={{
              marginTop:"20px",
              padding:"12px 25px",
              background:"#2563eb",
              color:"white",
              border:"none",
              borderRadius:"8px"
            }}
          >
            Generate AI Email
          </button>

        </div>

      </div>

    </div>
  );
}

export default NegotiationEmail;