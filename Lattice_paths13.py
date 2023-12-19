import time
import random 


def branch_func(n,path_list,printstate) -> list:
    done = False
    for i in range(len(path_list)):
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


def remove_prior(lists)->list:
    print("list:",lists)
    temp = []
    for i in range(len(lists)):
        x = lists[i][len(lists[i])-1][0]
        y = lists[i][len(lists[i])-1][1]
        temp.append([(x,y)])        
    print("temp=",temp)
    return temp

def prune_list(lists)->list: 
    result = []
    for i in lists:
        if i not in result:
            result.append(i)
    return result
path_list = [
    [(0,0)]
    ]

n = 2
finished = False
print_it = False
time1 = time.time()
for _ in range(2*n):
    
    time2 = time.time()
    print(f"we are at iteration:{_} and it took {(time2-time1)/60} min")
    #new_
    path_list, finished = branch_func(n,path_list,printstate=print_it)
    #new_pathlist = prune_list(new_pathlist)
    #path_list = new_pathlist.copy()
    if finished == True:
        print('We have the Final result:')
        print('number of paths =',len(path_list))
        break
path_list = prune_list(path_list)
print("len=",len(path_list))

 