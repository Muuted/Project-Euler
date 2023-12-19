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
            


    if printstate == True:
        print("")
        for obj in path_list:    
            print(obj)

    return path_list, done




path_list = [
    [(0,0)]
    ]

n = 2
finished = False
print_it = False
for _ in range(2*n):
    new_pathlist, finished = branch_func(n,path_list,printstate=print_it)[0], branch_func(n,path_list,printstate=False)[1]
    path_list = new_pathlist.copy()
    if finished == True:
        print('We have the Final result:')
        print('number of paths =',len(path_list))
        break

sum = 0
temp1 = path_list.copy()
temp2 = path_list.copy()

for i in range(len(temp1[0])):
    for j in range(i,len(temp1[0])):
        if (i != j) and (temp1[i] == temp2[j]):
            path_list.pop(j)
            sum += 1


for obj in path_list:    
        print(obj)
print("len=",len(path_list))
print("sum=",sum)


#print(path_list)
#print(path_list[7][:])