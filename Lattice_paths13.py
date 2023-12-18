
import time
import random 

"""
n = 3 # 2x2 lattice

max_col = False
max_row = False

num_paths = 0
num_tries = 100
row = 0
col = 0
last_row =0
last_col = n

a = time.time()

running = True
while running:
    if col == 0:
        print(f'path:({row},{col})')

    # The col logic
    if max_col == False and col < n:
        col += 1
        print(f'path:({row},{col})')

    if col >= last_col:
        max_col = True

    # The row logic
    if max_col == True and row <= n:
        row += 1
        print(f'path:({row},{col})')
        if max_row == False:
            pass #max_col = False 

    
   
    # Reset logic
    if (col >= n) and (row >= n):
        num_paths += 1
        row = 0
        col = 0
        last_col -= 1
        print('last_col:',last_col)

    # End logic
    if last_col <=0 :
        running = False
        
    b = time.time()
    if ((b-a)/60 >0.01):
        running = False
        print('done') 
print('num paths = ',num_paths)        
"""



#testing getting new paths
"""
temp = path_list[0].copy()
path_list[0].append((0,1))
path_list.append(temp)
path_list[len(path_list)-1].append((1,0))

for obj in path_list:    
    print(obj)
print('\n')
"""



"""
class Lattice_paths:
    def __init__(self,n) -> None:
        self.s = n
        #self.paths = [[(0,0)]]


    def branch_func() -> list:
        n = self.size
        path_list = self.paths
        for i in range(len(path_list)):
            temp = path_list[i].copy()

            lx = path_list[i][len(path_list[i])-1][0] # last x val
            ly = path_list[i][len(path_list[i])-1][1] # last y val
            nx, ny = lx ,ly

            if lx <= n:
                nx += 1
            if ly <= n:
                ny += 1

            # new tuples
            horiz = ( nx , ly )
            verti = ( lx , ny )
            #print(horiz)
            path_list[i].append(horiz)
            temp.append(verti)
            path_list.append(temp)

        for obj in path_list:    
            print(obj)

        return path_list
    
    def run(s):
        print("HIIIIIIIIIIIIIIIIIII",self.s)
        for _ in range(6):
            print(self.size)
            print('New paths')
            new_pathlist = branch_func(path_list)
            path_list = new_pathlist.copy()
            print('\n')
            print(len(path_list))
"""


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

            print("horiz:",horiz,"\n","verti:",verti)
            path_list[i].append(horiz) # appends to where we stand
            print("pathlist:",path_list)
            
            temp = path_list[i].copy()
            temp.append(verti) # appends to the copy
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
for _ in range(10*n):
    new_pathlist, finished = branch_func(n,path_list,printstate=True)[0], branch_func(n,path_list,printstate=False)[1]
    path_list = new_pathlist.copy()
    if finished == True:
        print('We have the Final result:')
        print('number of paths =',len(path_list))
        break

#print(path_list)