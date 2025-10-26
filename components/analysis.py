# Imports >>>
import re
from collections import Counter


class Analysis:
    def __init__(self):
        # sentence statistics initialization state.
        self.sentences = []
        self.total_sentences = 0


        # word statistics initialization state.
        self.words = []
        self.total_words = 0
        self.unique_words = Counter()
        self.word_len = Counter()



        # All stats together for creating final report.
        self.stats = {}


    def sentence_analyser(self, text):
        """
        :param text:
        sum of sentences in the text
        average sentence length in words
        shortest sentence
        longest sentence"""
        sentence = re.split(r'[.!?]+', text) # Split text into sentences based on punctuation marks.`
        total = len(sentence)    # Count the total number of sentences.
        self.total_sentences = total
        print(f"Total sentences: {self.total_sentences}")

        #average sentence length in words
        sentence_lengths = [len(re.findall(r"[a-z0-9]+(?:\.)*", s)) for s in sentence if s.strip()]
        average_length = sum(sentence_lengths) / total if total else 0
        print(f"Average sentence length (in words): {average_length:.2f}")

        # shortest sentence
        valid_sentences = [s for s in sentence if len(s.strip()) > 5]
        shortest_sentence = min(valid_sentences, key=len, default="")
        print(f"Shortest sentence: {shortest_sentence.strip()}")

        # longest sentence
        longest_sentence = max((s for s in sentence if s.strip()), key=len, default="")
        print(f"Longest sentence: {longest_sentence.strip()}")

        #TODO Ela add your variables inside stats
        self.stats.update({
            "total_sentences": total, # like this

        })

    def word_analyser(self, text:str) -> None :
        """
        :param text:
        Analyze words and compute statistics.
         - total words
         - unique words (vocabulary size)
         - vocabulary richness (unique/total in percentage
         - word length
         - word count
         - hapax words (appear exactly once)
         - top 20 words

         puts everything inside a list called self.stats
        """

        # Matches any single "word" character (alphanumeric or underscore). Equivalent to [a-zA-Z0-9_].
        # self.words is a list containing all words inside the document
        self.words = re.findall(r"[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*", text)

        # The length of the words list equals to the number of words in numbers
        # The unique words is a list of words all words are only counted once so no duplicates
        self.total_words = len(self.words)
        self.unique_words = Counter(self.words)

        # The length of the list of unique words in numbers
        # The richness of unique words to the total of words
        # times a hundred to make it a percentage wise
        vocabulary_size = len(self.unique_words)
        richness = (vocabulary_size / self.total_words) * 100 if self.total_words else 0.0

        # Counts each character inside all words and organizes them based on amount of characters (length)
        # Also gets the most common length
        self.word_len = Counter(len(w) for w in self.words if w)
        most_common_word_len = self.word_len.most_common(1)[0][0] if self.word_len else 0 # no idea :3

        # find the hapax inside the given text.
        # Hapax is a word OR phrase that appears only once in a given body of text
        hapax_count = sum(1 for w, c in self.unique_words.items() if c == 1) # complicated line but alright

        # find the top 20 most words inside the text and counts them
        # how much is that in total to total words?
        top20 = self.unique_words.most_common(20)
        #                                                                                                     _     c
        # _ means ignore the first value inside the top20 list  c means number of times the word appears. [('the', 50)]
        # it sums all the values up. example: 50 + 45 + 43 ...
        top20_total = sum(c for _, c in top20)

        # divides the top 20 total with the total words in text times a 100
        top20_percentage = (top20_total / self.total_words) * 100 if self.total_words else 0.0


        # || Update the statistics list with their name and corresponding value.
        # || Easily saves everything inside a list
        self.stats.update({
            "total_words": self.total_words,
            "unique_words": vocabulary_size,
            "richness_percentage": round(richness, 2), # 2 decimals
            "most_common_word_length": most_common_word_len,
            "hapax_count": hapax_count,
            "top20_words": top20,
            "top20_percentage": round(top20_percentage, 2), # 2 decimals

        })



