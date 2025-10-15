# Imports >>>


class Analysis:
    def __init__(self):
        self.total_words = 0
        ...


    def text_input(self, file_path):
        """
        Handles the text input from the user.
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as file:
            text = file.read()
            print(text)



    def sentence_analyser(self, text):
        """
         Analyses the sentences and handles every requirement.
        :param text:
        :return:
        """
        ...


    def word_analyser(self, text):
        """
        Analyses the words and handles every requirement.
        :param text:
        :return:
        """
        ...


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