import operator


def levenshtein(source, target, align=False):
    """
    Return minimum edit distance
    source -- source string
    target -- target string
    if align=True, initial and final deletes (on source) are free
    Returns: edit distance (int)
    """
    # Get lengths of source and target
    n, m = len(source), len(target)
    # Create "matrix"
    d = []
    for i in range(n + 1):
        d.append((m + 1) * [None])
    # For the oracles
    # Initialize "matrix"
    d[0][0] = 0
    for i in range(1, n + 1):
        if align:
            d[i][0] = 0
        else:
            d[i][0] = d[i - 1][0] + 1
    for j in range(1, m + 1):
        d[0][j] = d[0][j - 1] + 1
    # Recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if align and j == m:
                del_cost_inc = 0
            else:
                del_cost_inc = 1
            possibilities = [
                d[i - 1][j] + del_cost_inc,
                d[i - 1][j - 1] + 1,
                d[i][j - 1] + 1,
            ]
            min_index, min_value = argmin(possibilities)
            d[i][j] = min_value
    return d[n][m]


def argmin(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return min_index, min_value
