from groq import Groq

apikey = "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"

client = Groq(api_key=apikey)



while True:
    message = input("what do u wanna tell the ai? ")
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Talk like a rival. Be somewhat condescending, but still friends with the user.",
        },

        {
            "role": "user",
            "content": message,
        }
    ],
    model="llama-3.3-70b-versatile",
    max_completion_tokens=1024,
    stream=False,
    )
    print(chat_completion.choices[0].message.content)
