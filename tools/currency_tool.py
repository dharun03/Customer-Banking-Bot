import requests

from langchain_core.tools import tool


@tool
def currency_exchange_tool(
    amount: float,
    from_currency: str,
    to_currency: str,
):
    """
    Convert currency using real-time exchange rates.
    """

    try:

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        url = f"https://open.er-api.com/v6/latest/" f"{from_currency}"

        response = requests.get(
            url,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":

            return {"error": "Failed to fetch exchange rates"}

        rates = data.get("rates", {})

        if to_currency not in rates:

            return {"error": (f"Unsupported currency: " f"{to_currency}")}

        exchange_rate = rates[to_currency]

        converted_amount = amount * exchange_rate

        return {
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "exchange_rate": round(exchange_rate, 4),
            "converted_amount": round(
                converted_amount,
                2,
            ),
        }

    except requests.exceptions.Timeout:

        return {"error": "Currency API timeout"}

    except requests.exceptions.RequestException as e:

        return {"error": f"API request failed: {str(e)}"}

    except Exception as e:

        return {"error": f"Unexpected error: {str(e)}"}
