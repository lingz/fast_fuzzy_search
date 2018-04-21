import pyphone
from levenshtein import levenshtein
from collections import namedtuple


Result = namedtuple('Result', ['id', 'term', 'score'])


class FastFuzzySearch:
    def __init__(self, options={}):
        self.index = {}  # phone_sequences -> set of matching ids
        self.library = {}  # id -> original term
        self.options = options
        self.options.setdefault('language', 'english')

    def add_term(self, term, id):
        """
        Adds a term corresponding to id to the FastFuzzySearch index
        """
        self.library[id] = term
        words = term.split(' ')
        for word in words:
            variants = self.generate_phonetic_variants(word)
            for variant in variants:
                if variant:
                    ids = self.index.setdefault(variant, set())
                    ids.add(id)

    def search(self, query, n_results=10):
        """
        Searches in the index for all terms that might fuzzy match onto the
        query.  Scores and ranks the results and returns up to the top
        n_results.

        Returns: a list of Result(id, term, score) that will have length up to
        n_results
        """
        query_words = query.split(' ')
        res_sets = map(query_words, self.ids_for_query_word)
        common_ids = set.intersection(*res_sets)
        candidates = map(common_ids, lambda id: self.score_for_id(id, query))
        ranked_candidates = sorted(candidates, key=lambda res: res.score)
        return ranked_candidates[:n_results]

    def generate_phonetic_variants(self, word):
        """
        Returns a list of the phonetic seq itself and all variations missing 1
        character. i.e:

        Input: 'Word'
        Phonetic: [a, b, c]
        Output: [
            [a, b, c],
            [a, b],
            [a, c],
            [b, c],
        ]
        """
        res = []
        phonexes = pyphone.phonex(word, language=self.options['language'])
        for phonex in phonexes:
            res.append(phonex)
            for i in range(len(phonex)):
                res.append(phonex[:i] + phonex[i + 1:])
        return res

    def score_for_id(self, id, query):
        """
        Given a termId, returns the scored Result object
        """
        term = self.index.get(id)
        score = levenshtein(query, term, align=True)
        return Result(id, term, score)

    def ids_for_query_word(self, query_word):
        """
        Returns a set of all ids that match this query_word
        """
        variants = self.generate_phonetic_variants(query_word)
        res_sets = map(lambda variant: self.index.get(variant), variants)
        return set.union(filter(None.__ne__, res_sets))
