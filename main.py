#import depedencies

import openai
# create a python file and store your ChatGPT API key
from apikey import APIKEY

openai.api_key = APIKEY

output= openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    # sys , user , assistant
    messages=[
        {"role":"system","content":"Your a nutritionist"},
        {"role":"user","content":" i Need a breakfast recommendation filled with protein "},
    ]
)


print(output['choices'][0]['message']['content'])