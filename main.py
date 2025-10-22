# Imports >>>
import platform
from components.analysis import Analysis
from components.generate_report import GenerateReport
from components.handle_file import HandleFile

if __name__ == '__main__':
    # Check which operating system the user is using.
    # Windows = \
    # Linux   = /

    if platform.system() == "Windows":
        # Input file path and the report save path
        file_path = 'text_files\artificial_intelligence.txt'
        out_path = '.\reports\ai_analysis_report.txt'

    else:
        # Input file path and the report save path
        file_path = 'text_files/artificial_intelligence.txt'
        out_path = './reports/ai_analysis_report.txt'


    handler = HandleFile()
    analysis = Analysis()
    report = GenerateReport()

    text = handler.handle_text(file_path)
    analysis.word_analyser(text)

    stats = analysis.stats

    final_report = report.generate_report(stats)
    report.save_report(out_path, final_report)


