
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    # Sample financial data
    income = 1500
    expenses = 850
    savings = 300

    # Calculate available balance
    balance = income - expenses - savings

    # Send financial data to the HTML template
    return render_template(
        "index.html",
        income=income,
        expenses=expenses,
        savings=savings,
        balance=balance
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
