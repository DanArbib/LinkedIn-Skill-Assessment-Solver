# LinkedIn Skill Assessment Quiz Helper



https://github.com/DanArbib/LinkedIn-Skill-Assessment-Solver/assets/141600490/cafbde30-c1f0-4f5a-a114-16885a015e6f




## Overview

This Python script assists in passing LinkedIn Skill Assessment quizzes by automating the process of capturing screenshots, performing OCR (Optical Character Recognition) on them, and trimming the recognized text to extract questions and find answers.

## Features

- Captures screenshots of the screen.
- Allows you to specify crop percentages for each side (top, bottom, left, right) before performing OCR.
- Displays the captured and cropped image for verification.
- Performs OCR on the cropped image to recognize text.
- Trims the recognized text to extract questions.
- Generates answers to LinkedIn questions using GPT.


To run this project, follow these steps:
1. Clone this GitHub repository to your local machine using the following command:
   https://github.com/DanArbib/LinkedIn-Skill-Assessment-Solver.git
2. Create a `.env` file in the project directory and add your OpenAI API key as follows:
   OPENAI_API_KEY=your_api_key_here
3. Use `pip` to install the project dependencies from the `requirements.txt` file:
   pip install -r requirements.txt
4. Execute the `main.py` script to start the project:
   python main.py

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


