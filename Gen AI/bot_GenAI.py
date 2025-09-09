import pyautogui
import pyperclip
import time
import google.generativeai as genai


genai.configure(api_key="")

# Gemini model select karo
model = genai.GenerativeModel("gemini-1.5-flash")


# Small delay so you can see actions
time.sleep(2)

def is_last_message_from_sender(chat_log, sender_name="Name"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

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



    # Prompt ko Roman Urdu Hadi style me answer karwana
    system_message = "You are a person named Hadi Hassan who speaks Roman Urdu as well as English. You are from Pakistan and you are a coder. You analyze chat history and roast people in a short and funny way. Output should be the next chat response as plain text only (without name, date, or time) and in just one line."


    # Model se response lena
    response = model.generate_content(
        system_message + "\nUser:\n" + copied_text
    )

    response = response.text
    pyperclip.copy(response)

    if is_last_message_from_sender(copied_text):    

        # Step 5 Click the target input area
        pyautogui.click(585, 690)
        time.sleep(0.15)

        # Step 6 Paste (Ctrl+V) aur phir Enter
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

        # Step 7 Press Enter
        pyautogui.press('enter')
