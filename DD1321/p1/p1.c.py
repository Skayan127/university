## LAB1
# Kopiera det här programmet, du kan markera allt med C-a och kopiera med C-c och lägg det i en fil som du döper till p1.a.py och exekvera programmet med python3 p1.a.py


############################################################
#
# Labb 1
#

# global variables

url = "https://cloud.timeedit.net/kth/web/public01/ri.html?h=t&sid=7&p=20201021.x%2C20210117.x&objects=381614.5&ox=0&types=0&fe=0&g=f&ds=f&cch=16-53%2C6-10"

schema_filnamn = "DD1321.htm"
############################################################
#
# imports and defs
#
import re, getopt, sys, urllib.request


class veckadagdatum:
    def __init__(self):
        self.vecka = ''
        self.dag = ''
        self.lista = []
        self.datum = ''
        self.tid = ''

    def __str__(self):
        s = "{} => {:3s}, {:>5s}, {:>3s}, {} ;".format( self.__class__.__name__, self.vecka, self.dag, self.datum, self.tid )
        for h in self.lista:
            s += h + "; "
        return s

    def __contains__(self, x):
        if x in self.vecka:
            return True


###########################################################################
##
## parse_url_file
##
## IN  förväntas vara en lista.
##     
## OUT är också vara en lista.
##
## Funktionen tar in innehållet från file_content och återger det i form av relevant data, i detta fall ett studieschema.
##
def parse_url_file(file_content):
    vek = []

    reg_expr_w = re.compile('.*?td.*?class.*?headline.*?> *([MTOFL][a-zåäö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.*weekin.*> *(v.*?)<.', re.I)

    reg_expr_d = re.compile('.*?td.*?class.*?headline.*?>([MTOFL][a-zåäö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.')

    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)<.td')

    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)<.td', re.I)


    ############## Programmet kraschade här då inmatningen förväntas vara en lista och inte en sträng. ############## 

    #lines = file_content.split('\n')

    lines = file_content
    #print('Någonstans innan return file_name: ', lines)
    qq = veckadagdatum()
    for j, line in enumerate(lines):


        m = reg_expr_w.match(line) 
        if (m != None) :
            qq.dag = m.group(1)
            qq.datum = m.group(3) + "/" + m.group(2)  
            qq.vecka = m.group(4)
            next


        m = reg_expr_d.match(line) 
        if (m != None) : 
            qq.dag = m.group(1)
            qq.datum = m.group(3) + "/" + m.group(2)
            next


        m = reg_expr_i.match(line) 
        if (m != None) and len(m.group(1)) > 0:
            qq.lista.append(m.group(1))
            next


        m = reg_expr_t.match(line) 
        if (m != None) : 
            vek.append(qq)
            qq = veckadagdatum()
            qq.tid = m.group(1)
            next

    return vek




###########################################################################
##
## get file content
##
## IN  är en sträng. Det är filen DD1321.htm
##     
## OUT förväntas vara en sträng
##
## Funktioner läser in file_name som argument och returnerar filinnehållet i form av en sträng
## som senare används i def parse_url_file(file_content): .
##
##
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("No such file", file_name, " please run with --update")
        print ("	python", sys.argv[0], "--update")
        sys.exit() 
    file_content = infil.readlines()
    #file_content = infil.read()

    return file_content

###########################################################################
##
## usage
##
## IN  
##     
## OUT 
##
def usage():
    print ("Usage example:")
    print ("python" , sys.argv[0] ,  "--update ")
    print ("	updates Time Edit schedule")
    print ("python" , sys.argv[0] ,  '--check "v 49"')
    print ("	checks schedule for week 49")
    print ("python" , sys.argv[0])
    print ("	prints previously downloaded schedule")
    
###########################################################################
##
## parse_command_line_args
##
## IN  
##     
## OUT 
##
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print ("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"]=value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo

###########################################################################
##
## print_schedule
##
## IN  
##     
## OUT 
##
def print_schedule(data):
    print ("----------- Schedule -------------")
    for item in data:
        print (item)

###########################################################################
##
## search_data
##
## IN  
##     
## OUT 
##
def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print (item)
    if (found == False):
        print ("Nothing happens", what)

###########################################################################
##
## main
##
## IN  
##     
## OUT 
##
def main():

    global url

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print ("fetching url ...")
        webcontent = urllib.request.urlopen( url )
        with open( schema_filnamn, "w") as fil:
            for row in webcontent:
                utf8line = row.decode('utf8')
                fil.write(utf8line)
        print ("         done")
        
    # Get schedule from disc
    filedata  = get_file_content(schema_filnamn)
    sched = parse_url_file(filedata)

    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)

  
###########################################################################

if __name__ == "__main__":
    main()