from google import genai

key = "Provide your gemini API key here"
client = genai.Client(api_key=key)

chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("Hey, I am Jarvis\nHow may I help you ?")
while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chat.send_message(user)
    print("Jarvis:", response.text)
