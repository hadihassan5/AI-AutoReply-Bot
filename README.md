# 🤖 AI Chatbot Project

A lightweight AI chatbot that automates chat interactions. It captures a chat snippet from the screen, sends it to a language model, and pastes the AI-generated reply back into the chat.

This repository includes two independent implementations so you can choose between Google GenAI (Gemini) or OpenAI, depending on your preference.

# 🧩 Implementations

## Google GenAI (Gemini)

Script: Gen AI/bot_GenAI.py

Uses the google-generativeai client to generate responses.

## OpenAI

Script: Open AI/bot_OpenAI.py

Uses the openai client for response generation.

👉 Both implementations are standalone and can be run independently.

## 🛠 Supporting / Testing Scripts

client_genAI.py → Local tester for Google GenAI (without GUI automation).

client_openAI.py → Local tester for OpenAI (without GUI automation).

get_cursor.py → Prints mouse coordinates to configure automation click positions.

tempCodeRunnerFile.py → Temporary helper used during development.

## 📚 Libraries Used

pyautogui

pyperclip

google-generativeai

openai

time

## ▶ How to Run

Run your preferred implementation from the terminal:

## Run the Google GenAI bot
python bot_GenAI.py.py  

## Run the OpenAI bot
python bot_OpenAI.py


## Quick API testers (no GUI automation):

python client_genAI.py
python client_openAI.py


Make sure your API keys are properly configured in the environment or inside the scripts.

# ⚠️ Notes

Automation relies on fixed screen coordinates (see get_cursor.py) and the system clipboard for copy/paste.

Both implementations are independent — simply run the script for the provider you want to use.
