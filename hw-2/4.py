#4 еще не доделанный
def get_most_frequent(words, k):
  w = set(words)
  w = list(w)
  c = []
  result = []
  for i in w:
    kol = 0
    for j in range(len(words)):
      if i == words[j]:
        kol += 1
    c.append(kol)
  while k != 0:
    nom = c.index(max(c))
    result.append(w[nom])
    w.remove(w[nom])
    c.remove(c[nom])
    k -= 1
  return result
get_most_frequent(["hello", "world", "hello", "my", "dear", "world", "hello"], 3)