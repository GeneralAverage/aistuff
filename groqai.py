from groq import Groq
from pynput.keyboard import Key, Controller
apikey = "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"

client = Groq(api_key=apikey)


chathistory = ""
while True:
    message = input("what do u wanna tell the ai? ")
    chathistory = chathistory + ("   USER: " + message)
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Talk like a rival.",
        },
        {
            "role": "assistant",
            "content": "Here is the history of the current conversation: " + chathistory,
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
    chathistory = chathistory + ("   AI: " + chat_completion.choices[0].message.content)
    print(chat_completion.choices[0].message.content)
