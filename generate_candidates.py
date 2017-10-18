import pyphone

def generate_candidates(candidate, language="english"):
    candidates = []
    phones = set(pyphone.cluster_phones(language).values())
    for position in range(len(candidate)):
        # Deletion deletes the current phone edits before the current_phone
        candidates.append(candidate[:position] + candidate[position + 1:])
        for phone in phones:
            # Insertion edits before the current_phone
            candidates.append(candidate[:position] + (phone,) + candidate[position:])
    return candidates
