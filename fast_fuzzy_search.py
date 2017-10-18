import pyphone
from generate_candidates import generate_candidates

def fast_fuzzy_search(word, dictionary, num_results=10, max_distance=2):
    results = []
    current_candidates = pyphone.phonex(word)
    next_candidates = []
    for i in range(max_distance):
        for candidate in current_candidates:
            if dictionary.get(candidate):
                results.append(dictionary.get(candidate))
            if len(results) == num_results:
                return results
            for new_candidate in generate_candidates(candidate):
                next_candidates.append(new_candidate)
        current_candidates = next_candidates
        next_candidates = []
    return results
