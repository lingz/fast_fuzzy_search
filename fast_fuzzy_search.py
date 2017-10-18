from min_heap import MinHeap
import phonetics
from candidate import Candidate
from generate_candidates import generate_candidates

def next_candidate(candidates):
    if len(candidates) == 0:
        return None
    min_val = 1.6
    best_candidate = None
    for candidate in candidates.values():
        if candidate.score == -1:
            continue # This is blocked
        if candidate.score < min_val:
            best_candidate = candidate
            min_val = candidate.score
    candidates[best_candidate.ipa] = Candidate(-1, None) # Block this key for future
    return best_candidate

def fuzzy_search(word, dictionary, num_results=10):
    results = []
    candidates = {}
    phonetic_variants = phonetics.phoneticize(word)
    print('checking', word, phonetic_variants)
    input('ok?')

    for phonetic in phonetic_variants:
        candidate = Candidate(0, phonetic)
        candidates[candidate.ipa] = candidate

    while (len(candidates) > 0):
        candidate = next_candidate(candidates)

        result = dictionary.get(candidate.ipa)
        if result:
            results.append(result)

        if len(results) == num_results:
            break

        # Cache results to avoid repetitions
        for new_candidate in generate_candidates(candidate):
            prev_candidate = candidates.get(new_candidate.ipa)
            if prev_candidate is None or new_candidate < prev_candidate:
                candidates[new_candidate.ipa] = new_candidate
                print('adding', candidate, new_candidate, prev_candidate)
        # print(candidate.ipa, min_heap._heap)

    return results

import pprint
pp = pprint.PrettyPrinter(indent=4)

import scipy.cluster.hierarchy as hierarchy

CLUSTER_SENSITIVITY = 0.5

def cluster_phones(language):
    phone_set = phonetics.phone_set(language)
    vowels = list(filter(lambda x: phonetics.is_vowel(x), phone_set))
    consonants = list(filter(lambda x: phonetics.is_vowel(x), phone_set))

    phones = sorted(list(phonetics.phone_set(language)))
    triangle_distance = []

    for a in range(len(phones)):
        for b in range(a + 1, len(phones)):
            triangle_distance.append(phonetics.distance(phones[a], phones[b]))

    linkages = hierarchy.linkage(triangle_distance)
    clusters = hierarchy.fcluster(linkages, CLUSTER_SENSITIVITY)

    forward_map = {}
    cluster_map = {}

    for index in range(len(clusters)):
        set_phones = forward_map.get(clusters[index])
        if not set_phones:
            set_phones = []
            forward_map[clusters[index]] = set_phones
        set_phones.append(phones[index])
        cluster_map[phones[index]] = clusters[index]

    # To see the map
    pp.pprint(forward_map)
    print(len(phones))

    return cluster_map
