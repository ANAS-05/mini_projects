import os
import matplotlib.pyplot as plt
import pandas as pd 

labels = ['PASS','FAIL']
colors=['blue','red']

# File path
cwd = os.getcwd()
results_path = os.path.join(cwd,'web_scraper','results3sem.txt')

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
    ax.bar(df['roll'], df['sgpa'])
    plt.xticks(rotation=30)
    ax.set_ylim(0.00, 10.00) 
    ax.set_xlabel('ROLL NUMBERS')
    ax.set_ylabel('SGPA')
    ax.set_title('CSE-B 3RD SEM RESULTS')
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{results_path}' not found.")
except Exception as e:
    print(f"Error: {e}")
