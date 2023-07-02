# Sentence Analyzer

This Python program analyzes a sentence and extracts specific words based on certain conditions.

## Description

The program takes a sentence as input and performs the following steps:

1. Split the sentence into separate sentences based on periods.
2. Remove the periods from the original sentence.
3. Split the modified sentence into individual words.
4. Iterate through each sentence and extract words that meet the conditions.
    - Words must start with an uppercase letter.
    - Words should match with words in the original sentence.
5. Build a list of extracted words along with their positions in the original sentence.
6. Display the extracted words in the format `position:word`, one per line.
7. If no words are extracted, display "None" indicating no matches found.

## Usage

1. Enter a sentence when prompted by the program.
2. The program will analyze the sentence and display the extracted words.

## Example

### Input
```
The Massachusetts Institute of Technology is a private research university located in Cambridge, Massachusetts, United States.
```

### Output
```

2:Massachusetts
3:Institute
5:Technology
13:Cambridge
14:Massachusetts
15:United
16:States
```

