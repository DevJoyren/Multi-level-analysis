from pathlib import Path
from components.analysis import Analysis


class GenerateReport:

    def generate_report(self, stats):
        """
        Generates a natural-language style report from the given statistics.
        """

        lines = []
        lines.append("=== MULTI LEVEL TEXT ANALYSIS REPORT ===")
        lines.append("")

        total_words = stats.get('total_words', 0)
        unique_words = stats.get('unique_words', 0)
        richness = stats.get('richness_percentage', 0)
        most_common_length = stats.get('most_common_word_length', 0)
        hapax_count = stats.get('hapax_count', 0)
        top20 = stats.get('top20_words', [])
        top20_percentage = stats.get('top20_percentage', 0)


        total_sentences = stats.get('total_sentences', 0)
        sentence_lengths = stats.get("average_sentence", 0)
        shortest_sentence = stats.get("shortest_sentence", 0)
        longest_sentence = stats.get("longest_sentence", 0)

        lines.append(f"There are in total of {total_sentences} sentences in the text file, " 
                     f"the average of {sentence_lengths}% words per sentence. "
                     f"the shortest sentence is '{shortest_sentence}', and"
                     f"the longest sentence is '{longest_sentence}'.")

        lines.append(
            f"There are a total of {total_words} words inside this text document, "
            f"of which {unique_words} are unique. "
        )
        lines.append(
            f"This means the overall richness of the vocabulary is approximately {richness} percent."

            f"The most common word length found in the text is {most_common_length} characters. "

        )
        lines.append(f"Additionally, {hapax_count} words appeared only once throughout the entire document, "
            f"indicating a fair amount of lexical diversity.")

        lines.append("The twenty most frequently used words are listed below, ranked by occurrence:")
        lines.append("")

        for rank, word in enumerate(top20, start=1):
            lines.append(f"   {rank:>2}. {word}")

        lines.append("")
        lines.append(
            f"Together, these top twenty words account for roughly {top20_percentage} percent of the entire text."
        )
        lines.append("")
        return '\n'.join(lines).strip()



    def save_report(self, output_path: str, report_content: str) -> None:
        """
        Saves the generated report to a text file.
        """
        Path(output_path).write_text(report_content, encoding="utf-8")
