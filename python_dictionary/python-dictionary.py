import difflib
import random
import colorama
colorama.init()

# Step 1: Create a Python dictionary with word data
# You can add more words and definitions to this dictionary.
# If you enter "**add", you will go to the data add option. When you give input for word, definition, and code, you should add "###" after the code.
# Here's an example:
'''
-----------------------------------------------------------
⏩ Enter a word to search (or 'q' to quit): **add  ⏮🟢
-----------------------------------------------------------
                ⬇
-----------------------------------------------------------                
⏩ Enter the new word: if Statements 
-----------------------------------------------------------
                 ⬇
-----------------------------------------------------------                 
⏩ Enter the definition: Perhaps the most well-known statement type is the if statement.
-----------------------------------------------------------
                ⬇
-----------------------------------------------------------
⏩ Enter the code (end the code input with a line containing only '###'): >>> x = int(input("Please enter an integer: "))
-----------------------------------------------------------
                ⬇
-----------------------------------------------------------                
⏩⏩Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More'
### ❌    ⏩ three # for ending code 🔚 you have to use three # after paste/input code
-----------------------------------------------------------
⏩ Enter the output: More
-----------------------------------------------------------
✅ The word 'if Statements' has been added.
-----------------------------------------------------------
'''

all_about_python_data = {
    "abs(x)": {
        "definition": "Return the absolute value of a number.",
        "code": colorama.Fore.GREEN + "abs(x)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "The output will be the absolute value of the number." + colorama.Style.RESET_ALL
    },
    "aiter(async_iterable)": {
        "definition": "Return an asynchronous iterator for an asynchronous iterable.",
        "code": colorama.Fore.GREEN + "aiter(async_iterable)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will return an asynchronous iterator." + colorama.Style.RESET_ALL
    },
    "all(iterable)": {
        "definition": "Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:",
        "code": colorama.Fore.GREEN + """
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will return True if all elements are true or False if the iterable is empty." + colorama.Style.RESET_ALL
    },
    "anext(async_iterator)": {
        "definition": "When awaited, return the next item from the given asynchronous iterator, or default if given and the iterator is exhausted.\n\nThis is the async variant of the next() builtin, and behaves similarly.\n\nThis calls the __anext__() method of async_iterator, returning an awaitable. Awaiting this returns the next value of the iterator. If default is given, it is returned if the iterator is exhausted, otherwise StopAsyncIteration is raised.\n\nNew in version 3.10.",
        "code": colorama.Fore.GREEN + "awaitable anext(async_iterator)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the next item from the given asynchronous iterator." + colorama.Style.RESET_ALL
    },
    "anext(async_iterator, default)": {
        "definition": "When awaited, return the next item from the given asynchronous iterator, or default if given and the iterator is exhausted.\n\nThis is the async variant of the next() builtin, and behaves similarly.\n\nThis calls the __anext__() method of async_iterator, returning an awaitable. Awaiting this returns the next value of the iterator. If default is given, it is returned if the iterator is exhausted, otherwise StopAsyncIteration is raised.\n\nNew in version 3.10.",
        "code": colorama.Fore.GREEN + "awaitable anext(async_iterator, default)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the next item from the given asynchronous iterator, or the default value if the iterator is exhausted." + colorama.Style.RESET_ALL
    },
    "any(iterable)": {
        "definition": "Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:",
        "code": colorama.Fore.GREEN + """
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will return True if any element in the iterable is true, or False if the iterable is empty." + colorama.Style.RESET_ALL
    },
}





# Step 2: Implement the main loop
# Function to find similar words using fuzzy matching

def get_similar_words(input_word, words_list, num_similar=5):
    return difflib.get_close_matches(input_word, [word for word in words_list], n=num_similar, cutoff=0.01)

def search_word():
    while True:
        user_input = input(colorama.Fore.WHITE + colorama.Back.GREEN + "Enter a word to search (or 'q' to quit): " + colorama.Style.RESET_ALL)
        if user_input == 'q':
            print("Exiting the program.")
            break

        if user_input == '**add':
            # Switch to add mode
            while True:
                new_word = input("Enter the new word: ")
                if new_word in all_about_python_data:
                    print("The word already exists. Please enter a new word.")
                else:
                    new_definition = input("Enter the definition: ")
                    new_code = input("Enter the code (end the code input with a line containing only '###'): ")
                    code_lines = []
                    while True:
                        code_line = input()
                        if code_line.strip() == "###":
                            break
                        code_lines.append(code_line)
                    new_code = "\n".join(code_lines)
                    new_output = input("Enter the output: ")
                    all_about_python_data[new_word] = {
                        "definition": new_definition,
                        "code": colorama.Fore.GREEN + new_code + colorama.Style.RESET_ALL,
                        "output": colorama.Fore.YELLOW + new_output + colorama.Style.RESET_ALL
                    }
                    print(f"The word '{new_word}' has been added.")
                    break
        elif user_input == '**move':
            # Switch to search mode
            continue
        else:
            found_keywords = []
            for keyword, data in all_about_python_data.items():
                if user_input.lower() in keyword.lower():
                    found_keywords.append(keyword)


        if not found_keywords:
            if len(user_input) < 3:
                recommended_words = get_similar_words(user_input, all_about_python_data.keys(), num_similar=5)
                if recommended_words:
                    print(colorama.Fore.GREEN + "You are probably searching for this word!" + colorama.Style.RESET_ALL)
                    print(colorama.Fore.YELLOW + "Recommended similar words:" + colorama.Style.RESET_ALL)
                    for word in recommended_words:
                        print("- " + word)
                else:
                    print(colorama.Fore.RED + "No words found for this character in the dictionary." + colorama.Style.RESET_ALL)
            else:
                recommended_words = get_similar_words(user_input, all_about_python_data.keys(), num_similar=5)
                if recommended_words:
                    print(colorama.Fore.GREEN + "You are probably searching for this word!" + colorama.Style.RESET_ALL)
                    print(colorama.Fore.YELLOW + "Recommended similar words:" + colorama.Style.RESET_ALL)
                    for word in recommended_words:
                        print("- " + word)
                else:
                    print(colorama.Fore.RED + "Keyword not found." + colorama.Style.RESET_ALL)
        else:
            if len(found_keywords) == 1:
                word = found_keywords[0]
                word_data = all_about_python_data[word]
                print(colorama.Fore.BLUE + "Keyword name:" + colorama.Style.RESET_ALL, word)
                print(colorama.Fore.BLUE + "Definition:" + colorama.Style.RESET_ALL, word_data['definition'])
                print(colorama.Fore.GREEN + "Code:" + colorama.Style.RESET_ALL, word_data['code'])
                print(colorama.Fore.YELLOW + "Output:" + colorama.Style.RESET_ALL, word_data['output'])

                recommended_words = get_similar_words(word, all_about_python_data.keys(), num_similar=5)
                if word in recommended_words:
                    print(colorama.Fore.GREEN + "You are probably searching for this word!" + colorama.Style.RESET_ALL)
                print(colorama.Fore.YELLOW + "Recommended similar words:" + colorama.Style.RESET_ALL)
                for recommended_word in recommended_words:
                    print("- " + recommended_word)

                selected_word = input("Enter a recommended word to see its definition (or press Enter to continue): ").lower()
                if selected_word in all_about_python_data:
                    word_data = all_about_python_data[selected_word]
                    print(colorama.Fore.BLUE + f"Definition of {selected_word}:" + colorama.Style.RESET_ALL, word_data['definition'])
            else:
                print(colorama.Fore.YELLOW + "Possibly your searching answer:" + colorama.Style.RESET_ALL)
                for word in found_keywords:
                    print(f"Keyword: {word}\nDefinition: {all_about_python_data[word]['definition']}")
                    print(f"Code: {all_about_python_data[word]['code']}\nOutput: {all_about_python_data[word]['output']}\n")

if __name__ == "__main__":
    search_word()
