def Test():
  print("Test: starting")
  for i in range(10000000): pass
  print("Test: finishing")

def Lint():
  print("Lint: starting")
  for i in range(100000000): pass
  print("Lint: finishing")

def Coverage():
  print("Coverage: starting")
  for i in range(1000000000): pass #raise Exception("Sorry, an error here")
  print("Coverage: finishing")

def Docs():
  print("Docs: starting")
  for i in range(10000000): pass
  print("Docs: finishing")

def Benchmark():
  print("Benchmark: starting")
  for i in range(100000000): pass
  print("Benchmark: finishing")