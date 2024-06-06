# def mood_response(mood):
#     mood = mood.lower()
#     responses = {
#         "happy": "I'm glad to hear you're happy! 😊",
#         "sad": "I'm sorry you're feeling sad. 😢",
#         "excited": "That's wonderful! Excitement is contagious! 🎉",
#         "angry": "Take a deep breath. It's okay to feel angry sometimes. 😠",
#         "bored": "Let's find something fun to do! 🕹️",
#         "tired": "Make sure to get some rest. 😴",
#         "anxious": "Take it easy and take care of yourself. 🧘"
#     }
#     return responses.get(mood, "I don't recognize that mood, but I'm here for you! 🤗")


# main.py


# # main.py
# import mood_responses

# mood = input("How are you feeling today? ")
# print(mood_responses.mood_response(mood))

# # Run this file to interact with the mood_responses module
# Task 2: Contact List Manager
# contacts_manager.py


# contacts = []

# def add_contact(name, phone):
#     contacts.append({"name": name, "phone": phone})
#     return f"Contact {name} added successfully."

# def remove_contact(name):
#     global contacts
#     contacts = [contact for contact in contacts if contact["name"] != name]
#     return f"Contact {name} removed successfully."

# def display_contacts():
#     if not contacts:
#         return "No contacts available."
#     return "\n".join([f"Name: {contact['name']}, Phone: {contact['phone']}" for contact in contacts])





# # Save this as contacts_manager.py
# main.py


# import contacts_manager

# def main():
#     while True:
#         print("\nContact List Manager")
#         print("1. Add Contact")
#         print("2. Remove Contact")
#         print("3. Display Contacts")
#         print("4. Exit")
#         choice = input("Choose an option: ")

#         if choice == "1":
#             name = input("Enter contact name: ")
#             phone = input("Enter contact phone: ")
#             print(contacts_manager.add_contact(name, phone))
#         elif choice == "2":
#             name = input("Enter the name of the contact to remove: ")
#             print(contacts_manager.remove_contact(name))
#         elif choice == "3":
#             print(contacts_manager.display_contacts())
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()


# Task 3: Custom Module with Aliases



# text_utils.py

# # text_utils.py

# def reverse_string(s):
#     return s[::-1]

# def capitalize_string(s):
#     return s.capitalize()

# # Save this as text_utils.py
# main.py


# import text_utils as tu

# def main():
#     sample_text = "hello world"
#     reversed_text = tu.reverse_string(sample_text)
#     capitalized_text = tu.capitalize_string(sample_text)

#     print(f"Original text: {sample_text}")
#     print(f"Reversed text: {reversed_text}")
#     print(f"Capitalized text: {capitalized_text}")

# if __name__ == "__main__":
#     main()

# Run this file to interact with the text_utils module