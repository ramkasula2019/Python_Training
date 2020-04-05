
'''
Virtual environments are self-contained directory that contains a Python installation 
for a particular version of Python, plus a number of additional packages
virtualenv is a tool to create isolated Python environments. 
virtualenv creates a folder which contains all the necessary executables to use the packages 
that a Python project would need.
'''

# Install Virtual env
$ cd project_folder
$ virtualenv venv

# we can choose our choice of interpretor
$ virtualenv -p /usr/bin/python3.6 venv

# Activate venv
$ source venv/bin/activate (Window)
$ . venv/bin/activate (Linux)

# Install package inside venv
(venv) root@i10106:/usr/local/repositories/platform# pip install request

# Deactivate venv
(venv) root@i10106:/usr/local/repositories/platform# deactivate

# Removing venv
(venv) root@i10106:/usr/local/repositories/platform# rm -rf venv