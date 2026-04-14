# 🎵 Musician Community Demo App

def greet_user():
    print("\n--- Welcome to Musicians Community ---")
    
    time = input("Enter time (1=Morning, 2=Afternoon, 3=Evening): ")
    name = input("Enter your name: ")

    if time == "1":
        print(f"Good Morning {name}!")
    elif time == "2":
        print(f"Good Afternoon {name}!")
    elif time == "3":
        print(f"Good Evening {name}!")
    else:
        print(f"Hello {name}!")

    print("Welcome to our Musicians Community 🎶")

    status = input("What are you? (1=Producer, 2=Vocalist, 3=Guitarist, 4=Bassist, 5=Drummer): ")

    roles = {
        "1": "Producer",
        "2": "Vocalist",
        "3": "Guitarist",
        "4": "Bassist",
        "5": "Drummer"
    }

    if status in roles:
        print(f"🔥 {roles[status]} mode activated!")
    else:
        print("🔥 Musician mode activated!")

    return name


def create_profile():
    print("\n--- Create Your Profile ---")

    profile = {}
    profile["name"] = input("Name: ")
    profile["age"] = input("Age: ")
    profile["gender"] = input("Gender: ")
    profile["profession"] = input("Profession: ")
    profile["genre"] = input("Favorite Genre: ")
    profile["bio"] = input("Short Bio: ")
    profile["songs"] = input("Top songs (comma separated): ")
    profile["releases"] = input("Your releases: ")
    profile["artists"] = input("Favorite artists: ")

    print("\n🎤 PROFILE CREATED:")
    for key, value in profile.items():
        print(f"{key.capitalize()}: {value}")

    return profile


def start_jam():
    print("\n--- Start a Jam Session ---")
    
    print("Choose instrument needed:")
    print("1. Guitar")
    print("2. Drums")
    print("3. Keyboard")
    print("4. Bass")
    print("5. Vocals")

    choice = input("Enter choice: ")

    instruments = {
        "1": "Guitarist",
        "2": "Drummer",
        "3": "Keyboardist",
        "4": "Bassist",
        "5": "Vocalist"
    }

    if choice in instruments:
        print(f"🎯 Looking for a {instruments[choice]} near your location...")
        print("📍 (Demo) Matching musicians found!")
    else:
        print("Invalid choice.")


def message_musicians():
    print("\n--- Message Musicians ---")
    message = input("Type your message: ")
    print("📩 Message sent to nearby musicians!")
    print(f"Your message: {message}")


def main_menu():
    # user_name = greet_user()
    # profile = None

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Create Profile")
        print("2. Start Jam Session")
        print("3. Message Musicians")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            profile = create_profile()
        elif choice == "2":
            start_jam()
        elif choice == "3":
            message_musicians()
        elif choice == "4":
            print(f"Goodbye {user_name}! Keep creating 🎶")
            break
        else:
            print("Invalid choice. Try again.")


# Run App
# main_menu()