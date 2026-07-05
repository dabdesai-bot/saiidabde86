import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border="-"*50
    ret=False
    ret=os.path.exists(FolderName)

    if(ret==True):
        ret=os.path.isdir(FolderName)
        if(ret==False):
            print("Unable to create Folder")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory For Log File Created Successfully")

    TimeStamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(FolderName,"Marvellous_%s.log"%TimeStamp)
    print("Log File Get created With Name:",FileName)

    fobj=open(FileName,"w")
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveilliance System-----")
    fobj.write("log Created at:"+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------------System Report---------------\n")

    #print("CPU usage:",psutil.cpu_percent())
    fobj.write("CPU usage:%s %%\n"%psutil.cpu_percent())

    fobj.write(Border+"\n")

    mem=psutil.virtual_memory()
    #print("RAM usage:",mem.percent)
    fobj.write("RAM Usage: %s %%\n" %mem.percent)

    fobj.write(Border+"\n")

    fobj.write("\n Disk Usage Report\n")
    for part in psutil.disk_partitions():
        try:
            usage=psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint}used{usage.percent}%%")
            fobj.write("%s-> %s %% used\n"%(part.mountpoint,usage.percent))
        except:
            pass

    fobj.write(Border+"\n")
    
    net=psutil.net_io_counters()
    fobj.write("\nNetwork usage Report\n")
    fobj.write("Sent:%.2f MB\n" % (net.bytes_sent / (1024*1024)))
    fobj.write("Recv:%.2f MB\n" % (net.bytes_recv / (1024*1024)))
    fobj.write(Border+"\n")

    #process log
    
    fobj.write(Border+"\n")
    fobj.write("----------log file Ended--------\n")
    fobj.write(Border+"/n")

    
def main():
    Border="-"*50
    print(Border)
    print("-----Marvellous Platform Surveilliance System-----")
    print(Border)

    if(len(sys.argv)==2):
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to:")
            print("1:Create Automatic logs")
            print("2:Executes Perodically")
            print("3:Send mails with logs")
            print("4:Store information about the processes")
            print("5:Store information about CPU")
            print("6:Store Information about RAM usage")
            print("7:Store information about Secondary Storage")

        elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py Timeinterval DirectoryName")
            print("TimeInterval: The Time in Minutes for periodic Scheduling")
            print("DirectoryName: NAme of Directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
 
    # python Demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside Process Logic")
        print("Time Interval:",sys.argv[1])
        print("Directory Name:",sys.argv[2])

        #Apply the Scheduler

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Surveillance System Started Successfully")
        print("Directory created with name:",sys.argv[2])
        print("Time Interval in minutes:",sys.argv[1])
        print("Press CTRL+C to Stop the Execution")

        #wait till abort

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid Number of Command line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")
        

    print(Border)
    print("---------Thank you For Using Our Script-----------")
    print(Border)
    
if __name__=="__main__":
    main()