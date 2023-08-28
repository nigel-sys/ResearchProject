# -*- coding: utf-8 -*-
"""Copy of mealpy_ga.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VzCwlJm_QC50Lr4pGXefnNTD_5V_fiP4
"""

pip install mealpy mealpy==2.5.1

from mealpy.evolutionary_based.GA import BaseGA
from mealpy.swarm_based import GWO
import json 
import time

def Fun(solution):
  list1 = [0] * data['vmcount'][0]
  val = 0.0
  #print(solution)
  #print(int(round(solution[0])))
  for i in range(solution.size):
    solution[i]=round(solution[i])
    if(round(solution[i])!=0.0):
      list1[int(round(solution[i]))-1]=list1[int(round(solution[i]))-1] + data['task'][0]/data['VM'][int(round(solution[i]))-1] 
    else:
      list1[int(round(solution[i]))]=list1[int(round(solution[i]))-1] + data['task'][0]/data['VM'][int(round(solution[i]))] 
  #print(solution)
  return max(list1) 
    
start_time = time.time()

f = open('data.json') 
data = json.load(f)  
tcount=data['tcount']
size=data['tcount'][0]
vmcount= data['vmcount'][0]

problem_dict1 = {
    "fit_func": Fun,
    "lb": [0 for i in range(size)] ,
    "ub": [vmcount-1 for i in range(size)],
    "minmax": "min",
    "verbose": True,
}
model1 = BaseGA( epoch=10, pop_size=100, pc=0.9, pm=0.05)
best_position, best_fitness = model1.solve(problem_dict1)
print(f"Solution: {best_position}, Fitness: {best_fitness}")

s=[round(num,0) for num in best_position]
print(s)

#s=np.round(best_position,0)
p={}

exetime= time.time() - start_time
print(s)
data1 = {"name": s, "exetime": str(exetime)}

print(data1)

with open("sample.json", "w") as outfile:
    json.dump(data1, outfile)

