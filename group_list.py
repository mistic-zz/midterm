#!C:\python\python.exe
##lookup a contact list and give you the out put
##ncurses library for chage
import sys
import pygame.mixer
from tkinter.messagebox import askokcancel
import getopt, sys
from optparse import OptionParser


debug = False
name = '-a', '--name'
nick = '-i', '--nick'
number = '-u', '--number'
e_mail = '-e', '--e_mail'
find = '-f', '--find'
quit = '-q', '--quit'
 
sounds = pygame.mixer
sounds.init()
name = sounds.Sound("hello.wav")

GROUP_FILE = "C:\python\work\progect\midterm\group_list1.csv"
namesArray = []
template = """
 Contact_Id: %(id)s
 FIRST_Last: %(name)s
 NICK: %(nick)s
 NUMBER: %(number)s
 E_MAIL: %(E_mail)s
"""
##parser.print_help()
usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage=usage)

parser.add_option("-a", "--name",
                  action="store", type="string", dest="group_list",default=True,
                  help="Find all the names in the list." )

parser.add_option("-i", "--nick", 
                  action="store", type="string", dest="group_list",
                  help="Find all the nick names in the list.")

parser.add_option("-u", "--number", 
                  action="store", type="string", dest="group_list",
                  help="Find all the phone numbers in the list.")

parser.add_option("-e", "--e_mail", 
                  action="store", type="string", dest="group_list",
                  help="Find all the E_mails in the list.")

parser.add_option("-f", "--find", 
                  action="store", type="string", dest="group_list",
                  help="Find the Id Number you type in.")

parser.add_option("-q", "--quiet",                  
                  action="store", type="string", dest="group_list" , 
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

print(options)
print(args)

'''def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "aiuefq:v",["outup="])
    except (getopt.GetoptError, err):
        # print help information and exit:
        print (str(err)) # # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for m, v in opts: 
        if m == "-v":
            verbose = True
        if m == "-a":
            verbose = True
        if m == "-i":
            verbose = True
        if m == "-u":
            verbose = True
        if m == "-e":
            verbose = True
        if m == "-f":
            verbose = True
        if m == "-q":
            verbose = True
        elif m == ("-a", "-f"):
            usage()
            sys.exit()
        elif m == ("-i", "-f"):
            usage()
            sys.exit()
        elif m == ("-u", "-f"):
            usage()
            sys.exit()
        elif m == ("-e", "-f"):
            usage()
            sys.exit()
        elif m == ("-m", "--outup"):
            outup = v
        else:
            assert False, "unhandled option"

    #...
'''    

def name():
   ids= list_ID('name')
   for lists in ids:
      print(lists)

def find():
   lookup = int(input("Enter the id of the Contact: "))
   contact = group_list.group_lookup(lookup)
   prints = group_list.print_person(contact)
   name.play()

def nick():
   ids= list_ID('nick')
   for lists in ids:
      print(lists)

def number():
   ids= list_ID('number')
   for lists in ids:
      print(lists)

def e_mail():
   ids= list_ID('E_mail')
   for lists in ids:
      print(lists)

def quit():
      ans = askokcancel('Verify exit', "Really quit?")
      if ans: root.destroy()


def group_list(filename=GROUP_FILE):
    global namesArray
    if(namesArray):
        return namesArray
    else:
        filename=GROUP_FILE
        g=open(filename)
        array_to_return = [ ]
        for row in g:
            s = {}
            (s['id'], s['name'], s['nick'], s['number'], s['E_mail'])= row.split(",")
            array_to_return.append(s)
        g.close()
        namesArray = array_to_return
        return namesArray
    
def list_ID(key):
    names = group_list()
    lists=[]
    for each_name in names:
        lists.append(each_name['id'] + ": " + each_name[key])
        #for run in lists:
        #    return run
    return lists

def group_lookup(id = 1):
    """ this only looks up data and returns the dict that matches."""
    id=int(id)
    matching_row = None
    theList = group_list()
    for row in theList:
        if id == int(row['id']):
            matching_row = row
    if debug:
        print("requested id: ", 'id')
        print("matching_row: ", 'matching_row')
    return matching_row

def print_person(match):
    if match:
        t=template % match
        #print(t)
        #print("Contact_Id: " + match['id'])
        #print("FIRST_Last: " + match['name'])
        #print("NICK: " + match['nick'])
        #print("NUMBER: " + match['number'])
        #print("E_MAIL: " + match['E_mail'])
    return t

    
if __name__ == "__main__":
    #main();
    """
    lookup = int(input("Enter the id of the Contact: "))
    #look=self.look.get()
    match = group_lookup(lookup)
    print_person(match)
    """


