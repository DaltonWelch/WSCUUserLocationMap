#File_Output.py
import Parse

def write_parsed_log(weblog,outputName):
    parseTest = Parse.parse_file(weblog)
    f1 = open("WSCUMapLeaflet/ParsedLogs/"+str(outputName), 'w')

    unique_visitors = set(x[1] for x in parseTest)
    for v in unique_visitors:
        ip = v
        loc = Parse.lookup_address(ip)
        f1.write(str(loc[0])+","+str(loc[1])+",")
    print("File parse successful")
    f1.close()

def clear_file(fn):
    open(fn,'w').close()

def read_file(fn):
    f2 = open(fn,'r')
    message = f2.read()
    print(message)
    f2.close()


if __name__ == "__main__":
    """
    test
    """
    #"WebLogs/TestLog.log"
    #print(parseTest)

    write_parsed_log("WebLogs/TestLog.log","Parse_Log.txt")
