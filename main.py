from analysis import Analysis

file_path = './artificial_intelligence.txt'

if __name__ == '__main__':
    analysis = Analysis()

    text = analysis.text_input(file_path)
    print(text)





    # more to come we called the Analysis() class
    # now using analysis.  makes us able to run functions from Analysis()
