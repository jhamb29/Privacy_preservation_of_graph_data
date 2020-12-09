# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:00:14 2020

"""
import igraph

from igraph import *
g = Graph()



g.add_vertices(20)
print(g)


g.add_edges([(0,1),(0,9),(0,11),(0,12),(1,2),(2,3),(3,4),(3,5),(5,6),(7,6),(7,5),(1,7),(1,8),(8,18),(17,18),(9
             ,17),(10,17),(19,17),(16,17),(16,19),(11,10),(11,12),(15,13),(14,15),(14,13)]) 
print(g)

layout = g.layout_kamada_kawai()
layout = g.layout("kamada_kawai")
print(layout)
layout = g.layout("kk")
plot(g, layout = layout)


g.average_path_length()


g.transitivity_undirected()


g.degree()

lst = []

g.vcount()

v1=g.vcount() 

for x in range(g.vcount()):
  c=0    
  for y in range(0,g.vcount()):
      if g.degree(x)==g.degree(y) :
          c = c+1                
  if c==1 :
      lst.append(x)


print(lst)
z=g.maxdegree()

 # type(g.degree(4))


if len(lst)==1:
    if g.degree(lst[0]) < z:
        t1 = z-g.degree(lst[0]) 
        g.add_vertices(t1)
        for j in range(v1,g.vcount()):
                g.add_edges([(lst[0],j)]) 
        
    else:
        minn1=10000000000
        minn2=0
        for i in range(0,g.vcount()):
            if lst[0]!=i :
                if g.degree(lst[0]) - g.degree(i) < minn1:
                    minn1 = g.degree(lst[0]) - g.degree(i)  
                    minn2 = g.degree(i)
               
                
                
             
        for i in range(0,g.vcount()):
            if g.degree(i)==minn2 :
                t2 = z - g.degree(i)
                g.add_vertices(t2)    
                for j in range(v1,g.vcount()): 
                      g.add_edges([(i,j)]) 
                v1=g.vcount() 
            
            
            
   
else:
    maxx_degree = 0
    for i in range(0,len(lst)):
        if maxx_degree < g.degree(lst[i]):
            maxx_degree = g.degree(lst[i]) 
    print(maxx_degree)
    
    for i in range(0,len(lst)):
        if g.degree(lst[i])!=maxx_degree :
            t = maxx_degree - g.degree(lst[i])
            g.add_vertices(t)
            for j in range(v1,g.vcount()):
                g.add_edges([(lst[i],j)]) 
            v1=g.vcount()        
 
    
print(g)

g.degree()


layout = g.layout_kamada_kawai()
layout = g.layout("kamada_kawai")
print(layout)
layout = g.layout("kk")
plot(g, layout = layout)