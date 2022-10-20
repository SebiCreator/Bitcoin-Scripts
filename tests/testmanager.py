from ast import Sub


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    G_TEXT = '\33[90m'


def printError(category: str, msg: str):
    print(bcolors.FAIL + "[%s]\t" %
          category + bcolors.G_TEXT + msg + bcolors.ENDC)


def printWarning(category: str, msg: str):
    print(bcolors.WARNING + "[%s]\t" %
          category + bcolors.G_TEXT + msg + bcolors.ENDC)


def printSucess(category: str, msg: str):
    print(bcolors.OKGREEN+ "[%s]\t" %
          category + bcolors.G_TEXT + msg + bcolors.ENDC)



def handleAssessment(func,input,output):
        func_name = func.__name__
        res = func(input)
        try:
            if res == output:
                printSucess(func_name,"TEST PASSED!")
            else:
                printError(func_name,"TEST FAILED!")
                printWarning("DIFF", "is: %s\nshould: %s" % (res,output))
        except Exception as e:
            printError(func_name, "EXCPETION OCCURED")
            printWarning("EXCEPTION",e)