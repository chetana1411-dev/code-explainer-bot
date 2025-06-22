import os
from openai import OpenAI

client = OpenAI(api_key="insert your api here")  # Replace with your key

def explain_code(code_snippet):
    system_prompt = "You are a programming expert who explains code in simple terms."
    user_prompt = f"Explain the following code in detail:\n\n{code_snippet}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    code = ""
    print(" Paste your code below (hit Enter twice to end input):")
    while True:
        line = input()
        if line.strip() == "":
            break
        code += line + "\n"

    explanation = explain_code(code)
    print("\n Code Explanation:\n")
    print(explanation)


