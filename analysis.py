# Imports >>>
import re
from collections import Counter


class Analysis:
    def __init__(self):

        # word statistics initialization state.
        self.all_words = {}
        self.word_count = 0
        self.word_lengths = {}


    def text_input(self, file_path:str) -> str:
        """
        Handles the text input from the user.
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as file:
            text = file.read()   # Read the file
            text = text.lower()  # lowercase everything
            text = re.sub(r"[,-_:'""]", "", text) # replace unnecessary operations w non

            # TODO more normalization inside the text

            print("Text successfully read from file.")
        return text


    def sentence_analyser(self, text: str) -> str:
        """
         Analyses the sentences and handles every requirement.
        :param text:
        :return:
        """





    def word_analyser(self, text):
        """
        Analyses the words and handles every requirement.
        :param text:
        :return:
        """

        # \w stands for:
        # Matches any single "word" character (alphanumeric or underscore). Equivalent to [a-zA-Z0-9_].
        self.all_words = re.findall(r"\w+", text)


        # Looping trough each word inside the text and adding +1 for each word.

        for i in self.all_words:
            self.word_count += 1

        self.word_lengths = Counter(len(w) for w in self.all_words if w)

        # testing using print statements
        # print(self.words_dictionary)
        print("Total words: ", self.word_count)
        print("Word lengths by character: ", self.word_lengths)











    def generate_report(self, stats):
        """
        Generates a report from the given statistics.
        :param stats:
        :return:
        """
        ...


    def save_report(self, output_path):
        """

        :param output_path:
        :return:
        """
        ...