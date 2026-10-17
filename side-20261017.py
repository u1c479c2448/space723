"""Scratch module."""

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def flatten(xs):
    return [y for x in xs for y in x]

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(most_common("abracadabra"))
