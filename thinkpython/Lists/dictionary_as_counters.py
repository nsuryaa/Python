def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontosaurus')
print(h)
i = histogram('a')
print(i)

print(h.get('a',0))
print(h.get('b',0))