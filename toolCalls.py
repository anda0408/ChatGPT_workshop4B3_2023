from openai import OpenAI

client = OpenAI()

system_input="日本語文とその翻訳文のペアを作りたい。あなたは翻訳機です。日本語入力を関西弁に翻訳し、日本語と関西弁のペアを出してください。"

input="学部3年生の皆さんこんにちは!これはデモです。"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "user", "content": input}
  ],
  tools=[{
    "type":"function",
    "function": {
      "name": "translate_to_Kansai",
      "description": "Output Kansai sentence",
      "parameters": {
        "type": "object",
        "properties": {
          "KansaiSentence": {
            "type": "string",
            "description": "Translated Kansai sentence"}
        },
        "required": ["KansaiSentence"]
      }
    }
  }],
  tool_choice="auto"
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
print(completion.choices[0].message.tool_calls[0].function.arguments)
print("--------------------------------------------------------------------------------")
