from openai import OpenAI

client = OpenAI()

system_input="入力する内容について、間違った対応をしてください"
user_input="こんにちは!自己紹介してください。"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": system_input},
    {"role": "user", "content": user_input}
  ]
)
print()
print("Input --------------------------------------------------------------------------")
print(input)
print("--------------------------------------------------------------------------------")
print()
print("Output -------------------------------------------------------------------------")
print(completion)
print("--------------------------------------------------------------------------------")
print()
print("Reply --------------------------------------------------------------------------")
print(completion.choices[0].message.content)
print("--------------------------------------------------------------------------------")
