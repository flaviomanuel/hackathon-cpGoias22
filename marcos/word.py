class Word:

    def __init__(self, dict):
        self.conf = dict["conf"]
        self.end = dict["end"]
        self.start = dict["start"]
        self.word = dict["word"]

    def to_string(self):
        return "{:41} from {:.2f} sec to {:.2f} sec, confidence is {:.2f}%".format(self.word, self.start, self.end, self.conf*100)