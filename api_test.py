import langchain as lc
import langchain_openai
import getpass
import os
import datetime

import requests as re

if not os.environ.get("PROMPT_API"):
    os.environ["PROMPT_API"] = getpass.getpass("Enter prompt API url: ")

supported_formats=["json", "xml", "yaml"]

for format in supported_formats:

    url=f"{PROMPT_API}/shape/1"
    response= re.get(url, timeout=10, headers={"Accept":f"application/{format}"})

    try:
        request_response=response.text
    except:
        print(response.status_code)

    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    from langchain_openai import ChatOpenAI

    #TODO implement support for some more models here using LangChain
    model = ChatOpenAI(model="gpt-4o")

    print(response.headers.Date)
    print(format)
    print(model.invoke(f"You will be given an item description. Tell me what is the item. \r\n {request_response}").content)
    receive_timestamp = datetime.datetime.now()-datetime.timedelta(hours = 1) #adjusted for ChatGPT timestamp in GMT
    response_timestamp = datetime.datetime.strptime(response.headers.Date, "%a, %d %b %Y %H:%M:%S %Z")
    
    print("Request time:\r\n",receive_timestamp-response_timestamp)
