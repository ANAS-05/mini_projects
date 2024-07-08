import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

labels = ['PASS','FAIL']
colors=['blue','red']

# File path
cwd = os.getcwd()
results_path = os.path.join(cwd,'web_scraper','results2sem.txt')

pass_list=[]
result_of_pass=[]

try:
    with open(results_path,'r') as file:
        for value in file:
            if value.split()[2].startswith('PASSED'):         
               pass_list.append(value.split()[0])
               result_of_pass.append(float(value.split()[2].split('-')[1]))
            else:
               continue

    data = {
    "roll":pass_list,
    "sgpa":result_of_pass
    }

    df = pd.DataFrame(data)
    df.sort_values(by=["sgpa"],ascending=False,inplace=True)
    
    fig, ax = plt.subplots(figsize = (14,10))
    bars = ax.bar(df['roll'], df['sgpa'])

    #code for adding text on the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval,yval,ha='center', va='bottom')

    plt.xticks(rotation=90)

    #code for setting the y-axis in intervals of 0.5
    ax.set_yticks(np.arange(np.floor(ax.get_ylim()[0]), np.ceil(ax.get_ylim()[1])+0.5, 0.5))
    
    ax.set_xlabel('ROLL NUMBERS')
    ax.set_ylabel('SGPA')
    ax.set_title('CSE-B 2ND SEM RESULTS')
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{results_path}' not found.")
except Exception as e:
    print(f"Error: {e}")
