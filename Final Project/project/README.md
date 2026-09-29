# Text Analyzer

#### Video Demo: ......(for only cs50😅)

#### Description:

Text Analyzer is a simple Python command-line program that takes text from the user and analyzes it. It tells the user how many words and characters are in the text and also finds the word that appears most often.

I made this project as my final project for CS50P. I wanted to make something simple enough that I could understand every part of the code, while still using several of the Python concepts I learned during the course.

The main file is `project.py`. It contains the `main()` function, which handles the user input and displays the results. The `count_words()` function counts the words in the text, while `count_characters()` counts the characters. The `most_common_word()` function uses a dictionary to keep track of how many times each word appears and then finds the word with the highest count.

For example, if the user enters a sentence containing the same word several times, the program can identify that word as the most common one. The program uses `split()` to separate the input into words and a dictionary to store the number of occurrences of each word.

I also included `test_project.py`. It contains unit tests for the three main functions in `project.py`. These tests check that the functions return the expected results for different inputs.

I decided to make the project a command-line program instead of building a graphical interface because I wanted to focus mainly on the Python programming. The project does not use any external libraries, so no `requirements.txt` file is needed.

To run the program, use:

    python project.py

After running it, enter some text when prompted and the program will display the analysis.