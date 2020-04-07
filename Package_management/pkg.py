Package Management in Python (PIP)
#  Searching package
pip search requrests

# to instal package
pip install requests
pip install requests version == 2.6.0

# upgrading package
pip install upgrade requests

# uninstall package
pip uninstall requests

# to list package install in venv
pip list

# to get info of package
pip show requests

# to get versionised package info
pip freeze 

pip freeze > requirement.txt 
f = open('requirement.txt')
print(f.read())
f.close()
