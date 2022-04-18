# Same lexicon from Exercise 48

from typing import Tuple, List, Dict

class Lexicon:

    lexicon: Dict[str, List[str]] = {
        "north": ["direction"],
        "south": ["direction"],
        "east": ["direction"],
        "west": ["direction"],
        "down": ["direction"],
        "up": ["direction"],
        "down": ["direction"],
        "left": ["direction"],
        "right": ["direction"],
        "back": ["direction"],
        "forward": ["direction"],
        "go": ["verb"],
        "stop": ["verb"],
        "kill": ["verb"],
        "eat": ["verb"],
        "eats": ["verb"],
        "ate": ["verb"],
        "the": ["stop"],
        "in": ["stop"],
        "of": ["stop"],
        "from": ["stop"],
        "at": ["stop"],
        "it": ["stop"],
        "door": ["noun"],
        "bear": ["noun"],
        "princess": ["noun"],
        "cabinet": ["noun"],
        "honey": ["noun"],
    }


    def scan(self, string: str) -> List[Tuple[str, str]]:
        output: List[Tuple[str, str]] = []
        tokens = string.split()
        for token in tokens:
            try:
                output.append(("number", int(token)))
            except ValueError:
                types = Lexicon.lexicon.get(token.lower(), None)
                if types:
                    output.extend([
                        (t, token) for t in types
                    ])
                else:
                    output.append(("error", token))

        return output