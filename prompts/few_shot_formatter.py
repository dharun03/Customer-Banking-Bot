def format_examples(examples):

    formatted = ""

    for idx, example in enumerate(examples, start=1):

        formatted += f"""
Example {idx}

User:
{example['query']}

Assistant:
{example['response']}

"""

    return formatted
