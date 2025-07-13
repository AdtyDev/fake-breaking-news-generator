import random

sub = ["Arjun","Jhanvi","Kajol","Modi","Srk"]
actions = ["loves","to be","rides horse","dances with", "eats"]
locations = ["at red fort", "mumbai local train","touring at banaras","at chaat bhandarr"]


while True:
    subject = random.choice(sub)
    action = random.choice(actions)
    location = random.choice(locations)

    headline = f"BREAKING NEWS : {subject} {action} {location}"
    print("\n"+ headline)

    user_input = input("\n Do you want another headline?").strip().lower()

    if user_input == "no":
        break

print("THank you")



