def draw_line(size, lines ):

    # Create an n by n matrix
    hold = [[0 for _ in range(size)] for _ in range(size)]
    
    # if sum(hold) >= 16:
    #     print(hold)
    #     exit()

    line = [1,2]
    for el in line:
        for row in range(size):
            for col in range(size):
                
                if col == 0 and row == 0:
                    hold[0][0] = el

                else:
                    hold[row][col] = el
                    if confirm_validity(hold, row, col):
                        continue
                    else:
                        if el == 1:
                            hold[row][col] = 2
                        elif el == 2:
                            hold[row][col] = 1

                        
                        if confirm_validity(hold, row, col):
                            continue
                        else:
                            hold[row][col] = 0

        print(hold)

def confirm_validity(hold, row, col):

    if row == 0:
        if hold[row][col-1] + hold[row][col] == 3:
            return False
        return True
    
    if col == 0:
        if hold[row-1][col] + hold[row][col] == 3:
            return False
        if hold[row-1][col+1] + hold[row][col] == 2:
            return False
        return True
    
    if col == len(hold)-1 and row != 0:
        #Look previous
        if hold[row][col-1] + hold[row][col] == 3:
            return False
        #Look above
        if hold[row-1][col] + hold[row][col] == 3:
            return False
        #Look above to the left
        if hold[row-1][col-1]  +  hold[row][col] == 4:
            return False
        return True
    
    else:
        #Look previous
        if hold[row][col-1] + hold[row][col] == 3:
            return False
        #Look above
        if hold[row-1][col] + hold[row][col] == 3:
            return False
        #Look above to the right
        if hold[row-1][col+1] + hold[row][col]  == 2 and hold[row][col] != 0:
            return False
        #Look above to the left
        if hold[row-1][col-1]  +  hold[row][col] == 4:
            return False
        return True



hold = draw_line(4,2)

print(hold)
