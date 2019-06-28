import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        ans=input("Please verify is the word %s (yes/no): "%get_close_matches(word,data.keys())[0])
        if ans=="yes":
            word=get_close_matches(word,data.keys())[0]
            return data[word]
        elif ans=="no":
            return "invalid word please check it"
        else:
            return "invalid entry"
    else:
        return "this word doesn't exist,please check the word"


choice="yes"
while choice=="yes":
    word=input("enter word: ")
    print(translate(word))
    print("\n")
    choice=input("Do you have a question (yes/no): ")
