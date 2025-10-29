from pathlib import Path
from components.analysis import Analysis


class GenerateReport:

    def generate_report(self, stats):
        """
        Generates a natural-language style report from the given statistics.
        """
        # Add variables to use within generating the report
        # We get them from the list stats

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
        average_lengths = stats.get("average_lengths", 0)
        shortest_sentence = stats.get("shortest_sentence", 0)
        longest_sentence = stats.get("longest_sentence", 0)


        # Total sentences
        lines.append(f"There are in total of {total_sentences} sentences in the text file, " 
                     f"with an average of {average_lengths} words per sentence.")

        # Shortest and longest sentence
        lines.append(
            f"The shortest sentence inside this document contains {shortest_sentence} words."
            f"While the longest sentence inside this document contains {longest_sentence} words.\n"
        )

        lines.append(
            f"There are a total of {total_words} words inside this text document, "
            f"of which {unique_words} are unique. \n"
            
            f"This means the overall richness of the vocabulary is approximately {richness} percent."
            f"The most common word length found in the text is {most_common_length} characters. "

        )
        lines.append(f"Additionally, {hapax_count} words appeared only once throughout the entire document, "
            f"indicating a fair amount of lexical diversity.")

        lines.append("The twenty most frequently used words are listed below, ranked by occurrence:")
        lines.append("")

        if top20 and isinstance(top20[0], tuple):
            max_count = top20[0][1]  # assume sorted descending by frequency
            lines.append("The twenty most frequently used words are listed below, ranked by occurrence:")
            lines.append("")

            for rank, (word, count) in enumerate(top20, start=1):
                # Normalize the bar length: scale count to 100% (max = 20 chars)
                bar_length = int((count / max_count) * 20)
                bar = "=" * bar_length
                lines.append(f"{rank:>2}. {word:<12} {bar} ({count})")
        else:
            # fallback if only words (no counts)
            lines.append("The twenty most frequently used words are listed below, ranked by occurrence:")
            lines.append("")
            for rank, word in enumerate(top20, start=1):
                lines.append(f"{rank:>2}. {word}")

        lines.append("")

        lines.append(
            f"Together, these top twenty words account for roughly {top20_percentage}% of the entire text."
        )

        lines.append("")
        return '\n'.join(lines).strip()



    def save_report(self, output_path: str, report_content: str) -> None:
        """
        Saves the generated report to a text file.
        """
        Path(output_path).write_text(report_content, encoding="utf-8")
