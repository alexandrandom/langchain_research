import langchain as lc
import langchain_openai
import getpass
import os

import requests as re

url="https://phet-dev.colorado.edu/html/build-an-atom/0.0.0-3/simple-text-only-test-page.html"
response= re.get(url, timeout=10)

try:
    request_response=response.text
except:
   print(response.status_code)

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="o1-mini")
model.invoke(f"{request_response}")

