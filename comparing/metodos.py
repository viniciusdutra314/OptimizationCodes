import numpy as np
from numpy.random import random
from time import perf_counter_ns

def gerar_raizes(grau : int,tipo :str,distancia : float =1) -> list:
  raizes=[]
  if tipo=="diferentes":
    for _ in range(grau):
      raizes.append(distancia*random())
  if tipo=="iguais":
    raiz=distancia*random()
    for _ in range(grau):
      raizes.append(raiz)
  return raizes


def newton(x0 : float, func : callable, grad : callable, 
           epsilon :float, max_int=100,distancia : float =1):
  initial_guess=x0
  iterations=0
  start=perf_counter_ns()
  while True:
    x1=x0-(func(x0)/grad(x0))
    iterations+=1
    if (iterations>max_int): break
    if (np.abs(x1-x0)<epsilon): break
    x0=x1
  time_interval=perf_counter_ns()-start
  return np.array([x0,func(x0),iterations,time_interval,epsilon,initial_guess,distancia])

def halley(x0 : float, func : callable, grad : callable, secondgrad : callable,
epsilon :float, max_int=100, distancia : float =1):
  iterations=0
  initial_guess=x0
  start=perf_counter_ns()
  while True:
    x1=x0-(func(x0)/grad(x0))/(1-(secondgrad(x0)*func(x0))/(2*grad(x0)**2))
    iterations+=1
    if (iterations>max_int):break
    if (np.abs(x1-x0)<epsilon):break
    x0=x1
  time_interval=perf_counter_ns()-start
  return np.array([x0,func(x0),iterations,time_interval,epsilon,initial_guess,distancia])
