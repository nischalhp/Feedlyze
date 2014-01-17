#every thread can have an object of its own based on the answers it sends

class TextAnalyticsObj:

    sentences = []
    tokens = []
    postags = []
    chunks = []

    def __init__(self,sentences,tokens,postags,chunks):
        self.sentences = sentences
        self.tokens = tokens
        self.postags = postags
        self.chunks = chunks

    

