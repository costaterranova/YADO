import openai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def activity_finder():
    configure()
    openai.api_key = os.getenv('openai_api_key')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": os.getenv('list_of_things_to_do')},
                {"role": "user", "content": os.getenv('openai_prompt')}
            ],
        max_tokens=100
    )
    output = response.choices[0].message["content"]
    activity = output.split(' -- ')[0]
    time =  output.split(' -- ')[1]
    return activity, time
    