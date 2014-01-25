#every thread can have an object of its own based on the answers it sends

class TextAnalyticsObj:

    question = ""
    answer = ""
    sentences = []
    tokens = []
    postags = []
    chunks = []

    def __init__(self,question,answers,sentences,tokens,postags,chunks):
        self.question = question
        self.answers = answers
        self.sentences = sentences
        self.tokens = tokens
        self.postags = postags
        self.chunks = chunks

    

