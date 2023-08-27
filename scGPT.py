# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:38:52 2023

@author: shara
"""

import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can adjust the engine based on your preference
        prompt=prompt,
        max_tokens=50  # You can adjust the response length
    )
    return response.choices[0].text.strip()

print("ChatGPT: Hello! I'm SONU your chatbot. How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatGPT: Goodbye!")
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
