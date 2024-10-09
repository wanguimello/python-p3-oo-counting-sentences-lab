#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        # Ensure the value is a string
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    # Method to check if value is a sentence
    def is_sentence(self):
        return self.value.endswith(".")
    
    # Method to check if value is a question
    def is_question(self):
        return self.value.endswith("?")
    
    # Method to check if value is an exclamation
    def is_exclamation(self):
        return self.value.endswith("!")
    
    # Method to count sentences in the value
    def count_sentences(self):
        # Replace common sentence terminators with "."
        cleaned_value = self.value.replace("!", ".").replace("?", ".")
        sentences = [s for s in cleaned_value.split(".") if s.strip()]
        return len(sentences)


