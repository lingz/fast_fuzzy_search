class Candidate:
    def __init__(self, score, ipa):
        self.score = score
        self.ipa = ipa


    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return '(' + str(self.score) + ', ' + str(self.ipa) + ')'
