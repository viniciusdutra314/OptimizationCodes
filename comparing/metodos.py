import numpy as np
from numpy.random import random
from time import perf_counter_ns

def gerar_raizes(grau : int,tipo :str) -> list:
  raizes=[]
  if tipo=="diferentes":
    for _ in range(grau):
      raizes.append(random())
  if tipo=="iguais":
    raiz=random()
    for _ in range(grau):
      raizes.append(raiz)
  return raizes


def newton(x0 : float, func : callable, grad : callable, epsilon :float, max_int=100):
  initial_guess=x0
  iterations=0
  start=perf_counter_ns()
  while (abs(func(x0)) >abs(epsilon) and iterations < max_int):
    x0=x0-(func(x0)/grad(x0))
    iterations+=1
  time_interval=perf_counter_ns()-start
  return np.array([x0,func(x0),iterations,time_interval,epsilon,initial_guess])

def halley(x0 : float, func : callable, grad : callable, secondgrad : callable,
epsilon :float, max_int=100):
  iterations=0
  initial_guess=x0
  start=perf_counter_ns()
  while abs(func(x0)) >abs(epsilon) and iterations < max_int:
    newton_term=func(x0) / grad(x0)
    halley_term=(1-(secondgrad(x0)*func(x0))/(2*grad(x0)**2))
    x0=x0-newton_term/halley_term
    iterations+=1
  time_interval=perf_counter_ns()-start
  return np.array([x0,func(x0),iterations,time_interval,epsilon,initial_guess])
