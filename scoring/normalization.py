def min_max_normalize(value, min_val, max_val):
    if value is None:
        return 50
    return max(0, min(100, ((value - min_val) / (max_val - min_val)) * 100))


def reverse_normalize(value, min_val, max_val):
    if value is None:
        return 50
    score = ((value - min_val) / (max_val - min_val)) * 100
    return max(0, min(100, 100 - score))
