import pyautogui
import pyperclip
import time
from openai import OpenAI


client = OpenAI(
    api_key=""   
)


def is_last_message_from_sender(chat_log, sender_name="Name"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Small delay so you can see actions
time.sleep(2)

# Step 1: Click on Chrome icon at (455, 740)
pyautogui.click(455, 740)
time.sleep(2)  # wait for Chrome to open

while True:

    # Step 2: Drag from (495, 175) to (1325, 645)
    pyautogui.moveTo(495, 175)
    pyautogui.dragTo(1325, 645, duration=1, button='left')

    # Step 3: Copy selected text (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1320, 642)
    time.sleep(1)

    # Step 4: Get copied text from clipboard
    copied_text = pyperclip.paste()

    print("Copied Text:")
    print(copied_text)

    if is_last_message_from_sender(copied_text):    

        completions = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are a person named Hadi Hassan who speaks Roman Urdu as well as English. You are from Pakistan and you are a coder. You analyze chat history and roast people in a short and funny way. Output should be the next chat response as plain text only (without name, date, or time) and in just one line."},
                {"role": "user", "content": copied_text}
            ]
        )

        response =completions.choices[0].message.content
        pyperclip.copy(response)


        # Step 5 Click the target input area
        pyautogui.click(585, 690)
        time.sleep(0.15)

        # Step 6 Paste (Ctrl+V) aur phir Enter
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        # Step 7 Press Enter
        pyautogui.press('enter')
