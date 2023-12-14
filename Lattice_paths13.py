
import time


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
    if ((b-a)/60 >0.1):
        running = False
        print('done')
    
        

    
print('num paths = ',num_paths)