# Two types of Error
#     i) Syntax
#     ii) Exception (Logical)
#         a) Name error 
#         b) Value Error
#         c) Type Error

# Handling excpetion
#  Exceptions ca be handled using the try..except statement.
#  You basically put all your statements in try block and put error handlers in except block

while True:
    try:
        user_input = int(input(" Give intger number"))
        break
    except:
        print(" oops! that was not integer")


# Raise excpetion
#The raise statement allows the programmer to force a specified exception to occur.

# If you need to determine whether an exception was raised 
# but don’t intend to handle it, a simpler form of the 'raise' statement allows you to re-raise the exception:

while True:
    try:
        user_input = int(input(" plz input an integer"))
        break
    except:
        print("Wrong type input")
        raise

# FINALLY
# The try statement has another optional clause which is intended to define clean-up actions 
# that must be executed under all circumstances.

try:
    raise NameError('How u doing')
finally:
    print(" this run in all circumstances")