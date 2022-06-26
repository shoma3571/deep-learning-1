import numpy as np

def softmax(a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  return exp_a / sum_exp_a

A = np.array([1.0, 2.0, 3.0])
print(softmax(A))