"""This is the entry point of the program."""


def create_box(height, width, character):
    if height >= 1 and width >=1:
        box = ""
    
        for i in range(height):
            for j in range(width):
                box += character
            box += "\n"
    else:
        return "Oops! Need higher values for height and/or width."
        
    return box


def create_empty_box(height, width, character):
    if height >= 1 and width >=1:
        box = ""
        
        for i in range(height):
            empty_string = ''
            for j in range(width):
                if i == 0 or i  == (height - 1) or j == 0 or j == (width -1):
                    empty_string += character
                else:
                  empty_string += ' '
            box += (empty_string)
            box += "\n"
            
            
    else:
        return "Oops! Need higher values for height and/or width."
        
    return box

                      
"""
#Alternative Solutions 1:

def outline_box(height, width, character):
    return (character * width +' \n') + (character + ' '*(width-2) + character +'\n')*(height-2) + (character * width)
"""

#Alternative Solution 2:
"""
def outline_box(height, width, character):
    full_row = character * width
    edge_row = character + ' '*(width-2) + character
    interior = ''
    
    if height < 1 or width < 1:
        return 'Error'
    for x in range(1, height-1):
        interior += edge_row+'\n'
    
    box = (full_row+'\n') + (interior) + (full_row)
    
    return box
"""    
    
if __name__ == '__main__':
    #print(create_box(3, 4, '*'))
    print(create_empty_box(3,4,'*'))
