from classes import TextAnalyzer, Stack, Queue

def display_menu():
    """Displays the menu options"""
    print(
        """===== Text Analysis Tool ========== 
    Choose one of these options:
    1) Character Analysis
    2) Word Analysis
    3) Reversed String (Stack)
    4) FIFO Order (Queue)
    5) Word Count
    6) Exit
    """
    )

def get_valid_option():
    """Validates the user input for menu option"""
    while True:
        option = input("\n Your Option: ").strip()
        if option.isdigit() and 1 <= int(option) <= 6:
            return option
        print("Please enter a valid number between 1 and 6.")

def handle_option(option, text):
    """Handles the selected option and calls the appropriate functionality"""
    try:
        if option == "1":
            analyzer = TextAnalyzer(text)
            print("\nCharacter Analysis:")
            print(analyzer.character_analysis())
        elif option == "2":
            analyzer = TextAnalyzer(text)
            print("\nWord Analysis:")
            print(analyzer.word_analysis())
        elif option == "3":
            stack = Stack()
            print("\nReversed String (Stack):")
            print(stack.reverse_text(text))
        elif option == "4":
            queue = Queue()
            print("\nFIFO Order (Queue):")
            print(queue.reverse_word(text))
        elif option == "5":
            analyzer = TextAnalyzer(text)
            print("\nWord Count:")
            print(analyzer.word_count())
        else:
            print("Please enter a valid number between 1 and 6.")
    except Exception as e:
        print(f"An error occurred: {e}. Please check your input and try again.")

def main():
    """Main Function to run the text analysis tool"""
    display_menu()
    while True:
        num = get_valid_option()
        if num == '6':
            print("Exiting the program. Goodbye!")
            break
        sample_text = input("Write your text here: ").strip()
        if not sample_text:
            print("Input text cannot be empty. Please try again.")
            display_menu()
            continue
        handle_option(num, sample_text)

if __name__ == "__main__":
    main()
