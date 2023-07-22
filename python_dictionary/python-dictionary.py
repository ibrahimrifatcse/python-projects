import difflib
import random
import colorama
colorama.init()

# Step 1: Create a Python dictionary with word data
# You can add more words and definitions to this dictionary
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

def get_word_info(word):
    word_data = all_about_python_data[word]
    print(colorama.Fore.BLUE + "Keyword name:" + colorama.Style.RESET_ALL, word)
    print(colorama.Fore.BLUE + "Definition:" + colorama.Style.RESET_ALL, word_data['definition'])
    print(colorama.Fore.GREEN + "Code:" + colorama.Style.RESET_ALL, word_data['code'])
    print(colorama.Fore.YELLOW + "Output:" + colorama.Style.RESET_ALL, word_data['output'])

def search_word():
    while True:
        user_input = input(colorama.Fore.WHITE + colorama.Back.GREEN + "Enter a word to search (or 'q' to quit): " + colorama.Style.RESET_ALL)
        if user_input == 'q':
            print("Exiting the program.")
            break

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
