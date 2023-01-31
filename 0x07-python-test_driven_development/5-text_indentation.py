#!/usr/bin/python3
"""
The module that prints a text with two line after ., ? and : characters
"""

def text_indentation(text):
    """Function that prints a text with two lines after ., ? and : characters
    Args:
    text: inputs string
    Returns:
    No return
    Raises:
    TypeError: if text is not a string
    """

    if type(text) is not a string:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ". ? :":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="") 
