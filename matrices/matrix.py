import sys
sys.path.append("..")

from vectors import vector

def sum(m1, m2):
    return [vector.plus(m1[i], m2[i]) for i in range(len(m1))]
