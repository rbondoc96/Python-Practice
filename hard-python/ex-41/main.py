#!/usr/bin/env python3

import random
from urllib.request import urlopen
from sys import argv

from typing import List

def main():
    WORD_URL = "https://learncodethehardway.org/words.txt"
    WORDS = []

    def convert(snippet, phrase):
        # class_names is filled with random words from WORDS
        # The # of words taken is the # of occurences of %%% in the snippet
        # The words are capitalized
        class_names = [word.capitalize() for word in 
            random.sample(WORDS, snippet.count("%%%"))]

        # other_names is filled with random words from WORDS
        # The # of words taken is the # of occurences of *** in the snippet
        other_names = random.sample(WORDS, snippet.count("***"))
        results: List[str] = []
        param_names: List[str] = []

        # Creates a comma-separated list of parameters
        # Actually runs once since each snippet (key of PHRASES) has 1 instance
        # of @@@
        for i in range(snippet.count("@@@")):
            param_count = random.randint(1, 3)
            param_names.append(", ".join(random.sample(WORDS, param_count)))

        # This for() runs twice, once for the snippet, once for the phrase
        for sentence in snippet, phrase:
            result = sentence[:]

            for word in class_names:
                result = result.replace("%%%", word, 1)

            for word in other_names:
                result = result.replace("***", word, 1)

            # Since each snippet/phrase has 1 instance of @@@, only runs once
            for word in param_names:
                result = result.replace("@@@", word, 1)

            results.append(result)

            print("Snippet", snippet)
            print("Phrase", phrase)
            print("------------")            
            print("Result", result)
            print("Sentence", sentence)
            print("============")            

        return results


    # %%% - Class name
    # *** - Parameter or function name (each *** is a different word)
    # @@@ - Parameter
    PHRASES = {
        "class %%%(%%%)": "Make a class named %%% that is-a %%%",
        "class %%%:\n\tdef __init__(self, ***)": 
            "class %%% has-a __init__ that takes self and *** params.",
        "class %%%:\n\tdef ***(self, @@@)":
            "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
            "Set *** to an instance of class %%%",
        "***.***(@@@)":
            "From *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'":
            "From *** get the *** attribute and set it to ***",
    }

    # Do they want to drill phrases first?
    if len(argv) == 2 and argv[1] == "english":
        PHRASE_FIRST = True
    else:
        PHRASE_FIRST = False
    
    # Load up the words from the URL
    for word in urlopen(WORD_URL).readlines():
        WORDS.append(str(word.strip(), encoding="UTF-8"))

    try:
        while True:
            snippets = list(PHRASES.keys())
            random.shuffle(snippets)

            for snippet in snippets:
                phrase = PHRASES[snippet]
                question, answer = convert(snippet, phrase)
                
                if PHRASE_FIRST:
                    question, answer = answer, question
                
                print(question)
                input("[Press Enter to view the answer.]")
                print(f"ANSWER: {answer}\n\n")

    except EOFError:
        print("\nBye.")


if __name__ == "__main__":
    main()