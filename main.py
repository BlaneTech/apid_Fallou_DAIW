from controller.controller import *
from view.view import *

def main():
    con = Controller()
    # con.addressProcessing()
    # con.userProcessing()
    # con.companyProcessing()
    # con.postProcessing()
    # con.commentProcessing()
    # con.albumProcessing()
    # con.photoProcessing()
    # con.todoProcessing()
    
    display = View()
    display.menu()

if __name__ == '__main__':
    main()