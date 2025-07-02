### Simplistic DIAL chat client

# About

This project is a simplistic Python client for calling DIAL chat service. 
It expects users' inputs (questions) in command line & sends them to DIAL.
Once DIAL responds, this python client prints the response to terminal

# How to run:
Save this code to a file, e.g., dial_chat.py.
Install the requests library if you haven't:
`pip install requests`
`python -m pip install python-dotenv`
Run the script:
`python dial_chat.py`
Note:
If the DIAL API expects a different payload or response structure, adjust the payload and the way the response is parsed according to the DIAL API documentation.
The model name (gpt-3.5-turbo) is a common default; check the docs for the correct value if needed.
Let me know if you want this saved as a file in your workspace!