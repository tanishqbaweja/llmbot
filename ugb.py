from openrouter import OpenRouter

with OpenRouter(
  api_key="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",
) as client:
  response = client.chat.send(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    messages=[
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  )

  print(response.choices[0].message.content)
