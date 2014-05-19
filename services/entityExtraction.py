class EntityExtractor:
    

    ###### ENTITY EXTRACTOR ##########
    chunks = []
    entities = []

    def __init__(self,chunks):
        self.chunks = chunks
        self.entities = []


    def entityExtraction(self):
        #find entites
        for tree in self.chunks:
            #print tree,"tree"
            self.extractEntities(tree)       
        print list(set(self.entities))
        return self.entities

    def extractEntities(self,tree):
       
        if hasattr(tree, 'node') and tree.node:
            #print tree.node,"tree node"
            if tree.node == 'NE':
                #print tree
                for child in tree:
                    self.entities.append(' '.join([child[0] for child in tree]))
                    #print child,"child"
            else:
                for child in tree:
                    #print child,"recursive child"
                    self.extractEntities(child)
