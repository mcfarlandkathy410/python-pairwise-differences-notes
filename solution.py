

def solve(value):
    return [b-a for a, b in zip(value, value[1:])]
