from groq import Groq

api-key = "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"

client = Groq(api_key = api-key)
chat_completion = client.chat.completions.create(
    {
        "role" : "system",
        "message": ""
    },
    {
        "role" : "user",
        "message": ""
    }
)