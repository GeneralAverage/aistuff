from groq import Groq
from pynput import keyboard
from pynput.keyboard import Controller, Key,KeyCode
from PIL import ImageGrab
import pyttsx3
import asyncio
import sys
import string
import base64
import os
import time
mykeyboard = Controller()

    

engine = pyttsx3.init()

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
class KeyWaiter:
    def __init__(self, target_key=None):
        self.loop = asyncio.get_event_loop()
        self.target_key = target_key
        self.pressed = asyncio.Event()

    def on_press(self, key):
        if self.target_key is None or key == self.target_key:
            print(f"Key {key} pressed. Continuing...")
            self.pressed.set()
            return False  

    async def wait_for_key(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            await self.loop.run_in_executor(None, listener.join)
        await self.pressed.wait() 

async def waitquit():
    key_waiter = KeyWaiter(target_key=Key.esc)
    print("Waiting for quit command")
    await key_waiter.wait_for_key()
    print("Done!")
    sys.exit()
def wait_for_key(target_key):
    def on_press(key):
        if key == target_key:
            print(f"{key} pressed. Exiting...")

            return False  # Stop listener

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()





apikey = "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"

client = Groq(api_key=apikey)


chathistory = ""

wait_for_key(KeyCode.from_char('q'))

while True:
    
    
    
    currentScreenshot = ImageGrab.grab()
    currentScreenshot.save("screenshot.png")
    temp = encode_image("screenshot.png")
    os.remove("screenshot.png")
    chat_completion = client.chat.completions.create(
    messages=[
            
        {
            "role": "user",
            "content": [
                {
                    "type":"text",
                    "text":"I.",
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/png;base64,{temp}",
                    },
                },
            ],
        },
    ],
    model="llama-3.2-11b-vision-preview",
    max_completion_tokens=1000,
    stream=False,
    )
    airesponse = chat_completion.choices[0].message.content
    print(airesponse)
    time.sleep(1)
    engine.say(chat_completion.choices[0].message.content)
    engine.runAndWait()
