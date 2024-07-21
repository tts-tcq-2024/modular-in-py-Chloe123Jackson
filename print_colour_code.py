MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
import pandas as pd

def print_table():
    data = {'Major colour':['White', 'White', 'White', 'White','White','Red','Red','Red','Red','Red','Black','Black','Black','Black','Black', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow','Violet','Violet','Violet','Violet','Violet','Violet'],
        'Minor colour':["Blue", "Orange", "Green", "Brown", "Slate","Blue", "Orange", "Green", "Brown", "Slate","Blue", "Orange", "Green", "Brown", "Slate","Blue", "Orange", "Green", "Brown", "Slate","Blue", "Orange", "Green", "Brown", "Slate"]}
 
    df = pd.DataFrame(data)
    return df
    
    