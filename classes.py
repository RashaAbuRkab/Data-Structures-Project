"""
This module provides classes for text analysis and manipulation, 
including character and word frequency analysis, and text reversal 
using stack and queue data structures.
"""


class TextAnalyzer:
    """
    This class performs various text analyses such as character and word analysis.
    """

    def __init__(self, text):
        self.text = text.strip().lower() if text else ""
        self.char_array = list(self.text)

        if not self.text:
            raise ValueError("Input Text is empty.")

    def character_analysis(self):
        """Returns the frequency of characters in the given text."""
        char_dict = {}
        for i in self.char_array:
            if i not in ".!$@? ":
                if i not in char_dict:
                    char_dict[i] = 1
                else:
                    char_dict[i] += 1
        return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

    def word_analysis(self):
        """Returns the frequency of words in the given text."""
        words = self.text.split()
        unique_words = set(words)
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        return dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))

    def word_count(self):
        """Counts the number of words in the text."""
        return len(self.text.split())


class Stack:
    """A class to reverse the text using a stack."""

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Pushes an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and returns the last item from the stack."""
        return self.stack.pop() if self.stack else None

    def reverse_text(self, text):
        """Reverses the given text using a stack."""
        if not text:
            return "Input text is empty"
        for char in text.strip().lower():
            self.push(char)

        reversed_text = ""
        while self.stack:
            reversed_text += self.pop()
        return reversed_text


class Queue:
    """A class to print the word order using a queue."""

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the first item from the queue."""
        return self.queue.pop(0) if self.queue else None

    def reverse_word(self, text):
        """Reverses the words in the given text using a queue."""
        if not text:
            return "Input text is empty"
        for word in text.strip().lower().split():
            self.enqueue(word)

        fifo = ""
        while self.queue:
            fifo += self.dequeue() + " "
        return fifo.strip()
