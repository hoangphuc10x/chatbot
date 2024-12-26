import sys
import json
import torch
import random
import os
import io
from nltk_utils import tokenize, bag_of_words
from model import NeuralNet

# Đặt lại stdout để sử dụng mã hóa UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load trained model
FILE = "E:\\zyear4\\clone\\NavCareer_C1SE.15_12-2024\\chatbot\\data.pth"  # Full path to the data.pth file
data = torch.load(FILE, weights_only=True)  # Set weights_only=True

model = NeuralNet(data["input_size"], data["hidden_size"], data["output_size"])
model.load_state_dict(data["model_state"])
model.eval()

all_words = data["all_words"]
tags = data["tags"]

# Load intents with absolute path
script_dir = os.path.dirname(__file__)  # Path to the current directory where chatbot.py is located
intents_path = os.path.join(script_dir, 'intents.json')  # Combine path to intents.json

# Load intents from the JSON file
with open(intents_path, "r", encoding="utf-8") as f:
    intents = json.load(f)

# Get user input from command-line or prompt if not provided
if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = input("Please enter your query: ")

# Process user input
sentence = tokenize(user_input)
X = bag_of_words(sentence, all_words)
X = torch.from_numpy(X).float()
output = model(X)
_, predicted = torch.max(output, dim=0)

tag = tags[predicted.item()]

# Find the corresponding response
for intent in intents["intents"]:
    if tag == intent["tag"]:
        response = random.choice(intent["responses"])
        # In ra phản hồi với mã hóa UTF-8
        print(response)
        break
