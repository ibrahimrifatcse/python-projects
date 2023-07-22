import difflib
import random
import colorama
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import pyperclip

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

# Function to copy code to clipboard
def copy_code_to_clipboard(code):
    pyperclip.copy(code)

def show_word_info(word):
    word_data = all_about_python_data[word]
    info_text.config(state=tk.NORMAL)
    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, f"Keyword name: {word}\n")
    info_text.insert(tk.END, f"Definition: {word_data['definition']}\n")
    info_text.insert(tk.END, f"Code:\n{word_data['code']}\n")
    info_text.insert(tk.END, f"Output: {word_data['output']}\n")
    info_text.config(state=tk.DISABLED)

def search_word():
    user_input = search_entry.get().lower()
    found_keywords = []
    for keyword, data in all_about_python_data.items():
        if user_input in keyword.lower():
            found_keywords.append(keyword)

    if not found_keywords:
        if len(user_input) < 3:
            recommended_words = get_similar_words(user_input, all_about_python_data.keys(), num_similar=5)
            if recommended_words:
                info_text.config(state=tk.NORMAL)
                info_text.delete(1.0, tk.END)
                info_text.insert(tk.END, "You are probably searching for this word!\n")
                for word in recommended_words:
                    info_text.insert(tk.END, f"- {word}\n")
                info_text.config(state=tk.DISABLED)
            else:
                info_text.config(state=tk.NORMAL)
                info_text.delete(1.0, tk.END)
                info_text.insert(tk.END, "No words found for this character in the dictionary.\n")
                info_text.config(state=tk.DISABLED)
        else:
            recommended_words = get_similar_words(user_input, all_about_python_data.keys(), num_similar=5)
            if recommended_words:
                info_text.config(state=tk.NORMAL)
                info_text.delete(1.0, tk.END)
                info_text.insert(tk.END, "You are probably searching for this word!\n")
                for word in recommended_words:
                    info_text.insert(tk.END, f"- {word}\n")
                info_text.config(state=tk.DISABLED)
            else:
                info_text.config(state=tk.NORMAL)
                info_text.delete(1.0, tk.END)
                info_text.insert(tk.END, "Keyword not found.\n")
                info_text.config(state=tk.DISABLED)
    else:
        if len(found_keywords) == 1:
            word = found_keywords[0]
            show_word_info(word)
        else:
            info_text.config(state=tk.NORMAL)
            info_text.delete(1.0, tk.END)
            info_text.insert(tk.END, "Possibly your searching answer:\n")
            for word in found_keywords:
                info_text.insert(tk.END, f"Keyword: {word}\nDefinition: {all_about_python_data[word]['definition']}\n")
                info_text.insert(tk.END, f"Code:\n{all_about_python_data[word]['code']}\n")
                info_text.insert(tk.END, f"Output: {all_about_python_data[word]['output']}\n\n")
            info_text.config(state=tk.DISABLED)


# Create the main application window
root = tk.Tk()
root.title("All About Python")
root.geometry("800x600")

# Frame to hold the search bar and buttons
frame_top = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame_top.pack(fill=tk.X)

# Search bar and search button
search_entry = tk.Entry(frame_top, font=("Arial", 14))
search_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

search_button = tk.Button(frame_top, text="Search", font=("Arial", 14), command=search_word)
search_button.pack(side=tk.LEFT, padx=10)

# Clear button
clear_button = tk.Button(frame_top, text="Clear", font=("Arial", 14), command=lambda: info_text.delete(1.0, tk.END))
clear_button.pack(side=tk.LEFT, padx=10)

# Exit button
exit_button = tk.Button(frame_top, text="Exit", font=("Arial", 14), command=root.quit)
exit_button.pack(side=tk.LEFT)

# ScrolledText widget to display information
info_text = scrolledtext.ScrolledText(root, font=("Arial", 12), wrap=tk.WORD, state=tk.DISABLED)
info_text.pack(fill=tk.BOTH, expand=True)

# Code Holder - Copy button
code_holder = tk.Frame(root, bg="black", padx=5, pady=5)
code_holder.pack(fill=tk.BOTH, expand=True)

copy_button = tk.Button(code_holder, text="Copy Code", font=("Arial", 14),
                        command=lambda: copy_code_to_clipboard(all_about_python_data[search_entry.get()]["code"]))
copy_button.pack(side=tk.LEFT)

# Start the main event loop
root.mainloop()
