from pathlib import Path

from components.analysis import Analysis


class GenerateReport:

    def generate_report(self, stats):
        """
        Generates a report from the given statistics.
        """

        lines = []

        lines.append(f"=== MULTI LEVEL TEXT ANALYSIS ===")
        lines.append("")
        lines.append(f"Total words: {stats.get('total_words', 0)}")
        lines.append(f"Unique words: {stats.get('unique_words', 0)}")
        lines.append(f"Richness: {stats.get('richness_percentage', 0)}")
        lines.append(f"Most common word length: {stats.get('most_common_word_length', 0)}")
        lines.append(f"Hapax words: {stats.get('hapax_count', 0)}")
        lines.append(f"Top 20 words: {stats.get('top20_words', 0)}")
        lines.append(f"Top 20 percentage: {stats.get('top20_percentage', 0)}")
        lines.append("")
        return '\n'.join(lines).strip()

    def save_report(self, output_path: str, report_content: str) -> None:
        """
        Saves the report from the generated report.
        :param output_path:
        """
        Path(output_path).write_text(report_content, encoding="utf-8")


