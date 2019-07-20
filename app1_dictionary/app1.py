import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.6)) > 0:
        correct_word = get_close_matches(word, data.keys(), n=1, cutoff=0.6)[0]
        #print(correct_word)
        yn = input("Did you mean %s instead? Enter Y for Yes and N for No: " %correct_word)
        if yn.lower() == "y":
            return data[correct_word]
        elif yn.lower() == "n":
            return "Word not found. Sorry"
        else:
            return "unacceptable entry"
    else:
        return "No such word!!"

word = (input("Give me the word: "))

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
#print(translate(word))
