import sys

Values1 = []
Values2 = []

Ranks1 = {}
Ranks2 = {}

for line in open(sys.argv[1],'r'):
    (word1, word2, value) = line.split()
    Values1.append((value, (word1, word2)))

for line in open(sys.argv[2],'r'):
    (word1, word2, value) = line.split()
    Values2.append((value, (word1, word2)))

Values1 = sorted(Values1)
Values2 = sorted(Values2)

for i, x in enumerate(Values1):
    value, pair = x
    Ranks1[pair]=i

for i, x in enumerate(Values2):
    value, pair = x
    Ranks2[pair]=i

n = len(Ranks1.keys())

rhosum = 0.0

for pair in Ranks1.keys():
    rhosum += (Ranks1[pair] - Ranks2[pair])**2

rho = 1.0 - 6*rhosum/(n*(n**2-1))

print rho
