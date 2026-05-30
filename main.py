import datetime
import json

# Load tips and quotes from JSON
def load_data():
    with open("tips.json", "r") as f:
        return json.load(f)

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello {name}, welcome to Smart Student Assistant!")
    return name

def study_tips(data):
    tips = data["study_tips"]
    print("Study Tips:")
    for tip in tips:
        print("-", tip)
    return tips

def motivation_quote(data):
    quotes = data["quotes"]
    import random
    quote = random.choice(quotes)
    print("Motivation Quote:", quote)
    return quote

def current_datetime():
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date & Time:", dt)
    return dt

def save_output(content):
    with open("output.txt", "a") as f:
        f.write(content + "\n")

def main():
    data = load_data()
    name = greet_user()
    
    while True:
        print("\nMenu:")
        print("1. Generate Study Tips")
        print("2. Generate Motivation Quote")
        print("3. Display Current Date & Time")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            tips = study_tips(data)
            save_output("Study Tips: " + ", ".join(tips))
        elif choice == "2":
            quote = motivation_quote(data)
            save_output("Motivation Quote: " + quote)
        elif choice == "3":
            dt = current_datetime()
            save_output("Date & Time: " + dt)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
