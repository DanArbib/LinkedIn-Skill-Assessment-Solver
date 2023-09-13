import openai
import os
from dotenv import load_dotenv
load_dotenv()

def generate_answer(question):

    # Openai init key
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    prompt = f'I am taking a quiz and need to select the correct answer from the options provided. Question: [{question}]. Choose the correct answer.'

    response = openai.Completion.create(model="text-davinci-003", prompt=prompt.strip(), temperature=0,
                                              max_tokens=1000)
    res = response['choices'][0]['text'].replace('!', '').replace('"', '', ).strip()
    return res








