"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#i think this is a define list which refers some_words to all collections.
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# word loops elements in some words until finished.
for word in some_words:
    print(word)
# x loops elements in some words until finished.
for x in some_words:
    print(x)

print(some_words)
# it's like flow control. if count of words are less than 3, 
# types 'some_words contains more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words')
#define something
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #include all the information above
    print(platform.uname())

usefulFunction()
