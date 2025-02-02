from sys import *
def fun(parameter):
    print("Logic of script")

def main():
    print("Application name:",argv[0])

    if(len(argv)!=3):
        print("Error:Invalid number of arguments")
        exit()
    
    if(argv[1]=='-h'):
        print("this script is defined for -------------")
        exit()
 
    if(argv[1]=='-u'):
        print("Usage:Application name __________")
        exit()

    try:
        fun(argv[1])
    except Exception as E:
        print("Error:Invalid input ",E)

    if((len(argv)<1) or (len(argv)>3)):
        print("Error:Invalid number of arguments")

if __name__=="__main__":
    main()