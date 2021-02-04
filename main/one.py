
def func():
    print("FUNCTION in one.py")

print("TOP level in one.py")


if __name__ == '__main__':
    print('one.py is being run directly!')
else:
    print("One.py has been imported")