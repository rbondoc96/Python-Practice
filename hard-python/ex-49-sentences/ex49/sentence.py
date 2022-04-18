class Sentence:

    def __init__(self, _subject: str, _verb: str, _object: str):
        self.subject = _subject
        self.verb = _verb
        self.object = _object

    def __str__(self):
        return f"{self.subject} {self.verb} {self.object}"