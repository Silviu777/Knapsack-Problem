import numpy as np
import matplotlib.pyplot as grafic

# takes float values from a text file in which every value is written on a line
def read(fis):
    c = np.genfromtxt(fis)
    return c


# checks the feasibility of the x choice and determines the objective function
def ok(x,n,c,v,max):
    val = 0
    cost = 0
    for i in range(n):
        val=val+x[i]*v[i]
        cost=cost+x[i]*c[i]
    return cost<=max,val

# creates the graphical representation of the population to highlight the variability
def rep_pop(pop,dim,n):
    x=[i for i in range(dim)]
    y=[pop[i][n] for i in range(dim)]
    grafic.plot(x,y,"gs-",markersize=12)

# generates the initial population
# I:
# fc, fv - Cost and Values text files
# max - maximum capacity
# dim - number of individuals in the population
# E: pop - initial population

def gen(fc,fv,max,dim):
    
    # reads the Cost and Values text files
    c = read(fc)
    v = read(fv)
    # n - length of the problem
    
    n = len(c)
    # considers the population as a list of elements - n+1 individuals lists
    
    pop = []
    for i in range(dim):
        ready = False
        while ready == False: 
        # generates the x candidate with elemets 0,1
        
            x = np.random.randint(0,2,n)
            read,val = ok(x,n,c,v,max)
    
        x = list(x)
       
        x = x + [val]
       
        pop = pop + [x]
        
    rep_pop(pop, dim, n)
    
    return pop



