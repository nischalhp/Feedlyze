from Model import Model


class StatisticsFinder:

    def __init__(self):
        print "Constructor"


    def getTfidf(self,tokensList):
        # this holds meaning keeping in consideration that 
        # the number of responses are in thousands
        # collate all the answers to a question
        # remove stop words
        # build the statistics for a question
        tf_table = {}
        stopWords = 'a about above after again against all am an and any are aren\'t as at be because been before being below between both but by can\'t cannot could couldn\'t did didn\'t do does doesn\'t doing don\'t down during each few for from further had hadn\'t has hasn\'t have haven\'t having he he\'d he\'ll he\'s her here here\'s hers herself him himself his how how\'s i i\'d i\'ll i\'m i\'ve if in into is isn\'t it it\'s its itself let\'s me more most mustn\'t my myself no nor not of off on once only or other ought our ours ourselves out over own same shan\'t she she\'d she\'ll she\'s should shouldn\'t so some such than that that\'s the their theirs them themselves then there there\'s these they they\'d they\'ll they\'re they\'ve this those through to too under until up very was wasn\'t we we\'d we\'ll we\'re we\'ve were weren\'t what what\'s when when\'s where where\'s which while who who\'s whom why why\'s with won\'t would wouldn\'t you you\'d you\'ll you\'re you\'ve your yours yourself yourselves'
        stopWordsList = list(stopWords)
        # tokenList is a list of token lists
        # we need token from token lists
        for tokens in tokensList:
            for token in tokens:
                if str(token) in stopWordsList:
                    continue
                else:
                    if token in tf_table.keys():
                        value = tf_table[token]
                        value += 1
                        del tf_table[token]
                        tf_table[token] = value
                    else:
                        tf_table[token] = 1
        return tf_table




