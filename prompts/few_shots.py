FEW_SHOT_EXAMPLES = [
    {
        "query": "I’ve been charged twice for the same transaction!",
        "response": """
I understand how frustrating duplicate charges can be.

I’ve raised a P2 dispute (Ticket #DC-4412)
for the duplicate debit of ₹2,340 on 12-Jan.

Your refund will be processed within
5 working days.
""",
    },
    {
        "query": """
Your bank is terrible.
I’ve been waiting 3 weeks for my new card.
""",
        "response": """
I sincerely apologize for the delay.

Sentiment: HIGH FRUSTRATION detected —
escalating to a senior agent.

Meanwhile, I’ve expedited your card dispatch
(new ETA: 2 business days)
and added a ₹200 inconvenience credit.
""",
    },
    {
        "query": "Can you check my account balance?",
        "response": """
Sure!

Your savings account ending 4421
has a balance of ₹1,23,456.78 as of today.

Would you like a mini-statement
or to set up a balance alert?
""",
    },
    {
        "query": "What is the home loan interest rate currently?",
        "response": """
Our current home loan interest rates start from 8.35% per annum,
depending on your credit profile and loan tenure.

Would you like me to help estimate your EMI as well?
""",
    },
    {
        "query": "I lost my debit card yesterday.",
        "response": """
I’m sorry to hear that.

For your security, I recommend immediately blocking the debit card.

I’ve initiated a card-block request and raised a priority support ticket.
A replacement card can be issued within 5–7 business days.
""",
    },
    {
        "query": "How can I complete my KYC process?",
        "response": """
You can complete your KYC by submitting:

- Aadhaar Card
- PAN Card
- Passport-size photograph
- Address proof

You may complete the process either online through video KYC
or by visiting the nearest branch.
""",
    },
    {
        "query": "Convert 500 USD to INR.",
        "response": """
Based on the current exchange rate,
500 USD is approximately ₹41,600 INR.

Please note that final rates may vary slightly
depending on forex charges and processing fees.
""",
    },
    {
        "query": "Nobody is responding to my fraud complaint.",
        "response": """
I sincerely apologize for the inconvenience.

Your complaint indicates possible fraud-related activity
and high customer frustration.

I’ve escalated this as a P1 priority case
to our fraud resolution team for immediate review.
""",
    },
    {
        "query": "Calculate EMI for a 20 lakh loan at 9% for 15 years.",
        "response": """
For a loan amount of ₹20,00,000
at an interest rate of 9% for 15 years,

your estimated monthly EMI would be approximately ₹20,285.

Would you also like to see the total interest payable?
""",
    },
    {
        "query": "My salary account has not been credited yet.",
        "response": """
I understand your concern.

Salary credit delays may occur due to processing timelines
from the employer’s bank.

I recommend waiting until end-of-day today.
If the issue persists, I can raise a service request for investigation.
""",
    },
    {
        "query": "How do I apply for a personal loan?",
        "response": """
You can apply for a personal loan through:

- Mobile banking app
- Net banking portal
- Nearest branch

Typical required documents include:
- PAN card
- Aadhaar card
- salary slips
- bank statements

Loan approval is generally completed within 24–48 hours.
""",
    },
    {
        "query": "There is an unauthorized transaction on my credit card.",
        "response": """
I’m sorry to hear about the unauthorized transaction.

I’ve flagged this as a high-priority fraud-related complaint
and initiated temporary card blocking for your protection.

A fraud investigation ticket has been created
and our security team will contact you shortly.
""",
    },
    {
        "query": "Can you help me open a fixed deposit account?",
        "response": """
Certainly!

You can open a fixed deposit account
through mobile banking, internet banking,
or by visiting a branch.

Current FD interest rates range between 6.5% and 7.25%
depending on tenure and customer category.
""",
    },
]
