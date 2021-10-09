import sys
import fileinput
import datetime as dt

class Cookies:
    """parses cookie_log.csv and returns most active cookie in specified day
    
    Methods:
    most_active_cookie - parses command line args, prints most active
                        cookies
    createCount - creates counter object (hashmap) to count elements in
                array
    parse - parses log file 
    """
    
    def __init__(self):
        # hashmap to hold parsed log
        self.data = {}

    def most_active_cookie(self):
        """prints most active cookies in specified day from log file
        """
        
        filename = sys.argv[1]
        self.parse(filename)
        # date argument in command prompt
        inp_date = sys.argv[3]

        # convert str to datetime object
        inp_date = dt.datetime.strptime(inp_date,"%Y-%m-%d").date()
        
        # input date not in log file
        if inp_date not in self.data:
            print("date not found")
            return
        
        # create counter of cookies in specified day
        count = self.createCount(self.data[inp_date])

        # count of most active cookie
        maxVal = max(count.values())

        # print all most active cookies
        for key,val in count.items():
            if val == maxVal:
                print(key)
        
        
    def createCount(self,arr):
        """Creates counter object to count elements in array
        
        Keyword arguments:
        arr -- array used to create counter
        Return: counter
        """
        
        counter = {}

        # create counter of items in array
        for item in arr:
            counter[item] = counter.get(item,0) + 1

        return counter   

    def parse(self,filename):
        """parses command line arguments and log file
        
        Keyword arguments:
        filename -- log file to parse
        """
        
        # parse file input
        with fileinput.input(files=(filename)) as f:
            for line in f:

                # clean lines and create list object
                line = line.replace('\n','')
                split_line = line.split(',')

                # extract time and convert to datetime object
                time = split_line[1]
                date_obj = dt.datetime.strptime(time,"%Y-%m-%dT%H:%M:%S+00:00").date()

                # create hashmap with date:cookie structure
                if date_obj in self.data:
                    self.data[date_obj].append(split_line[0])
                else:
                    self.data[date_obj] = [split_line[0]]
            

if __name__ == "__main__":
    active = Cookies()
    active.most_active_cookie()