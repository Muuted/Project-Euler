
import time


n = 20

max_col = False
max_row = False

num_paths = 0
num_tries = 100
row = 0
col = 0
last_row =0
last_col =0

a = time.time()
running = True
while running:

    # The col logic
    if max_col == False:
        col += 1

    if col >= n:
        max_col = True

    # The row logic
    if max_col == True:
        row += 1
        if max_row == False:
            max_col = False 

    
    
    # Reset logic
    if (col >= n) and (row >= n):
        num_paths += 1
        row = 0
        col = 0

    # End logic
    b = time.time()
    if (b-a)/60 >0.1:
        running = False
        print('done')

