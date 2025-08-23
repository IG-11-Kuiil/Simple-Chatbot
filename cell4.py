print("Chatbot ready! Type 'exit' to quit.\n")
while True:
    u = input("You: ")
    if u.lower().strip() == "exit":
        break
    history.append("User: " + u)
    p = "\n".join(history + ["Bot:"])
    r = client.models.generate_content(model=MODEL, contents=p)
    b = r.text.strip()
    print("Bot:", b, "\n")
    history.append("Bot: " + b)
