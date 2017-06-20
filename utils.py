
def merge(a, b):
  result = {}
  for key, value in a.items():
    result[key] = value

  for key, value in b.items():
    result[key] = value

  return result
