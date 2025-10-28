# Multi-Level Text Analysis

## Overview
The **Multi-Level Text Analysis** project is a Python-based application designed to perform detailed linguistic and statistical analysis on plain text files. It automatically processes a `.txt` file and generates a comprehensive report containing insights about sentence structure, vocabulary richness, and word usage.

This project demonstrates how computational text analysis can be used to extract meaningful patterns from language — bridging programming, data analysis, and natural language understanding.

---

## Features
- **Sentence-Level Statistics**  
  Calculates total sentences and the average sentence length in words.

- **Word-Level Analysis**  
  Measures total and unique words, word frequency distribution, and vocabulary richness (unique-to-total ratio).

- **Word Length Distribution**  
  Analyzes how often words of certain lengths appear and identifies the most common word length.

- **Hapax Legomena Detection**  
  Finds words that appear exactly once in the text (rare word analysis).

- **Top Words Extraction**  
  Identifies the 20 most frequently occurring words and calculates their percentage of total text usage.

- **Statistical Insights**  
  Finds the shortest and longest sentences to reveal text variability and structure.

- **Formatted Report Generation**  
  Automatically generates a structured report in `.pdf` or `.txt` format summarizing all results.

---

## File Structure
```plaintext
Multi-level-analysis/
│
├── components/
│   ├── analysis.py          # Handles all word and sentence analysis logic
│   ├── handle_file.py       # Manages file reading and text extraction
│   ├── generate_report.py   # Creates and exports the analysis report
│
├── text_files/
│   └── artificial_intelligence.txt  # Example input file
│
├── reports/
│   └── ai_analysis_report.txt       # Example generated report
│
├── main.py                # Main entry point for running the analysis
├── README.md              # Project documentation
```

---

## How It Works
1. The user provides a text file as input.  
2. The file is processed by the `HandleFile` class to extract clean text data.  
3. The `Analysis` class performs a series of computations to analyze the text at multiple levels (word, sentence, statistical).  
4. The `GenerateReport` class compiles the results into a readable, structured report and saves it to the `/reports` folder.

---

## Key Achievements
- Demonstrates modular software design with reusable components.
- Implements real-world natural language processing fundamentals without external libraries.
- Produces data-driven insights in a clear, structured format.
- Serves as a foundation for further extensions such as sentiment analysis, keyword extraction, or visualization dashboards.

---

## Usage
Run the main file in your terminal:
```bash
python main.py
```
