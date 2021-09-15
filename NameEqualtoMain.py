print(__name__) #first module's name equls __main__
#this conditional is used to check whether a python module is beimg run directly or being imported

def main():
    print(__name__)
if __name__ == '__main__':
    main()