from analysis import Analysis


if __name__ == '__main__':
    # Input file path and the report save path
    file_path = './artificial_intelligence.txt'
    out_path = './reports/ai_analysis_report.txt'

    analysis = Analysis()

    text = analysis.handle_text(file_path)
    analysis.word_analyser(text)

    # test by printing all statistics
    print(analysis.stats)
