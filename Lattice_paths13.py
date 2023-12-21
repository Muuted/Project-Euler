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

def first_try():
        
    path_list = [
        [(0,0)]
        ]

    n = 2
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
    
    list_len = len(path_list)
    print(path_list) 
    for i in range(list_len):
        x = path_list[i][0] # x val
        y = path_list[i][1] # y val
        
        # dealing with horizontal movement
        if x < n:
            path_list[i][0] += 1
        """
        if x >= n and y < n:
            path_list[i][1] += 1
        """
        
        #dealing with vertical movement
        if y < n:
            pos2 = [ x , y+1 ]
            path_list.append(pos2)
        """
        if y >= n and x < n:
            pos2 = [ x+1 , y ]
            path_list.append(pos2)
        """
        if y >= n or x >= n:
            if x >= n:
                path_list[i][1] +=1
                
            if y >= n:
                path_list[i][0] +=1
                
    

    
    return path_list


path_list = [ [0,0] ]
N=3
for i in range(N+1):
    print(len(path_list))
    path_list = second_try(n=2,path_list=path_list)

print(len(path_list))
print(path_list) 

#first_try()
