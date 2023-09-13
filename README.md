# LinkedIn Skill Assessment Quiz Helper




## Overview

This Python script assists in passing LinkedIn Skill Assessment quizzes by automating the process of capturing screenshots, performing OCR (Optical Character Recognition) on them, and trimming the recognized text to extract questions and find answers.

## Features

- Captures screenshots of the screen.
- Allows you to specify crop percentages for each side (top, bottom, left, right) before performing OCR.
- Displays the captured and cropped image for verification.
- Performs OCR on the cropped image to recognize text.
- Trims the recognized text to extract questions.
- Generates answers to LinkedIn questions using the GPT-3 model.


Usage
Run the script: python main.py.
Follow the on-screen instructions to specify crop percentages for each side to capture the quiz area.
During the quiz, press 'Enter' to read each question.
The script will capture the question, perform OCR, trim the text, and generate answers if configured.
The recognized question and generated answer will be displayed.
Customization
You can customize the script by modifying the following:

OCR languages: You can change the languages for OCR by editing the reader initialization in the script.
Trimming keywords: To customize the keywords for trimming the text, you can modify the trim_text function.
Answer generation: Customize the answer generation logic in the generate_answer function based on your specific needs.
License
This script is provided under the MIT License. Feel free to modify and distribute it as needed.


