from langchain_core.tools import tool

MOCK_RATES = {
    "USD_INR": 83.2,
    "EUR_INR": 90.5,
    "GBP_INR": 105.7,
    "INR_USD": 0.012,
}


@tool
def currency_exchange_tool(
    amount: float,
    from_currency: str,
    to_currency: str,
):
    """
    Convert currency using mock exchange rates.
    """

    key = f"{from_currency.upper()}_{to_currency.upper()}"

    rate = MOCK_RATES.get(key)

    if not rate:
        return {"error": "Unsupported currency pair"}
    converted_amount = amount * rate

    return {
        "amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "exchange_rate": rate,
        "converted_amount": round(converted_amount, 2),
    }
