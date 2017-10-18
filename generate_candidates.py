from candidate import Candidate
import phonetics


PHONE_THRESHOLD = 0.3

def generate_candidates(candidate, max_score=1.0, language="english"):
    candidates = []
    phones = phonetics.phone_set(language)

    for position in range(len(candidate.ipa)):
        current_phone = candidate.ipa[position]
        # Deletion Edits
        cost = 0.5 if phonetics.is_vowel(current_phone) else 0.5
        new_candidate = Candidate(candidate.score + cost, candidate.ipa[:position] + candidate.ipa[position + 1:])
        candidates.append(new_candidate)

        for phone in phones:
            # Insertion edits before the current_phone
            cost = 0.5 if phonetics.is_vowel(phone) else 0.5
            new_candidate = Candidate(candidate.score + cost, candidate.ipa[:position] + (phone,) + candidate.ipa[position:])
            candidates.append(new_candidate)
            
            # Substitution edits
            cost = phonetics.distance(current_phone, phone)
            if cost > 0.3:
                continue
            new_candidate = Candidate(candidate.score + cost, candidate.ipa[:position] + (phone,) + candidate.ipa[position + 1:])
            candidates.append(new_candidate)

    return filter(lambda x: x.score <= max_score, candidates)
