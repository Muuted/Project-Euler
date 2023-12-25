import time
import random 
from cProfile import Profile 
from pstats import SortKey, Stats

def branch_func(n,path_list,printstate) -> list:
    done = False
    N = len(path_list)
    for i in range(N):
        lx = path_list[i][len(path_list[i])-1][0] # last x val
        ly = path_list[i][len(path_list[i])-1][1] # last y val

        if lx + ly >= 2*n: # we have reached the right bottom corner.
            done = True
            print('we finished, num of paths:',len(path_list))
            break

        if lx + ly < 2*n:
            temp = path_list[i].copy()
            #print(lx+ly,2*n)
            nx, ny = lx ,ly

            # Not reached boundary
            if lx < n:
                nx = lx + 1
            if ly < n:
                ny = ly + 1

            # Reached Boundary
            if lx >= n and ly < n:
                ly = ly + 1
            if ly >= n and lx < n:
                lx = lx + 1


            if lx > n: # check if we exceede the allowed limit
                print('lx>=n','lx=',lx,'ly=',ly)
            if ly > n:
                print('ly>=n','lx=',lx,'ly=',ly)

            # new tuples
            horiz = ( nx , ly )
            verti = ( lx , ny )
 
            temp.append(verti) # appends to the copy
            path_list[i].append(horiz) # appends to where we stand
            path_list.append(temp) # makes the copy + new pos, a new list 
            
    #path_list = prune_list(path_list)


    if printstate == True:
        print("")
        for obj in path_list:    
            print(obj)

    return path_list, done


def prune_list(lists)->list: 
    result1 = []
    for i in lists:
        if i not in result1:
            result1.append(i)
    
    result = []
    for j in range(len(result1)):
        x = result1[j][len(result1[j])-1][0] # last x val
        y = result1[j][len(result1[j])-1][1] # last y val
        result.append([(x,y)])
    #print("result:",result)
    return result1

def first_try(n):
        
    path_list = [
        [(0,0)]
        ]

    #n = 2
    finished = False
    print_it = False
    time1 = time.time()
    for _ in range(2*n + 1):
        time2 = time.time()
        print(f"we are at iteration:{_} and it took {(time2-time1)/60} min")
        #new_
        path_list, finished = branch_func(n,path_list,printstate=print_it)
        
        #path_list = prune_list(path_list)
        #path_list = new_pathlist.copy()

    path_list = prune_list(path_list)
    print(f'We have the Final result, it took {(time.time()-time1)/60}min')
    print('number of paths =',len(path_list))
    
    print("len=",len(path_list))
    #print(path_list)
    return 0
"""

with Profile() as profile:
    print(f"{first_try() = }")
    (
        Stats(profile)
        .strip_dirs()
        .sort_stats(SortKey.CALLS)
        .print_stats()
)
"""


def second_try(n,path_list):
    temp_list = []
    for i in range(len(path_list)):

        if path_list[i][0] < n: # x pos
            path_list[i][0] += 1

        if path_list[i][1] < n: # y pos
            pos2 = [ path_list[i][0] , path_list[i][1]+1 ]
            temp_list.append(pos2)
        
        if path_list[i][1] >= n or path_list[i][0] >= n:

            if path_list[i][0] >= n and path_list[i][1]+1 < n+1:
                path_list[i][1] += 1
                
            if path_list[i][1] >= n and path_list[i][0]+1 < n+1:
                path_list[i][0] += 1
            

    
    for x in temp_list:
        path_list.append(x)

    return path_list

"""
path_list = [ [0,0] ]
grit_size = 3
num_steps = 2*grit_size
time1 = time.time()
print(" ")
print(len(path_list))
print(path_list)

for step in range(num_steps):
    time2 = time.time()
    print("we are at i=",step, "  it took: ",(time2-time1)/60,"min")
    path_list = second_try(
        n=grit_size
        ,path_list=path_list
        )
    print(" ")
    print(len(path_list))
    print(path_list)

print("the lenght:",len(path_list))"""
#print("The list: ",path_list) 

#first_try(n=3)

from scipy.special import binom, comb
n = 20
x,y = 2*n,n
paths = comb(x,y,exact=True)
print(paths)