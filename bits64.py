# small utilities, no deps

def flatten(xs):
    return [y for x in xs for y in x]

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(list(chunks(range(15), 6)))
