'''
How to run jupyter notebook :
C:\PYTHON_TRAINING_BY_SAJAL\WPy64-3810\python-3.8.1.amd64> jupyter notebook --generate-config
Edit C:\Users\i80430\.jupyter\jupyter_notebook_config.py as 
i) c.NotebookApp.browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' --> to open with chrome
ii) ## The directory to use for notebooks and kernels.
    c.NotebookApp.notebook_dir = 'C:/repo/python-e2e-book'
iii) C:\PYTHON_TRAINING_BY_SAJAL\WPy64-3810\python-3.8.1.amd64> jupyter notebook    
'''

#Singel quote sring and double quote string has same meaning. 
#We can use double quote or raw formatter which make us easy to escape single quote as follwing example
print('how\'s your day')
print("how's your day")
print(r"how's your day")

a, b = 0, 1
while a < 30:
    print(a, end =',')
    a, b = b, a + b
    
'''
how's your day
how's your day
how's your day
0,1,1,2,3,5,8,13,21,
'''  