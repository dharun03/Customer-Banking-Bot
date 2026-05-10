from langchain_core.tools import tool


@tool
def emi_calculator_tool(
    principal: float,
    annual_rate: float,
    tenure_years: int,
):
    """
    Calculate EMI for a loan.
    """

    monthly_rate = annual_rate / 12 / 100

    months = tenure_years * 12

    emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / (
        ((1 + monthly_rate) ** months) - 1
    )

    return {
        "principal": principal,
        "annual_rate": annual_rate,
        "tenure_years": tenure_years,
        "monthly_emi": round(emi, 2),
    }
