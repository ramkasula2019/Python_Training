# fibonacci.py
# fibonacci module
def fibo(n):
    result = []
    a, b= 0, 1
    while (a < n):
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    print("the module is run by itself")
    print(fibo(300))
    print(sys.path)
else:
    print("The module is run from other modules by importing")


#The __init__.py files are required to make Python treat directories containing the file as packages
#During shell interpretaion, we may need to reload our modules. For that
# from directory Module.. We can load fibonacci module by import fibonacci. 
# Now change the file in that case, we can reload it by import lib library
# import importlib
# importlib.reload(fibonacci)

# We can import modules from intra pacakgae using dot(.) notation for the path
# eg from sor.views import machine_vew

# we can run python filename.py also to run from command prompt