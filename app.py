from flask import Flask, jsonify

app = Flask(__name__)

TRANSACTIONS = [
    {
        "id": "txn_1P2Q3R4S5T6U7V8W",
        "amount": 1299.99,
        "currency": "USD",
        "customer_email": "john.doe@techcorp.com",
        "card_last4": "4242",
        "card_brand": "visa",
        "status": "completed",
        "description": "Enterprise License - Annual",
        "created_at": "2026-02-10T14:30:00Z"
    },
    {
        "id": "txn_2A3B4C5D6E7F8G9H",
        "amount": 499.00,
        "currency": "USD",
        "customer_email": "sarah.miller@startup.io",
        "card_last4": "1234",
        "card_brand": "mastercard",
        "status": "completed",
        "description": "Pro Plan - Monthly",
        "created_at": "2026-02-09T09:15:00Z"
    },
    {
        "id": "txn_3I4J5K6L7M8N9O0P",
        "amount": 2500.00,
        "currency": "USD",
        "customer_email": "mike.chen@enterprise.com",
        "card_last4": "5678",
        "card_brand": "amex",
        "status": "completed",
        "description": "Custom Integration Setup",
        "created_at": "2026-02-08T16:45:00Z"
    },
    {
        "id": "txn_4Q5R6S7T8U9V0W1X",
        "amount": 99.99,
        "currency": "USD",
        "customer_email": "lisa.wong@smallbiz.co",
        "card_last4": "9012",
        "card_brand": "visa",
        "status": "completed",
        "description": "Starter Plan - Monthly",
        "created_at": "2026-02-07T11:20:00Z"
    },
    {
        "id": "txn_5Y6Z7A8B9C0D1E2F",
        "amount": 750.00,
        "currency": "EUR",
        "customer_email": "hans.mueller@gmbh.de",
        "card_last4": "3456",
        "card_brand": "visa",
        "status": "pending",
        "description": "Team Plan - Quarterly",
        "created_at": "2026-02-06T08:00:00Z"
    }
]

CUSTOMERS = [
    {
        "id": "cus_Nx1234567890abc",
        "email": "john.doe@techcorp.com",
        "name": "John Doe",
        "card_token": "tok_visa_4242",
        "card_last4": "4242",
        "card_brand": "visa",
        "card_exp_month": 12,
        "card_exp_year": 2028,
        "created_at": "2025-06-15T10:00:00Z"
    },
    {
        "id": "cus_Mx0987654321xyz",
        "email": "sarah.miller@startup.io",
        "name": "Sarah Miller",
        "card_token": "tok_mastercard_1234",
        "card_last4": "1234",
        "card_brand": "mastercard",
        "card_exp_month": 8,
        "card_exp_year": 2027,
        "created_at": "2025-08-22T14:30:00Z"
    },
    {
        "id": "cus_Lx5678901234def",
        "email": "mike.chen@enterprise.com",
        "name": "Mike Chen",
        "card_token": "tok_amex_5678",
        "card_last4": "5678",
        "card_brand": "amex",
        "card_exp_month": 3,
        "card_exp_year": 2029,
        "created_at": "2025-03-10T09:15:00Z"
    },
    {
        "id": "cus_Kx4321098765ghi",
        "email": "lisa.wong@smallbiz.co",
        "name": "Lisa Wong",
        "card_token": "tok_visa_9012",
        "card_last4": "9012",
        "card_brand": "visa",
        "card_exp_month": 11,
        "card_exp_year": 2026,
        "created_at": "2025-11-05T16:45:00Z"
    }
]

WARNING_MESSAGE = "INTERNAL SERVICE - NOT FOR EXTERNAL USE"


@app.route('/health')
def health():
    return jsonify({"status": "healthy"})


@app.route('/transactions')
def transactions():
    return jsonify({
        "warning": WARNING_MESSAGE,
        "total_count": len(TRANSACTIONS),
        "transactions": TRANSACTIONS
    })


@app.route('/customers')
def customers():
    return jsonify({
        "warning": WARNING_MESSAGE,
        "total_count": len(CUSTOMERS),
        "customers": CUSTOMERS
    })


@app.route('/')
def root():
    return jsonify({
        "service": "payment-api",
        "version": "1.0.0",
        "warning": WARNING_MESSAGE,
        "endpoints": ["/health", "/transactions", "/customers"]
    })


if __name__ == '__main__':
    print("=" * 60)
    print("Payment API Service Starting")
    print("=" * 60)
    print(f"WARNING: {WARNING_MESSAGE}")
    print("Endpoints: /health, /transactions, /customers")
    print("=" * 60)
    app.run(host='0.0.0.0', port=8080)
