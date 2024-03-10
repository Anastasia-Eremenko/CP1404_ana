words = "hi there mum".split()
print(words)
print(max(len(word) for word in words))
print([])

string = "name=bob&age=99&day=wed"
pairs = string.split("&")
result = [tuple(pair.split("=")) for pair in pairs]
print(result)