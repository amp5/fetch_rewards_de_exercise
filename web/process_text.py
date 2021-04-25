class TextAnalysis():

    def similarity_score(self, txt1, txt2):
        '''Takes in two texts and computes 
        similarity - how many words they have in common '''

        if not isinstance(txt1, str) or not isinstance(txt2, str):
            raise TypeError("Both inputs must be strings")

        # If both inputs are the exact same return score of 1
        if txt1 == txt2:
            return 1.0

        # Tokenizes string inputs to cleaned words and creates 
        # a set of unique words found in each input text
        uniq1 = set(self.tokenize(txt1))
        uniq2 = set(self.tokenize(txt2))

        return self.jaccard_index(uniq1, uniq2)


    def remove_punc(self, txt):
        '''Removes any non-space punctuation'''
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in txt:
            if char in punc:
                txt = txt.replace(char, "")
        return txt

    def tokenize(self, txt):
        '''Takes a string as an input, removes punctuation, ensures text
        is lowercase and returns list of words'''
        return self.remove_punc(txt).lower().split()

    # Created this as a function to enable ease of choosing a different  
    # algorithm to calculate similarity
    def jaccard_index(self, set1, set2):
        '''Takes two sets of unique words and calculates jaccard index score =
        number of unique words found in both sets divided by the total number of
        unique words total'''
        score = float(len(set1.intersection(set2))/len(set1.union(set2)))
        return round(score, 2)


