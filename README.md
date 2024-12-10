# Chatbot Deployment with Flask and JavaScript

In this tutorial we deploy the chatbot I created in [this](https://github.com/python-engineer/pytorch-chatbot) tutorial with Flask and JavaScript.

This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains the starter files.


==============IN THE FIRST SETUP==============
Clone repo and create a virtual environment
```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
$ python -m venv venv
$ . venv/bin/activate ||    ./venv/Scripts/activate

```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt') || nltk.download('punkt_tab')
>>> quit()
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py

$ pip install underthesea

$ (venv) python app.py

```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ pip freeze > requirements.txt
set up requirement to run faster in the second time run app.py
```

$ (venv) python app.py 
for test on postman
```
$ (venv) python chat.py
test in terminal
```
=========IN THE SECOND TIME TO RUN========
-
$ pip install -r requirements.txt


