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


def newton(x0 : float, polinomio : callable, 
           epsilon :float, max_int=100,distancia : float =1):
  start=perf_counter_ns()
  initial_guess=x0
  func=polinomio
  grad=polinomio.deriv(1)
  iterations=0
  while True:
    fval=func(x0)
    fder=grad(x0)
    x1=x0-(fval)/fder
    iterations+=1
    if (iterations>max_int): 
      converged=False
      break
    if (np.abs(x1-x0)<epsilon): 
      converged=True
      break
    x0=x1
  time_interval=perf_counter_ns()-start
  return np.array([x0,func(x0),iterations,time_interval,epsilon,initial_guess,distancia,converged])

def halley(x0 : float, polinomio : callable, epsilon :float, 
           max_int=100, distancia : float =1):
  start=perf_counter_ns()
  iterations=0
  initial_guess=x0
  func=polinomio
  grad=polinomio.deriv(1)
  secondgrad=grad.deriv(1)
  while True:
    fval=func(x0)
    fder=grad(x0)
    fder2=secondgrad(x0)
    newton_step=fval/fder
    x1=x0-newton_step/(1-newton_step*fder2/(2*fder))
    iterations+=1
    if (iterations>max_int):
      converged=False
      break
    if (np.abs(x1-x0)<epsilon):
      converged=True
      break
    x0=x1
  time_interval=perf_counter_ns()-start
  return np.array([x0,func(x0),iterations,time_interval,epsilon,initial_guess,distancia,converged])

