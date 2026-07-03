import "./LoanTable.css";

function LoanTable() {
  return (
    <div className="table-container">

      <table className="loan-table">

        <thead>

          <tr>
            <th>Lender</th>
            <th>Loan Type</th>
            <th>Outstanding</th>
            <th>Interest</th>
            <th>EMI</th>
            <th>Overdue</th>
            <th>Priority</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>HDFC Bank</td>
            <td>Personal Loan</td>
            <td>₹5,00,000</td>
            <td>10%</td>
            <td>₹18,000</td>
            <td>0 Months</td>
            <td>
              <span className="medium">
                Medium
              </span>
            </td>

            <td>
              <button className="view-btn">
                View
              </button>
            </td>
          </tr>

          <tr>
            <td>SBI</td>
            <td>Credit Card</td>
            <td>₹1,20,000</td>
            <td>18%</td>
            <td>₹6,000</td>
            <td>2 Months</td>

            <td>
              <span className="high">
                High
              </span>
            </td>

            <td>
              <button className="view-btn">
                View
              </button>
            </td>
          </tr>

          <tr>
            <td>Axis Bank</td>
            <td>Home Loan</td>
            <td>₹18,50,000</td>
            <td>8.5%</td>
            <td>₹21,500</td>
            <td>0 Months</td>

            <td>
              <span className="low">
                Low
              </span>
            </td>

            <td>
              <button className="view-btn">
                View
              </button>
            </td>

          </tr>

        </tbody>

      </table>

    </div>
  );
}

export default LoanTable;