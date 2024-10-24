import json
from nltk_utils import tokenize,stem,bag_of_words # type: ignore

with open('intents.json','r') as f:
    intent= json.load(f)

all_words = []
xy= []
for intent in intent['intents']:

