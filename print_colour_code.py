MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_colour_code_table():
    table=[['Pair number','Major colour','Minor colour']]
    pair_number=1
    row=[]
    for major_colour in MAJOR_COLORS:
        for minor_colour in MINOR_COLORS:
            l.append(pair_number)
            l.append(major_colour)
            l.append(minor_colour)
            table.append(l)
            pair_number+=1
            l=[]
            print(table)
    for row in table:
        print('--------------------------------------------')
        print('| {:^11} | {:^12} | {:^12} |'.format(*row))
    
    
