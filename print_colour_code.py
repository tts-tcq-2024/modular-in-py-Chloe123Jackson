MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
# table = [['1', 2222, 30, 500], [4, 55, 6777, 1]]
table=[['Pair number','Major colour','Minor colour']]
pair_number=1
l=[]
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
    
    
