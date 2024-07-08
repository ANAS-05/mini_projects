import os
import matplotlib.pyplot as plt

labels = ['PASS','FAIL']
colors=['blue','red']

# File path
cwd = os.getcwd()
results_path = os.path.join(cwd,'web_scraper','results3sem.txt')

pass_count = fail_count = 0

try:
    with open(results_path,'r') as file:
        for value in file:
            if value.split()[2].startswith('PASSED'):         
                pass_count += 1
            else:
                fail_count += 1

    plt.pie([pass_count,fail_count],labels=labels,autopct='%1.1f%%',colors=colors)
    plt.title('RESULTS OF CSE-B 3RD SEMESTER')
    plt.show()

except FileNotFoundError:
    print(f"Error: File '{results_path}' not found.")
except Exception as e:
    print(f"Error: {e}")
