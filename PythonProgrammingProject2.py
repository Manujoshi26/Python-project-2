def count_words(text):
    # Check if input is empty and handle the error case
    if not text.strip():
        return 0  # No words in empty or whitespace-only input
    
    # Split text by whitespace and count the resulting words
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter!")
    
    # Prompt the user for input
    user_input = input("Please enter a sentence or paragraph to count the words: ").strip()
    
    # Count words using the function
    word_count = count_words(user_input)
    
    # Display the result to the user
    if word_count == 0:
        print("No words entered. Please try again.")
    else:
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
