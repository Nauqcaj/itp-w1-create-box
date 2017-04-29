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

                        #######
                        #NOTES#
                        #######
"""
Originally had the variable 'empty_string' in same name scope as variable 'name'.
That didn't work. 
I moved it under the first 'for loop' scope. It worked, but I'm not entirely sure why.
"""
"""
Under the second for statement i had 'box += character' and the else statement 
had the value 'box += empty_string'. 
It did not work.
I switched it around a bit, and it worked, but aagain, I'm not entirely sure why.
"""


if __name__ == '__main__':
    #print(create_box(3, 4, '*'))
    print(create_empty_box(3,4,'*'))