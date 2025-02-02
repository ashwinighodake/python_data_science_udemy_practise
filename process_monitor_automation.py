import psutil
def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            #pinfor['vms']=proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    return listprocess

def main():
    print("Process Monitor with memory usage")
    listprocess=ProcessDisplay()

    for element in listprocess:
        print(element)

if __name__=="__main__":
    main()