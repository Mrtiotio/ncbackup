from config import initR, dataDir, dbDir
import re
import time
import os
import sys

# Check argument
def argCheck():
    arg = sys.argv
    if len(sys.argv) == 1:
        # arg = "Please provide an argument: type \"ncbackup --help\" for help"
        arg = "f1"
        return arg
    elif sys.argv[1] not in [
        "-h",
        "--help",
        "-i",
        "--init",
        "-b",
        "--backup",
        "-r",
        "--restore",
        "--reset",
        "-R"
        ]:
        arg = "f2"
        return arg
    else:
        arg = sys.argv[1]
    return arg

arg = argCheck()

# Remove for production
print(arg)

# The replace function
def replace( filePath, text, subs, flags=0 ):
    with open( filePath, "r+" ) as file:
        fileContents = file.read()
        textPattern = re.compile( re.escape( text ), flags )
        fileContents = textPattern.sub( subs, fileContents )
        file.seek( 0 )
        file.truncate()
        file.write( fileContents )


def initPr():
    if initR == "True":
        print("\"nc-backup\" already initialised.")
    else:
        print("Please provide the data directory.")
        dataIn = input("Data dir: ")
        time.sleep(1)
        print("Please provide the database directory.")
        dbIn = input("Database dir: ")
        if dataIn == dbIn:
            print("The data and database directorys cannot be the same!")
    
        else:
            replace("config.py", initR, "True" )
            replace("config.py", dataDir, dataIn )
            replace("config.py", dbDir, dbIn )

# The reset function
def reset():
    print("\"NC-backup\" has been reset!")
    os.system('cp config.py.bak config.py')

# Main function
def main(arg):
    output = ""
    if arg == "f1":
        output = "Please provide an argument: type \"ncbackup --help\" for help"
    elif arg == "f2":
        output = sys.argv[1]+" is not a valid argument"
    elif arg == "--help" or arg == "-h":
        output = "This is help"
    elif arg == "--init" or arg == "-i":
        initPr()
    elif arg == "--restore" or arg == "-r":
        output = "This is restore"
    elif arg == "--backup" or arg == "-b":
        output = "This is backup"
    elif arg == "--reset" or arg == "-R":
        reset()
    return output


print(main(arg))