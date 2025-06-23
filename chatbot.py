print("Hello, I am your friendly chatbot")
name=input("What's your name  ")
print(f"\n Nice meeting you {name}!! ")
feelings=input("How are you feeling today \n")
if "good" in feelings.lower() or "great" in feelings.lower() or "amazing" in feelings.lower():
    print("I am glad to hear that\n")
else:
    print("I hope your day gets better")
hobby=input("What's your favourite hobby?")
print(f"\n wow, {hobby} sounds fun")