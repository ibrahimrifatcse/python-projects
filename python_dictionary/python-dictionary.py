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
    "anext(async_iterator)": {
        "definition": "When awaited, return the next item from the given asynchronous iterator, or default if given and the iterator is exhausted.\n\nThis is the async variant of the next() builtin, and behaves similarly.\n\nThis calls the __anext__() method of async_iterator, returning an awaitable. Awaiting this returns the next value of the iterator. If default is given, it is returned if the iterator is exhausted, otherwise StopAsyncIteration is raised.\n\nNew in version 3.10.",
        "code": colorama.Fore.GREEN + "awaitable anext(async_iterator)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the next item from the given asynchronous iterator." + colorama.Style.RESET_ALL
    },
    "ascii(object)": {
        "definition": "As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \\x, \\u, or \\U escapes.",
        "code": colorama.Fore.GREEN + "ascii(object)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a string containing a printable representation of the object with non-ASCII characters escaped." + colorama.Style.RESET_ALL
    },
    "bin(x)": {
        "definition": "Convert an integer number to a binary string prefixed with “0b”.",
        "code": colorama.Fore.GREEN + "bin(x)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a binary string representation of the integer number." + colorama.Style.RESET_ALL
    },
    "bool(x)": {
        "definition": "Convert a value to a Boolean, using the standard truth testing procedure.",
        "code": colorama.Fore.GREEN + "bool(x)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns True if the value is true, False otherwise." + colorama.Style.RESET_ALL
    },
    "breakpoint(*args, **kws)": {
        "definition": "This function drops you into the debugger at the call site.",
        "code": colorama.Fore.GREEN + "breakpoint(*args, **kws)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "When called, this function opens the debugger at the call site." + colorama.Style.RESET_ALL
    },
    "bytearray(iterable_of_ints)": {
        "definition": "Return a bytearray object.",
        "code": colorama.Fore.GREEN + "bytearray(iterable_of_ints)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new bytearray object initialized from the given iterable of integers." + colorama.Style.RESET_ALL
    },
    "bytes(iterable_of_ints)": {
        "definition": "Return a bytes object.",
        "code": colorama.Fore.GREEN + "bytes(iterable_of_ints)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new bytes object initialized from the given iterable of integers." + colorama.Style.RESET_ALL
    },
    "callable(object)": {
        "definition": "Return True if the object appears callable, False otherwise.",
        "code": colorama.Fore.GREEN + "callable(object)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns True if the object can be called (e.g., functions, classes, instances), False otherwise." + colorama.Style.RESET_ALL
    },
    "chr(i)": {
        "definition": "Return the string representing a character whose Unicode code point is the integer i.",
        "code": colorama.Fore.GREEN + "chr(i)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a string representing the character with the given Unicode code point." + colorama.Style.RESET_ALL
    },
    "classmethod(function)": {
        "definition": "Return a class method for function.",
        "code": colorama.Fore.GREEN + """
class C:
    @classmethod
    def f(cls, arg1, arg2, ...):
        ...
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a class method object that can be called on the class." + colorama.Style.RESET_ALL
    },
    "compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)": {
        "definition": "Compile the source into a code or AST object.",
        "code": colorama.Fore.GREEN + "compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a code object or an abstract syntax tree (AST) object." + colorama.Style.RESET_ALL
    },
    "complex(real, imag=0)": {
        "definition": "Create a complex number.",
        "code": colorama.Fore.GREEN + "complex(real, imag=0)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a complex number with the given real and imaginary parts." + colorama.Style.RESET_ALL
    },
    "delattr(object, name)": {
        "definition": "Delete a named attribute on an object.",
        "code": colorama.Fore.GREEN + "delattr(object, name)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Deletes the named attribute from the object." + colorama.Style.RESET_ALL
    },
    "dict()": {
        "definition": "Create a new dictionary.",
        "code": colorama.Fore.GREEN + "dict()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new empty dictionary." + colorama.Style.RESET_ALL
    },
    "dir([object])": {
        "definition": "Without arguments, return the list of names in the current local scope.\nWith an argument, attempt to return a list of valid attributes for that object.",
        "code": colorama.Fore.GREEN + "dir([object])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a list of names in the current local scope or valid attributes for the given object." + colorama.Style.RESET_ALL
    },
    "divmod(a, b)": {
        "definition": "Return the tuple (a//b, a%b).",
        "code": colorama.Fore.GREEN + "divmod(a, b)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the quotient and remainder when a is divided by b." + colorama.Style.RESET_ALL
    },
    "enumerate(iterable, start=0)": {
        "definition": "Return an enumerate object.",
        "code": colorama.Fore.GREEN + "enumerate(iterable, start=0)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns an enumerate object that generates pairs of (index, value) from the iterable." + colorama.Style.RESET_ALL
    },
    "eval(expression, globals=None, locals=None)": {
        "definition": "The arguments are a string and optional globals and locals. If provided, locals can be any mapping type.",
        "code": colorama.Fore.GREEN + "eval(expression, globals=None, locals=None)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Evaluates the expression in the given globals and locals contexts." + colorama.Style.RESET_ALL
    },
    "exec(object[, globals[, locals]])": {
        "definition": "This function supports dynamic execution of Python code.",
        "code": colorama.Fore.GREEN + "exec(object[, globals[, locals]])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Executes Python code dynamically." + colorama.Style.RESET_ALL
    },
    "filter(function, iterable)": {
        "definition": "Construct an iterator from those elements of iterable for which function returns true.",
        "code": colorama.Fore.GREEN + """
def is_positive(x):
    return x > 0

numbers = [1, -2, 3, -4, 5]
filtered_numbers = filter(is_positive, numbers)
for num in filtered_numbers:
    print(num)
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Filters elements in the iterable based on the function's output." + colorama.Style.RESET_ALL
    },
    "float(x)": {
        "definition": "Convert a number or a string containing a number to a floating-point number.",
        "code": colorama.Fore.GREEN + "float(x)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Converts the input to a floating-point number." + colorama.Style.RESET_ALL
    },
    "format(value[, format_spec])": {
        "definition": "Convert a value to a “formatted” version of a string.",
        "code": colorama.Fore.GREEN + "format(value[, format_spec])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Formats the value as a string using the format_spec (optional)." + colorama.Style.RESET_ALL
    },
    "frozenset([iterable])": {
        "definition": "Return a new frozenset object, optionally with elements taken from iterable.",
        "code": colorama.Fore.GREEN + "frozenset([iterable])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new frozenset object, optionally initialized from the iterable." + colorama.Style.RESET_ALL
    },
    "getattr(object, name[, default])": {
        "definition": "Return the value of the named attribute of object.",
        "code": colorama.Fore.GREEN + "getattr(object, name[, default])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the value of the named attribute of the object or the default value if the attribute is not found." + colorama.Style.RESET_ALL
    },
    "globals()": {
        "definition": "Return a dictionary representing the current global symbol table.",
        "code": colorama.Fore.GREEN + "globals()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a dictionary representing the current global symbol table." + colorama.Style.RESET_ALL
    },
    "hasattr(object, name)": {
        "definition": "The arguments are an object and a string.",
        "code": colorama.Fore.GREEN + "hasattr(object, name)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns True if the object has the named attribute, False otherwise." + colorama.Style.RESET_ALL
    },
    "hash(object)": {
        "definition": "Return the hash value of the object (if it has one).",
        "code": colorama.Fore.GREEN + "hash(object)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the hash value of the object if it's hashable." + colorama.Style.RESET_ALL
    },
    "help([object])": {
        "definition": "Invoke the built-in help system.",
        "code": colorama.Fore.GREEN + "help([object])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Invokes the built-in help system for the given object (if provided)." + colorama.Style.RESET_ALL
    },
    "hex(x)": {
        "definition": "Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.",
        "code": colorama.Fore.GREEN + "hex(x)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Converts the integer number to a lowercase hexadecimal string." + colorama.Style.RESET_ALL
    },
    "id(object)": {
        "definition": "Return the identity of an object.",
        "code": colorama.Fore.GREEN + "id(object)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a unique identifier for the object." + colorama.Style.RESET_ALL
    },
    "input([prompt])": {
        "definition": "If the prompt argument is present, it is written to standard output without a trailing newline.",
        "code": colorama.Fore.GREEN + "input([prompt])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Reads a line from input and returns it as a string." + colorama.Style.RESET_ALL
    },
    "int(x, base=10)": {
        "definition": "Return an integer object constructed from a number or a string.",
        "code": colorama.Fore.GREEN + "int(x, base=10)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns an integer object constructed from the input number or string." + colorama.Style.RESET_ALL
    },
    "isinstance(object, classinfo)": {
        "definition": "Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof.",
        "code": colorama.Fore.GREEN + "isinstance(object, classinfo)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns True if the object is an instance of the given class or its subclass." + colorama.Style.RESET_ALL
    },
    "issubclass(class, classinfo)": {
        "definition": "Return True if class is a subclass (direct, indirect, or virtual) of classinfo.",
        "code": colorama.Fore.GREEN + "issubclass(class, classinfo)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns True if class is a subclass of classinfo." + colorama.Style.RESET_ALL
    },
    "iter(object[, sentinel])": {
        "definition": "Return an iterator object.",
        "code": colorama.Fore.GREEN + "iter(object[, sentinel])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns an iterator object for the given object." + colorama.Style.RESET_ALL
    },
    "len(s)": {
        "definition": "Return the length (the number of items) of an object.",
        "code": colorama.Fore.GREEN + "len(s)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the number of items in the object." + colorama.Style.RESET_ALL
    },
    "list(iterable)": {
        "definition": "Return a list object.",
        "code": colorama.Fore.GREEN + "list(iterable)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new list initialized from the given iterable." + colorama.Style.RESET_ALL
    },
    "locals()": {
        "definition": "Update and return a dictionary representing the current local symbol table.",
        "code": colorama.Fore.GREEN + "locals()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a dictionary representing the current local symbol table." + colorama.Style.RESET_ALL
    },
    "map(function, iterable, ...)": {
        "definition": "Return an iterator that applies function to every item of iterable, yielding the results.",
        "code": colorama.Fore.GREEN + """
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
for num in squared_numbers:
    print(num)
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Applies the function to every item in the iterable and yields the results." + colorama.Style.RESET_ALL
    },
    "max(iterable, *[, key, default])": {
        "definition": "With a single iterable argument, return its biggest item.",
        "code": colorama.Fore.GREEN + "max(iterable, *[, key, default])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the largest item in the iterable or the maximum of two or more arguments." + colorama.Style.RESET_ALL
    },
    "memoryview(obj)": {
        "definition": "Return a memory view object of the given argument.",
        "code": colorama.Fore.GREEN + "memoryview(obj)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a memory view object of the given argument." + colorama.Style.RESET_ALL
    },
    "min(iterable, *[, key, default])": {
        "definition": "With a single iterable argument, return its smallest item.",
        "code": colorama.Fore.GREEN + "min(iterable, *[, key, default])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the smallest item in the iterable or the minimum of two or more arguments." + colorama.Style.RESET_ALL
    },
    "next(iterator, default)": {
        "definition": "Retrieve the next item from the iterator by calling its __next__() method.",
        "code": colorama.Fore.GREEN + "next(iterator, default)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the next item from the iterator or the default value if the iterator is exhausted." + colorama.Style.RESET_ALL
    },
    "object()": {
        "definition": "Return a new featureless object.",
        "code": colorama.Fore.GREEN + "object()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new featureless object (base for all classes)." + colorama.Style.RESET_ALL
    },
    "oct(x)": {
        "definition": "Convert an integer number to an octal string prefixed with “0o”.",
        "code": colorama.Fore.GREEN + "oct(x)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Converts the integer number to an octal string." + colorama.Style.RESET_ALL
    },
    "open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)": {
        "definition": "Open file and return a corresponding file object.",
        "code": colorama.Fore.GREEN + "open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Opens the file and returns a file object." + colorama.Style.RESET_ALL
    },
    "ord(c)": {
        "definition": "Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.",
        "code": colorama.Fore.GREEN + "ord(c)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns an integer representing the Unicode code point of the given character." + colorama.Style.RESET_ALL
    },
    "pow(x, y[, z])": {
        "definition": "Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z).",
        "code": colorama.Fore.GREEN + "pow(x, y[, z])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns x raised to the power y, optionally modulo z." + colorama.Style.RESET_ALL
    },
    "print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)": {
        "definition": "Print objects to the text stream file, separated by sep and followed by end.",
        "code": colorama.Fore.GREEN + "print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Prints objects to the text stream file with optional custom separator, end, and file." + colorama.Style.RESET_ALL
    },
    "property([fget[, fset[, fdel[, doc]]]])": {
        "definition": "Return a property attribute for new-style classes (classes that derive from object).",
        "code": colorama.Fore.GREEN + """
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a property attribute for getting, setting, and deleting the attribute." + colorama.Style.RESET_ALL
    },
    "range(stop)": {
        "definition": "Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.",
        "code": colorama.Fore.GREEN + "range(stop)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a sequence of integers from 0 to stop (exclusive)." + colorama.Style.RESET_ALL
    },
    "repr(object)": {
        "definition": "Return a string containing a printable representation of an object.",
        "code": colorama.Fore.GREEN + "repr(object)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a string representation of the object that can be used to recreate the object." + colorama.Style.RESET_ALL
    },
    "reversed(seq)": {
        "definition": "Return a reverse iterator.",
        "code": colorama.Fore.GREEN + "reversed(seq)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a reverse iterator for the given sequence." + colorama.Style.RESET_ALL
    },
    "round(number[, ndigits])": {
        "definition": "Return number rounded to ndigits precision after the decimal point.",
        "code": colorama.Fore.GREEN + "round(number[, ndigits])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Rounds the number to the specified precision after the decimal point." + colorama.Style.RESET_ALL
    },
    "set([iterable])": {
        "definition": "Return a new set object, optionally with elements taken from iterable.",
        "code": colorama.Fore.GREEN + "set([iterable])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new set object, optionally initialized from the iterable." + colorama.Style.RESET_ALL
    },
    "setattr(object, name, value)": {
        "definition": "This is the counterpart of getattr().",
        "code": colorama.Fore.GREEN + "setattr(object, name, value)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Sets the named attribute on the object to the given value." + colorama.Style.RESET_ALL
    },
    "slice(stop)": {
        "definition": "Return a slice object representing the set of indices specified by range(start, stop, step).",
        "code": colorama.Fore.GREEN + "slice(stop)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a slice object representing a sequence of indices from 0 to stop (exclusive)." + colorama.Style.RESET_ALL
    },
    "sorted(iterable, *, key=None, reverse=False)": {
        "definition": "Return a new sorted list from the items in iterable.",
        "code": colorama.Fore.GREEN + "sorted(iterable, *, key=None, reverse=False)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new sorted list from the items in the iterable, based on the optional key and reverse arguments." + colorama.Style.RESET_ALL
    },
    "staticmethod(function)": {
        "definition": "Return a static method for function.",
        "code": colorama.Fore.GREEN + """
class C:
    @staticmethod
    def f(arg1, arg2, ...):
        ...
""" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a static method object that can be called without an instance of the class." + colorama.Style.RESET_ALL
    },
    "str(object='')": {
        "definition": "Return a string version of object.",
        "code": colorama.Fore.GREEN + "str(object='')" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Converts the object to its string representation." + colorama.Style.RESET_ALL
    },
    "sum(iterable, start=0)": {
        "definition": "Sums start and the items of an iterable from left to right and returns the total.",
        "code": colorama.Fore.GREEN + "sum(iterable, start=0)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Sums the items of the iterable and the start value (optional) and returns the total." + colorama.Style.RESET_ALL
    },
    "super([type[, object-or-type]])": {
        "definition": "Return a temporary object of the superclass that is initialized with obj.",
        "code": colorama.Fore.GREEN + "super([type[, object-or-type]])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a temporary object of the superclass that is initialized with the given object." + colorama.Style.RESET_ALL
    },
    "tuple([iterable])": {
        "definition": "Build a tuple.",
        "code": colorama.Fore.GREEN + "tuple([iterable])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns a new tuple object, optionally initialized from the iterable." + colorama.Style.RESET_ALL
    },
    "type(object)": {
        "definition": "With one argument, return the type of an object.",
        "code": colorama.Fore.GREEN + "type(object)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the type of the object." + colorama.Style.RESET_ALL
    },
    "vars([object])": {
        "definition": "Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.",
        "code": colorama.Fore.GREEN + "vars([object])" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns the __dict__ attribute for the object (if available)." + colorama.Style.RESET_ALL
    },
    "zip(*iterables)": {
        "definition": "Make an iterator that aggregates elements from each of the iterables.",
        "code": colorama.Fore.GREEN + "zip(*iterables)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Returns an iterator that aggregates elements from each of the iterables." + colorama.Style.RESET_ALL
    },
    "_()": {
        "definition": "A special object such that the expression _(expr) is equivalent to expr.",
        "code": colorama.Fore.GREEN + "_()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "A special object that allows using it as a placeholder for an expression." + colorama.Style.RESET_ALL
    },
    "__import__(name, globals=None, locals=None, fromlist=(), level=0)": {
        "definition": "This function is invoked by the import statement.",
        "code": colorama.Fore.GREEN + "__import__(name, globals=None, locals=None, fromlist=(), level=0)" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "Imports a module dynamically." + colorama.Style.RESET_ALL
    },
    # Multithreading
"Multithreading": {
    "definition": "Multithreading is a concurrent execution model where multiple threads are executed by a single process.",
    "code": "import threading\n\ndef print_numbers():\n    for i in range(5):\n        print(i)\n\nthread1 = threading.Thread(target=print_numbers)\nthread2 = threading.Thread(target=print_numbers)\n\nthread1.start()\nthread2.start()\n\nthread1.join()\nthread2.join()",
    "output": "The output will be two sets of numbers printed concurrently."
},

# Multiprocessing
"Multiprocessing": {
    "definition": "Multiprocessing is a concurrent execution model where multiple processes are spawned to execute tasks.",
    "code": "import multiprocessing\n\ndef print_numbers():\n    for i in range(5):\n        print(i)\n\nprocess1 = multiprocessing.Process(target=print_numbers)\nprocess2 = multiprocessing.Process(target=print_numbers)\n\nprocess1.start()\nprocess2.start()\n\nprocess1.join()\nprocess2.join()",
    "output": "The output will be two sets of numbers printed concurrently using different processes."
},

# Exception Handling
"Exception Handling": {
    "definition": "Exception handling allows the program to handle errors or exceptional situations gracefully without crashing.",
    "code": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero.')\nelse:\n    print('Division successful:', result)\nfinally:\n    print('End of the program.')",
    "output": "The output will be 'Cannot divide by zero.' followed by 'End of the program.'"
},

# User-Defined Exception Handling
"User-Defined Exception Handling": {
    "definition": "Python allows you to create custom exception classes to handle specific types of errors in your application.",
    "code": "class CustomError(Exception):\n    def __init__(self, message):\n        self.message = message\n\ntry:\n    raise CustomError('This is a custom exception.')\nexcept CustomError as ce:\n    print('Custom Exception:', ce.message)",
    "output": "The output will be 'Custom Exception: This is a custom exception.'"
},
"Stack": {
    "definition": "A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.",
    "code": "class Stack:\n    def __init__(self):\n        self.items = []\n\n    def push(self, item):\n        self.items.append(item)\n\n    def pop(self):\n        if not self.is_empty():\n            return self.items.pop()\n\n    def peek(self):\n        if not self.is_empty():\n            return self.items[-1]\n\n    def is_empty(self):\n        return len(self.items) == 0\n\n    def size(self):\n        return len(self.items)",
    "output": "The Stack class allows you to push items onto the stack, pop items from the top, peek at the top item without removing it, check if the stack is empty, and get the size of the stack."
},
"Queue": {
    "definition": "A queue is a linear data structure that follows the First In, First Out (FIFO) principle.",
    "code": "from collections import deque\n\nclass Queue:\n    def __init__(self):\n        self.items = deque()\n\n    def enqueue(self, item):\n        self.items.append(item)\n\n    def dequeue(self):\n        if not self.is_empty():\n            return self.items.popleft()\n\n    def is_empty(self):\n        return len(self.items) == 0\n\n    def size(self):\n        return len(self.items)",
    "output": "The Queue class allows you to enqueue items at the rear, dequeue items from the front, check if the queue is empty, and get the size of the queue."
},
"Union-Find (Disjoint Set)": {
    "definition": "Union-Find is a data structure that efficiently keeps track of disjoint sets and supports merging them together.",
    "code": "class UnionFind:\n    def __init__(self, n):\n        self.parent = list(range(n))\n        self.rank = [0] * n\n\n    def find(self, x):\n        if self.parent[x] != x:\n            self.parent[x] = self.find(self.parent[x])\n        return self.parent[x]\n\n    def union(self, x, y):\n        root_x = self.find(x)\n        root_y = self.find(y)\n        if root_x != root_y:\n            if self.rank[root_x] > self.rank[root_y]:\n                self.parent[root_y] = root_x\n            elif self.rank[root_x] < self.rank[root_y]:\n                self.parent[root_x] = root_y\n            else:\n                self.parent[root_y] = root_x\n                self.rank[root_x] += 1",
    "output": "The UnionFind class allows you to efficiently find the representative of a set and merge two sets together."
},
"Linked List (Add, Delete, Search)": {
    "definition": "A linked list is a linear data structure consisting of nodes, where each node points to the next node in the sequence.",
    "code": "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\n\nclass LinkedList:\n    def __init__(self):\n        self.head = None\n\n    def add(self, data):\n        new_node = Node(data)\n        if self.head is None:\n            self.head = new_node\n        else:\n            current = self.head\n            while current.next:\n                current = current.next\n            current.next = new_node\n\n    def delete(self, key):\n        current = self.head\n        prev = None\n        while current:\n            if current.data == key:\n                if prev:\n                    prev.next = current.next\n                else:\n                    self.head = current.next\n                return\n            prev = current\n            current = current.next\n\n    def search(self, key):\n        current = self.head\n        while current:\n            if current.data == key:\n                return True\n            current = current.next\n        return False",
    "output": "The LinkedList class allows you to add elements to the end of the list, delete elements with a given value, and search for elements in the list."
},
"Quick Find (Dynamic Connectivity)": {
    "definition": "Quick Find is an algorithm used to solve the dynamic connectivity problem, where the goal is to connect two elements in a set.",
    "code": "class QuickFind:\n    def __init__(self, n):\n        self.n = n\n        self.id = list(range(n))\n\n    def connected(self, p, q):\n        return self.id[p] == self.id[q]\n\n    def union(self, p, q):\n        pid = self.id[p]\n        qid = self.id[q]\n        if pid != qid:\n            for i in range(self.n):\n                if self.id[i] == pid:\n                    self.id[i] = qid",
    "output": "The QuickFind class allows you to check if two elements are connected and merge two sets together efficiently."
},
"Quick Union (Dynamic Connectivity)": {
    "definition": "Quick Union is an algorithm used to solve the dynamic connectivity problem, where the goal is to connect two elements in a set.",
    "code": "class QuickUnion:\n    def __init__(self, n):\n        self.n = n\n        self.parent = list(range(n))\n\n    def root(self, i):\n        while i != self.parent[i]:\n            i = self.parent[i]\n        return i\n\n    def connected(self, p, q):\n        return self.root(p) == self.root(q)\n\n    def union(self, p, q):\n        i = self.root(p)\n        j = self.root(q)\n        self.parent[i] = j",
    "output": "The QuickUnion class allows you to check if two elements are connected and merge two sets together efficiently using tree structures."
},
"Generics": {
    "definition": "In Python, there is no explicit support for generics like in some other programming languages.",
    "code": "from typing import TypeVar\n\nT = TypeVar('T')\n\n\ndef swap(a: T, b: T) -> None:\n    a, b = b, a\n",
    "output": "The swap function is a generic function that takes two arguments of the same type and swaps their values."
},
"Iterators": {
    "definition": "Iterators allow you to iterate over a sequence of elements one by one.",
    "code": "class MyIterator:\n    def __init__(self, data):\n        self.data = data\n        self.index = 0\n\n    def __iter__(self):\n        return self\n\n    def __next__(self):\n        if self.index < len(self.data):\n            result = self.data[self.index]\n            self.index += 1\n            return result\n        else:\n            raise StopIteration\n\n\nmy_list = [1, 2, 3, 4, 5]\nmy_iterator = MyIterator(my_list)\n\nfor item in my_iterator:\n    print(item)",
    "output": "The MyIterator class allows you to create custom iterators to traverse elements in a sequence one by one."
},
"Stack Applications": {
    "definition": "Stacks have various applications, including function call management, expression evaluation, and undo/redo functionality.",
    "code": "",
    "output": "Stacks can be used to manage function calls, evaluate expressions, and implement undo/redo functionality in text editors and other applications."
},
"Queue Applications": {
    "definition": "Queues have various applications, including task scheduling, message passing, and print job management.",
    "code": "",
    "output": "Queues can be used to schedule tasks, pass messages between threads or processes, and manage print jobs in a print spooler."
},
"Sorting Algorithms (Selection Sort, Insertion Sort, Shell Sort)": {
    "definition": "Sorting algorithms arrange elements in a specific order, such as ascending or descending.",
    "code": "def selection_sort(arr):\n    for i in range(len(arr)):\n        min_index = i\n        for j in range(i + 1, len(arr)):\n            if arr[j] < arr[min_index]:\n                min_index = j\n        arr[i], arr[min_index] = arr[min_index], arr[i]\n\n\n\ndef insertion_sort(arr):\n    for i in range(1, len(arr)):\n        key = arr[i]\n        j = i - 1\n        while j >= 0 and key < arr[j]:\n            arr[j + 1] = arr[j]\n            j -= 1\n        arr[j + 1] = key\n\n\n\ndef shell_sort(arr):\n    gap = len(arr) // 2\n    while gap > 0:\n        for i in range(gap, len(arr)):\n            temp = arr[i]\n            j = i\n            while j >= gap and arr[j - gap] > temp:\n                arr[j] = arr[j - gap]\n                j -= gap\n            arr[j] = temp\n        gap //= 2",
    "output": "The functions selection_sort, insertion_sort, and shell_sort implement their respective sorting algorithms on a given list or array."
},
"Shuffling": {
    "definition": "Shuffling is the process of rearranging elements in a random order.",
    "code": "import random\n\nmy_list = [1, 2, 3, 4, 5]\nrandom.shuffle(my_list)\nprint(my_list)",
    "output": "The output will be the elements of the list randomly rearranged."
},
"Convex Hull (Graham Scan Algorithm)": {
    "definition": "The convex hull is the smallest convex polygon that encloses all given points in a set.",
    "code": "def orientation(p, q, r):\n    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])\n    if val == 0:\n        return 0\n    return 1 if val > 0 else 2\n\ndef convex_hull(points):\n    n = len(points)\n    if n < 3:\n        return points\n\n    points.sort(key=lambda x: (x[0], x[1]))\n\n    upper_hull = [points[0], points[1]]\n    for i in range(2, n):\n        while len(upper_hull) > 1 and orientation(upper_hull[-2], upper_hull[-1], points[i]) != 2:\n            upper_hull.pop()\n        upper_hull.append(points[i])\n\n    lower_hull = [points[-1], points[-2]]\n    for i in range(n - 3, -1, -1):\n        while len(lower_hull) > 1 and orientation(lower_hull[-2], lower_hull[-1], points[i]) != 2:\n            lower_hull.pop()\n        lower_hull.append(points[i])\n\n    return upper_hull + lower_hull[1:]",
    "output": "The convex_hull function takes a list of points as input and returns the convex hull of those points using the Graham Scan algorithm."
},

"Merge Sort": {
    "definition": "Merge Sort is a divide-and-conquer sorting algorithm that divides the input array into two halves, recursively sorts them, and then merges the two sorted halves.",
    "code": "def merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        left_half = arr[:mid]\n        right_half = arr[mid:]\n\n        merge_sort(left_half)\n        merge_sort(right_half)\n\n        i = j = k = 0\n        while i < len(left_half) and j < len(right_half):\n            if left_half[i] < right_half[j]:\n                arr[k] = left_half[i]\n                i += 1\n            else:\n                arr[k] = right_half[j]\n                j += 1\n            k += 1\n\n        while i < len(left_half):\n            arr[k] = left_half[i]\n            i += 1\n            k += 1\n\n        while j < len(right_half):\n            arr[k] = right_half[j]\n            j += 1\n            k += 1",
    "output": "The merge_sort function takes an unsorted list as input and returns the list sorted in ascending order using the Merge Sort algorithm."
},
"Bottom-Up Merge Sort": {
    "definition": "Bottom-Up Merge Sort is a variation of the Merge Sort algorithm that iteratively divides the input list into sublists and merges them.",
    "code": "def bottom_up_merge_sort(arr):\n    n = len(arr)\n    width = 1\n    while width < n:\n        for i in range(0, n, width * 2):\n            left = i\n            mid = min(i + width, n)\n            right = min(i + width * 2, n)\n            merged = sorted(arr[left:right])\n            arr[left:right] = merged\n        width *= 2",
    "output": "The bottom_up_merge_sort function takes an unsorted list as input and returns the list sorted in ascending order using the Bottom-Up Merge Sort algorithm."
},
"Sorting Complexity": {
    "definition": "Sorting complexity refers to the time and space requirements of sorting algorithms.",
    "code": "",
    "output": "Sorting algorithms can have different time and space complexities, such as O(n log n) for Merge Sort and Quick Sort, O(n^2) for Selection Sort and Insertion Sort, and O(n) for Counting Sort."
},
"Comparators and Stability": {
    "definition": "A comparator is a function that defines the order of elements during sorting. Stability in sorting refers to preserving the relative order of equal elements in the input.",
    "code": "",
    "output": "A comparator can be customized to sort elements based on specific attributes or keys. A stable sorting algorithm maintains the relative order of equal elements."
},
"Quicksort": {
    "definition": "Quicksort is a divide-and-conquer sorting algorithm that selects a pivot element, partitions the array into two subarrays, and recursively sorts them.",
    "code": "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)",
    "output": "The quicksort function takes an unsorted list as input and returns the list sorted in ascending order using the Quicksort algorithm."
},
"Duplicate Keys": {
    "definition": "Duplicate keys refer to having multiple elements with the same sorting key in the input.",
    "code": "",
    "output": "Sorting algorithms can handle duplicate keys differently. Some algorithms maintain the order of equal elements, while others may not."
},
"System Sort": {
    "definition": "System Sort refers to using the built-in sorting function or method provided by the programming language or system.",
    "code": "",
    "output": "In Python, you can use the built-in sorted() function or list.sort() method to perform system sort using Timsort, a hybrid sorting algorithm derived from Merge Sort and Insertion Sort."
},
"Priority Queue and Binary Heaps": {
    "definition": "A priority queue is a data structure that allows efficient access to the element with the highest priority. Binary Heaps are commonly used to implement priority queues.",
    "code": "import heapq\n\n# Min-Heap\nheap = []\nheapq.heappush(heap, 3)\nheapq.heappush(heap, 1)\nheapq.heappush(heap, 2)\n\n# Get the smallest element\nmin_element = heapq.heappop(heap)\n\n# Max-Heap (negate the elements)\nmax_heap = []\nfor num in [3, 1, 2]:\n    heapq.heappush(max_heap, -num)\n\n# Get the largest element (negate it back)\nmax_element = -heapq.heappop(max_heap)",
    "output": "The heapq module in Python provides functions to create min-heaps and max-heaps, which can be used to implement priority queues efficiently."
},
"Heapsort": {
    "definition": "Heapsort is a sorting algorithm that uses a binary heap to efficiently sort elements.",
    "code": "import heapq\n\ndef heapsort(arr):\n    heap = arr.copy()\n    heapq.heapify(heap)\n    for i in range(len(arr)):\n        arr[i] = heapq.heappop(heap)",
    "output": "The heapsort function takes an unsorted list as input and returns the list sorted in ascending order using the Heapsort algorithm."
},
"Elementary and Balanced Search Trees": {
    "definition": "Search trees are data structures that support efficient insertion, deletion, and lookup operations.",
    "code": "",
    "output": "Elementary search trees, like Binary Search Trees (BSTs), are simple and easy to implement. Balanced search trees, like AVL trees and Red-Black trees, maintain balance to ensure efficient operations in worst-case scenarios."
},
"Red-Black BSTs": {
    "definition": "Red-Black BST is a type of self-balancing binary search tree where each node has an extra bit for denoting the color (red or black) and follows specific rules to maintain balance.",
    "code": "",
    "output": "Red-Black BSTs guarantee logarithmic time complexity for insertion, deletion, and lookup operations, making them efficient for dynamic ordered data sets."
},
"B-Tree": {
    "definition": "B-Tree is a self-balancing search tree data structure that maintains sorted data and is commonly used for databases and file systems.",
    "code": "",
    "output": "B-Trees provide efficient data retrieval and insertion, and their node capacity makes them suitable for storing large amounts of data."
},
"1D Range Search": {
    "definition": "1D Range Search refers to finding all elements within a given range in a one-dimensional data set.",
    "code": "",
    "output": "Search trees like BSTs and Red-Black trees can be used to efficiently perform 1D range search by traversing only relevant branches of the tree."
},
"Line Segment Intersection": {
    "definition": "Line Segment Intersection is the process of finding all points where two or more line segments intersect.",
    "code": "",
    "output": "Efficient algorithms like Bentley-Ottmann sweep line algorithm can be used to find line segment intersections in a set of line segments."
},
"Kd-Trees": {
    "definition": "Kd-Tree is a binary search tree used for efficient multidimensional search operations in k-dimensional space.",
    "code": "",
    "output": "Kd-Trees partition the space into regions and allow for faster nearest neighbor search and range search in multiple dimensions."
},
"Interval Search Tree": {
    "definition": "Interval Search Tree is a data structure used to efficiently search for intervals that overlap with a given interval.",
    "code": "",
    "output": "Interval Search Trees are helpful for scheduling and resource allocation tasks, where you need to find overlapping time intervals."
},
"Rectangle Intersection": {
    "definition": "Rectangle Intersection refers to finding the overlapping region between two rectangles in a 2D space.",
    "code": "",
    "output": "Efficient algorithms can be used to compute the intersection of rectangles by analyzing their coordinates and dimensions."
},
"Hash Table and Separate Chaining": {
    "definition": "A hash table is a data structure that stores key-value pairs and allows constant-time average case access to elements. Separate Chaining is a technique used to handle hash collisions.",
    "code": "",
    "output": "Hash tables provide efficient insertion, deletion, and retrieval of elements based on their keys. Separate chaining resolves hash collisions by maintaining a linked list for each bucket."
},
"Linear Probing": {
    "definition": "Linear Probing is a collision resolution technique used in hash tables to find the next available slot by incrementing the index linearly.",
    "code": "",
    "output": "Linear Probing helps in resolving hash collisions by searching for the next available slot in a linear manner within the hash table."
},
"Hash Table Context": {
    "definition": "Hash tables find wide applications in various domains, including caching, databases, compilers, and symbol tables.",
    "code": "",
    "output": "Hash tables play a crucial role in implementing various algorithms and data structures, making them a fundamental concept in computer science."
},
"Symbol Table Applications": {
    "definition": "Symbol tables are data structures that store unique keys and their associated values, allowing efficient symbol lookup and manipulation.",
    "code": "",
    "output": "Symbol tables are widely used in compilers, interpreters, and symbol management systems for programming languages to handle identifiers and their references."
},
"Depth-First Search": {
    "definition": "Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking.",
    "code": "",
    "output": "DFS is commonly used to traverse and explore graphs and is helpful in applications like finding connected components and detecting cycles in a graph."
},
"Breadth-First Search": {
    "definition": "Breadth-First Search (BFS) is a graph traversal algorithm that explores all the vertices of a graph level by level.",
    "code": "",
    "output": "BFS is used to find the shortest path in unweighted graphs and explore graphs with multiple layers or levels."
},

"Topological Sort": {
    "definition": "Topological Sort is an ordering of the vertices of a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before vertex v in the ordering.",
    "code": "",
    "output": "Topological Sort is useful in scheduling tasks that have dependencies and in determining the order of execution in a workflow."
},
"Strong Components": {
    "definition": "Strongly Connected Components (SCCs) are groups of vertices in a directed graph where each vertex is reachable from every other vertex in the group.",
    "code": "",
    "output": "Finding SCCs is crucial in many applications, such as in network analysis, to identify groups of nodes that are highly interconnected."
},
"WordNet": {
    "definition": "WordNet is a lexical database that groups words into sets of synonyms called synsets and provides semantic relationships between words.",
    "code": "",
    "output": "WordNet is commonly used in natural language processing tasks, such as word sense disambiguation and semantic similarity measurement."
},
"Introduction to MSTs": {
    "definition": "Minimum Spanning Trees (MSTs) are subsets of edges in an undirected graph that connect all the vertices with the minimum total edge weight.",
    "code": "",
    "output": "MSTs are used in network design, clustering, and approximation algorithms to find the most efficient connections between nodes."
},
"Greedy Algorithm": {
    "definition": "Greedy Algorithm is an algorithmic paradigm that makes locally optimal choices at each step with the hope of finding a global optimum.",
    "code": "",
    "output": "Greedy algorithms are simple and efficient, and they are used in various optimization problems, including those related to MSTs and scheduling."
},
"Kruskal's Algorithm": {
    "definition": "Kruskal's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph.",
    "code": "",
    "output": "Kruskal's Algorithm works by sorting the edges by weight and adding them to the MST if they do not create a cycle."
},
"Prim's Algorithm": {
    "definition": "Prim's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph.",
    "code": "",
    "output": "Prim's Algorithm works by starting from an arbitrary vertex and adding the minimum weight edges that connect the current MST to the rest of the graph."
},
"Shortest Paths": {
    "definition": "Shortest Paths refer to finding the shortest path between two vertices in a graph, considering the weights of the edges.",
    "code": "",
    "output": "Shortest Paths algorithms like Dijkstra's Algorithm and Bellman-Ford Algorithm are commonly used in navigation systems and network routing."
},
"Dijkstra's Algorithm": {
    "definition": "Dijkstra's Algorithm is a shortest path algorithm that finds the shortest path from a source vertex to all other vertices in a non-negative weighted graph.",
    "code": "",
    "output": "Dijkstra's Algorithm is efficient for finding the shortest paths in networks, maps, and transportation systems."
},
"Edge-Weighted DAGs": {
    "definition": "Edge-Weighted Directed Acyclic Graphs (DAGs) are directed graphs with no cycles and weights assigned to edges.",
    "code": "",
    "output": "Edge-Weighted DAGs are used to model various real-world scenarios, such as project scheduling and task dependencies."
},
"Negative Weights": {
    "definition": "Negative Weights refer to the presence of edges with negative weights in a graph.",
    "code": "",
    "output": "Graphs with negative weights require specialized algorithms like the Bellman-Ford Algorithm to find shortest paths."
},
"Maximum Flow and Minimum Cut": {
    "definition": "Maximum Flow and Minimum Cut are concepts in network flow problems, where the goal is to maximize flow from a source to a sink while minimizing the cut capacity.",
    "code": "",
    "output": "Maximum Flow and Minimum Cut algorithms are used in various applications, such as transportation networks and flow analysis."
},
"Ford–Fulkerson Algorithm": {
    "definition": "The Ford–Fulkerson Algorithm is an iterative method used to find the maximum flow in a flow network.",
    "code": "",
    "output": "The Ford–Fulkerson Algorithm works by finding augmenting paths from the source to the sink and adjusting the flow along these paths until no more augmenting paths can be found."
},
"Maxflow–Mincut Theorem": {
    "definition": "The Maxflow–Mincut Theorem states that the maximum flow in a flow network is equal to the capacity of the minimum cut.",
    "code": "",
    "output": "The Maxflow–Mincut Theorem provides a fundamental insight into network flow problems and is used to verify the correctness of flow algorithms."
},
"Running Time Analysis": {
    "definition": "Running Time Analysis refers to the study of the computational time required by an algorithm as a function of the input size.",
    "code": "",
    "output": "Analyzing the running time of algorithms helps in understanding their efficiency and scalability for different problem sizes."
},
"Radix Sorts": {
    "definition": "Radix Sort is a non-comparative sorting algorithm that sorts integers by grouping digits.",
    "code": "",
    "output": "Radix Sorts are used to efficiently sort large datasets with fixed-length keys or integers."
},
"LSD Radix Sort": {
    "definition": "Least Significant Digit (LSD) Radix Sort is a variant of Radix Sort that starts sorting from the least significant digit.",
    "code": "",
    "output": "LSD Radix Sort is efficient for sorting fixed-length integers and strings."
},
"MSD Radix Sort": {
    "definition": "Most Significant Digit (MSD) Radix Sort is a variant of Radix Sort that starts sorting from the most significant digit.",
    "code": "",
    "output": "MSD Radix Sort is useful for sorting variable-length strings and keys."
},
"Tries": {
    "definition": "Trie, also known as Prefix Tree, is a tree-like data structure used to store a dynamic set of strings.",
    "code": "",
    "output": "Tries are commonly used in search engines, spell-checkers, and applications involving efficient string lookups and pattern matching."
},
"R-way Tries": {
    "definition": "R-way Tries are a type of Tries where each node has R children, where R is the size of the alphabet or character set.",
    "code": "",
    "output": "R-way Tries are efficient for storing strings and supporting string-related operations, like prefix search and autocomplete."
},
"Ternary Search Tries": {
    "definition": "Ternary Search Tries are a variant of Tries that use a ternary structure for space optimization.",
    "code": "",
    "output": "Ternary Search Tries are helpful in applications like spell-checking and IP address matching."
},
"Character-Based Operations": {
    "definition": "Character-Based Operations refer to operations involving strings, characters, and substrings.",
    "code": "",
    "output": "Character-Based Operations are fundamental for working with text data and performing string manipulation."
},

"Substring Search": {
    "definition": "Substring Search is the process of finding occurrences of a pattern (substring) within a larger text.",
    "code": "",
    "output": "Efficient substring search algorithms like Knuth–Morris–Pratt and Boyer–Moore are used to find patterns in text data."
},
"Knuth–Morris–Pratt": {
    "definition": "The Knuth–Morris–Pratt algorithm is a substring search algorithm that efficiently finds occurrences of a pattern in a text.",
    "code": "",
    "output": "The Knuth–Morris–Pratt algorithm improves the efficiency of substring search by using a preprocessed pattern to skip unnecessary comparisons."
},
"Boyer–Moore": {
    "definition": "The Boyer–Moore algorithm is a substring search algorithm that efficiently finds occurrences of a pattern in a text.",
    "code": "",
    "output": "The Boyer–Moore algorithm is particularly useful for large texts and long patterns, as it skips characters based on a precomputed bad character table."
},
"Rabin–Karp": {
    "definition": "The Rabin–Karp algorithm is a substring search algorithm that uses hashing to efficiently find occurrences of a pattern in a text.",
    "code": "",
    "output": "The Rabin–Karp algorithm is helpful for finding multiple pattern occurrences in a text using rolling hash functions."
},
"Regular Expressions": {
    "definition": "Regular Expressions (REs) are patterns used to match strings or search for specific patterns in text data.",
    "code": "",
    "output": "Regular Expressions are widely used in text processing, validation, and pattern matching applications."
},
"REs and NFAs": {
    "definition": "Regular Expressions can be represented by Non-deterministic Finite Automata (NFAs) to efficiently match patterns.",
    "code": "",
    "output": "NFAs provide a theoretical foundation for understanding Regular Expressions and their computational properties."
},
"NFA Simulation": {
    "definition": "NFA Simulation is the process of simulating Non-deterministic Finite Automata to match patterns.",
    "code": "",
    "output": "Efficient algorithms are used to simulate NFAs and match patterns in text data using Regular Expressions."
},
"NFA Construction": {
    "definition": "NFA Construction is the process of building Non-deterministic Finite Automata from Regular Expressions.",
    "code": "",
    "output": "Efficient algorithms construct NFAs from Regular Expressions to perform pattern matching tasks."
},
"Data Compression": {
    "definition": "Data Compression is the process of reducing the size of data to save storage space or transmission time.",
    "code": "",
    "output": "Data Compression techniques like Run-Length Coding, Huffman Compression, and LZW Compression are commonly used in file compression and data transmission."
},
"Run-Length Coding": {
    "definition": "Run-Length Coding is a lossless data compression technique that replaces repeated sequences of identical symbols with a single symbol and a count.",
    "code": "",
    "output": "Run-Length Coding is useful for compressing data with long runs of repeated symbols, such as images and simple graphics."
},
"Huffman Compression": {
    "definition": "Huffman Compression is a lossless data compression technique that assigns variable-length codes to different symbols based on their frequencies.",
    "code": "",
    "output": "Huffman Compression generates efficient codes for symbols that occur more frequently, resulting in better compression ratios."
},
"LZW Compression": {
    "definition": "LZW Compression (Lempel-Ziv-Welch) is a lossless data compression technique that replaces frequently occurring sequences of characters with shorter codes.",
    "code": "",
    "output": "LZW Compression is commonly used in file formats like GIF and TIFF and is suitable for compressing text and image data."
},

"Reductions": {
    "definition": "Reductions are techniques used to transform one problem into another to analyze complexity and solve problems.",
    "code": "",
    "output": "Reductions are fundamental in the study of computational complexity and help relate the difficulty of different problems."
},
"Introduction to Reductions": {
    "definition": "Introduction to Reductions provides an overview of the concepts and applications of problem reductions.",
    "code": "",
    "output": "Reductions help understand the computational difficulty of problems and their interconnections."
},
"Designing Algorithms": {
    "definition": "Designing Algorithms involves creating efficient algorithms for various computational problems.",
    "code": "",
    "output": "Algorithm design involves applying reduction techniques and problem-solving strategies to develop efficient solutions."
},
"Establishing Lower Bounds": {
    "definition": "Establishing Lower Bounds involves proving the minimum time complexity required to solve a problem.",
    "code": "",
    "output": "Lower bounds are crucial in determining the intrinsic difficulty of computational problems and understanding the limits of algorithms."
},
"Linear Programming (optional)": {
    "definition": "Linear Programming is a mathematical optimization technique used to find the best outcome in a mathematical model with linear relationships.",
    "code": "",
    "output": "Linear Programming is widely used in various optimization problems, including resource allocation and production planning."
},
"Simplex Algorithm": {
    "definition": "The Simplex Algorithm is an iterative method used to solve linear programming problems.",
    "code": "",
    "output": "The Simplex Algorithm efficiently finds the optimal solution to linear programming problems by moving along the edges of the feasible region."
},
"Simplex Implementations": {
    "definition": "Simplex Implementations refer to the practical implementation and optimization of the Simplex Algorithm.",
    "code": "",
    "output": "Various techniques are used to optimize the Simplex Algorithm for solving real-world linear programming problems."
},
"Intractability": {
    "definition": "Intractability refers to computational problems that cannot be efficiently solved using algorithms.",
    "code": "",
    "output": "Understanding intractable problems is essential in the study of computational complexity and the limitations of computing resources."
},
"P vs. NP": {
    "definition": "P vs. NP is a major unsolved problem in computer science that addresses the relationship between polynomial-time algorithms and non-deterministic polynomial-time algorithms.",
    "code": "",
    "output": "The resolution of the P vs. NP problem would have significant implications for cryptography, optimization, and artificial intelligence."
},
"NP-Completeness": {
    "definition": "NP-Completeness is a property of computational problems that are at least as hard as any problem in the complexity class NP.",
    "code": "",
    "output": "Identifying NP-Complete problems helps categorize computational problems based on their complexity and difficulty."
},
"List": {
    "definition": "A list is a versatile and mutable data structure in Python used to store a collection of elements.",
    "code": "",
    "output": "Lists are commonly used for holding multiple items and can store elements of different data types."
},
"Tuple": {
    "definition": "A tuple is an immutable data structure in Python used to store an ordered sequence of elements.",
    "code": "",
    "output": "Tuples are similar to lists but cannot be modified after creation, making them suitable for representing fixed collections."
},
"Set": {
    "definition": "A set is an unordered collection of unique elements in Python.",
    "code": "",
    "output": "Sets are commonly used for eliminating duplicate values from a sequence and performing mathematical set operations."
},
"Dictionary": {
    "definition": "A dictionary is an unordered collection of key-value pairs in Python.",
    "code": "",
    "output": "Dictionaries are useful for mapping keys to corresponding values and are efficient for data retrieval based on keys."
},
"List Methods": {
    "definition": "List methods are built-in functions that can be performed on lists to modify or retrieve data.",
    "code": "",
    "output": "List methods allow you to manipulate lists by adding, removing, searching, sorting, and more."
},
"append(x)": {
    "definition": "The 'append()' method adds a single element 'x' at the end of the list.",
    "code": "",
    "output": "After using 'append()', the list will contain the new element 'x' as the last element."
},
"extend(iterable)": {
    "definition": "The 'extend()' method adds all elements from an iterable to the end of the list.",
    "code": "",
    "output": "The 'extend()' method allows you to concatenate multiple elements to the list efficiently."
},
"insert(i, x)": {
    "definition": "The 'insert()' method inserts an element 'x' at a specified index 'i' in the list.",
    "code": "",
    "output": "After using 'insert()', the list will include the new element 'x' at the specified index 'i'."
},
"remove(x)": {
    "definition": "The 'remove()' method removes the first occurrence of element 'x' from the list.",
    "code": "",
    "output": "After using 'remove()', the first occurrence of 'x' will be removed from the list."
},
"pop([i])": {
    "definition": "The 'pop()' method removes and returns the element at the specified index 'i'. If 'i' is not provided, it removes and returns the last element.",
    "code": "",
    "output": "After using 'pop()', the element at the specified index 'i' will be removed and returned."
},
"clear()": {
    "definition": "The 'clear()' method removes all elements from the list, making it an empty list.",
    "code": "",
    "output": "After using 'clear()', the list will be empty with no elements."
},
"index(x[, start[, end]])": {
    "definition": "The 'index()' method returns the index of the first occurrence of element 'x' in the list. You can specify optional 'start' and 'end' parameters to search within a specific range.",
    "code": "",
    "output": "After using 'index()', you will get the index of the first occurrence of 'x' in the list."
},
"count(x)": {
    "definition": "The 'count()' method returns the number of occurrences of element 'x' in the list.",
    "code": "",
    "output": "After using 'count()', you will get the count of occurrences of 'x' in the list."
},
"sort(*, key=None, reverse=False)": {
    "definition": "The 'sort()' method arranges the elements in ascending order. You can provide an optional 'key' function to customize the sorting. Use 'reverse=True' to sort in descending order.",
    "code": "",
    "output": "After using 'sort()', the list will be sorted in ascending order."
},
"reverse()": {
    "definition": "The 'reverse()' method reverses the order of elements in the list.",
    "code": "",
    "output": "After using 'reverse()', the elements of the list will be reversed."
},
"copy()": {
    "definition": "The 'copy()' method creates a shallow copy of the list, i.e., a new list with the same elements.",
    "code": "",
    "output": "After using 'copy()', you will have a new list that is a replica of the original list."
},
"List Comprehensions": {
    "definition": "List comprehensions provide a concise way to create lists based on other sequences or iterables.",
    "code": "",
    "output": "List comprehensions allow you to generate new lists by applying expressions to existing sequences or iterables."
},
"Using Lists as Stacks": {
    "definition": "Lists can be used as stacks using the 'append()' and 'pop()' methods.",
    "code": "",
    "output": "By using 'append()' and 'pop()', lists can function as Last-In-First-Out (LIFO) data structures."
},
"Using Lists as Queues": {
    "definition": "While lists can be used as queues, they are not efficient due to slow inserts or pops from the beginning. Instead, 'collections.deque' is recommended for efficient queue operations.",
    "code": "",
    "output": "Lists can be used as First-In-First-Out (FIFO) queues, but 'collections.deque' is more efficient for queue operations."
},
"Looping Techniques": {
    "definition": "Looping techniques refer to different methods for iterating through sequences and performing specific tasks.",
    "code": "",
    "output": "Looping techniques help in efficient data processing, retrieval, and manipulation during iterations."
},
"items()": {
    "definition": "The 'items()' method is used to retrieve both the key and value while looping through a dictionary.",
    "code": "",
    "output": "When using 'items()', you get a key-value pair during each iteration through the dictionary."
},
"enumerate()": {
    "definition": "The 'enumerate()' function is used to retrieve the position index and corresponding value while looping through a sequence.",
    "code": "",
    "output": "When using 'enumerate()', you get the index and value during each iteration through the sequence."
},
"zip()": {
    "definition": "The 'zip()' function is used to loop over two or more sequences simultaneously.",
    "code": "",
    "output": "When using 'zip()', elements from multiple sequences are combined and processed together during iteration."
},
"reversed()": {
    "definition": "The 'reversed()' function is used to loop over a sequence in reverse order.",
    "code": "",
    "output": "When using 'reversed()', the sequence is traversed in reverse from the last element to the first."
},
"sorted()": {
    "definition": "The 'sorted()' function is used to loop over a sequence in sorted order.",
    "code": "",
    "output": "When using 'sorted()', the elements of the sequence are sorted, and the iteration is performed in the sorted order."
},
"Comparing Sequences and Other Types": {
    "definition": "Sequences and other types in Python are compared using lexicographical ordering.",
    "code": "",
    "output": "Lexicographical ordering compares each element of the sequences until a difference is found during comparison."
},
"Python Object-Oriented Programming (OOP)": {
    "definition": "Object-Oriented Programming (OOP) is a programming paradigm that focuses on organizing code into classes and objects.",
    "code": "",
    "output": "OOP allows developers to model real-world entities as objects with attributes (data) and methods (functions)."
},
"Class": {
    "definition": "A class is a blueprint or template that defines the properties and behaviors of objects.",
    "code": "",
    "output": "A class encapsulates data (attributes) and functionality (methods) that are common to its objects."
},
"Object": {
    "definition": "An object is an instance of a class, representing a real-world entity with its own unique data and behavior.",
    "code": "",
    "output": "Objects are created from classes and allow interaction with attributes and methods defined in the class."
},
"Attributes": {
    "definition": "Attributes are data members (variables) that store information about the object's state.",
    "code": "",
    "output": "Each object may have different attribute values based on the class it belongs to."
},
"Methods": {
    "definition": "Methods are functions defined within a class, enabling objects to perform specific actions or behaviors.",
    "code": "",
    "output": "Methods define the behavior of objects and can modify the object's state or perform specific operations."
},
"Encapsulation": {
    "definition": "Encapsulation is the principle of bundling data (attributes) and methods together within a class.",
    "code": "",
    "output": "Encapsulation hides the internal implementation details of an object and exposes only the necessary interface."
},
"Abstraction": {
    "definition": "Abstraction is the process of simplifying complex implementation details and focusing on essential features.",
    "code": "",
    "output": "Abstraction allows developers to create class interfaces without revealing the underlying complexities."
},
"Inheritance": {
    "definition": "Inheritance is a mechanism where a class (subclass) inherits attributes and methods from another class (superclass).",
    "code": "",
    "output": "Inheritance promotes code reuse and hierarchy in object relationships."
},
"Polymorphism": {
    "definition": "Polymorphism allows objects to be treated as instances of their superclass and enables method overloading and overriding.",
    "code": "",
    "output": "Polymorphism allows the same method to have different implementations in different classes, enhancing flexibility."
},
"Class Constructor (__init__ method)": {
    "definition": "The __init__ method is a special method in Python classes that initializes object attributes during object creation.",
    "code": "",
    "output": "The __init__ method is automatically called when an object is created from the class and sets initial attribute values."
},
"Class Destructor (__del__ method)": {
    "definition": "The __del__ method is a special method that is called when an object is about to be destroyed or deallocated.",
    "code": "",
    "output": "The __del__ method is used to perform clean-up activities or release resources before the object is removed from memory."
},
"Class Methods": {
    "definition": "Class methods are methods that operate on the class and are not bound to any specific instance of the class.",
    "code": "",
    "output": "Class methods are defined using the @classmethod decorator and receive the class as their first argument."
},
"Static Methods": {
    "definition": "Static methods are methods that do not require access to the class or instance and are independent of the class.",
    "code": "",
    "output": "Static methods are defined using the @staticmethod decorator and do not receive the class or instance as their first argument."
},
"Multiple Inheritance": {
    "definition": "Multiple inheritance is a feature where a class can inherit attributes and methods from more than one superclass.",
    "code": "",
    "output": "Multiple inheritance can lead to diamond inheritance problems and requires careful handling of method resolution order."
},
"Method Overloading": {
    "definition": "Method overloading is a feature that allows a class to define multiple methods with the same name but different parameters.",
    "code": "",
    "output": "Python does not support traditional method overloading, but it can be achieved using default parameters or variable-length argument lists."
},
"Method Overriding": {
    "definition": "Method overriding is a feature that allows a subclass to provide a specific implementation for a method already defined in its superclass.",
    "code": "",
    "output": "Method overriding enables a subclass to customize the behavior of a method inherited from its superclass."
},
"Class Variables": {
    "definition": "Class variables are variables that are shared among all instances (objects) of a class.",
    "code": "",
    "output": "Class variables are defined outside any method and remain constant across all instances of the class."
},
"Instance Variables": {
    "definition": "Instance variables are variables that are unique to each instance (object) of a class.",
    "code": "",
    "output": "Instance variables are defined within methods and are specific to individual objects."
},
 "False": {
        "definition": "Boolean value representing False.",
        "code": colorama.Fore.GREEN + "False" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "False" + colorama.Style.RESET_ALL
    },
    "True": {
        "definition": "Boolean value representing True.",
        "code": colorama.Fore.GREEN + "True" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "True" + colorama.Style.RESET_ALL
    },
    "None": {
        "definition": "A special constant representing the absence of a value or a null value.",
        "code": colorama.Fore.GREEN + "None" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "None" + colorama.Style.RESET_ALL
    },
    "NotImplemented": {
        "definition": "A special constant used to denote that a certain operation is not implemented.",
        "code": colorama.Fore.GREEN + "NotImplemented" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "NotImplemented" + colorama.Style.RESET_ALL
    },
    "__debug__": {
        "definition": "A constant that is True if Python was not started with an -O option.",
        "code": colorama.Fore.GREEN + "__debug__" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "__debug__" + colorama.Style.RESET_ALL
    },
    "quit": {
        "definition": "A built-in function that terminates the Python interpreter.",
        "code": colorama.Fore.GREEN + "quit()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will terminate the Python interpreter." + colorama.Style.RESET_ALL
    },
    "exit": {
        "definition": "A built-in function that terminates the Python interpreter.",
        "code": colorama.Fore.GREEN + "exit()" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will terminate the Python interpreter." + colorama.Style.RESET_ALL
    },
    "copyright": {
        "definition": "A string containing the copyright information of Python.",
        "code": colorama.Fore.GREEN + "copyright" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will return the copyright information of Python." + colorama.Style.RESET_ALL
    },
    "credits": {
        "definition": "A string containing the list of people who have contributed to Python.",
        "code": colorama.Fore.GREEN + "credits" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will return the list of contributors to Python." + colorama.Style.RESET_ALL
    },
    "license": {
        "definition": "A string containing the license information of Python.",
        "code": colorama.Fore.GREEN + "license" + colorama.Style.RESET_ALL,
        "output": colorama.Fore.YELLOW + "This will return the license information of Python." + colorama.Style.RESET_ALL
    },
    # ... continue for other concepts and built-in functions


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






'''
# brute-forces

def calculate_similarity(word1, word2):
    common_characters = set(word1) & set(word2)
    return len(common_characters) / max(len(word1), len(word2))


def get_similar_words(input_word, words_list, num_similar=5):
    similar_words = []
    for word in words_list:
        similarity = calculate_similarity(input_word, word)
        if similarity > 0.01:
            similar_words.append((word, similarity))

    similar_words.sort(key=lambda x: x[1], reverse=True)
    return [word for word, _ in similar_words[:num_similar]]


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
'''
