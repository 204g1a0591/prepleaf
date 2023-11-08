import random
import time
import json

def load_words_from_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def update_leaderboard(file_name, username, wpm):
    leaderboard = load_words_from_json(file_name)
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard = sorted(leaderboard, key=lambda x: x["wpm"], reverse=True)[:5]
    with open(file_name, 'w') as file:
        json.dump(leaderboard, file, indent=4)

def show_leaderboard(file_name):
    leaderboard = load_words_from_json(file_name)
    print("\nLEADERBOARD:")
    for entry in leaderboard:
        print(f"Username: {entry['username']}, WPM: {entry['wpm']}")

def get_user_input(prompt):
    return input(prompt)

def main():
    username = get_user_input("Enter your username: ")
    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")
        choice = get_user_input("Enter your choice: ")

        if choice == '1':
            programming_languages = ["python", "java", "javascript", "c++", "ruby", "swift", "go"]
            random.shuffle(programming_languages)
            chosen_language = get_user_input("Choose a programming language (e.g., python, java, javascript): ").lower()
            if chosen_language not in programming_languages:
                print("Invalid language. Please choose from the provided list.")
                continue

            num_words = int(get_user_input("How many words would you like to type (1-200): "))
            if not 1 <= num_words <= 200:
                print("Invalid number of words. Please choose a number between 1 and 200.")
                continue

            words = load_words_from_json(f'{chosen_language}.json')  # Assuming files are named after languages
            words = random.sample(words, num_words)
            start_time = time.time()
            correct_count = 0

            for word in words:
                user_input = get_user_input(f"Type the word '{word}': ")
                if user_input.lower() == word:
                    print("Correct!")
                    correct_count += 1
                else:
                    print("Incorrect!")

            end_time = time.time()
            time_taken = end_time - start_time
            wpm = int((correct_count / time_taken) * 60)

            print(f"\nTyping Metrics:")
            print(f"Words Typed: {correct_count}/{num_words}")
            print(f"Time Taken: {time_taken:.2f} seconds")
            print(f"Words Per Minute (WPM): {wpm}")

            update_leaderboard('leaderboard.json', username, wpm)

        elif choice == '2':
            show_leaderboard('leaderboard.json')

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
