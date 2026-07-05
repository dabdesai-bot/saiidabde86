import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def make_zip(folder):
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name=folder +"_"+timestamp+".zip"

    #oprn the zip file
    zobj=zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)

    for root , dirs ,files in os.walk(folder):
        for file in files:
            full_path=os.path.join(root,file)
            relative=os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)
    zobj.close()

    return zip_name     
   
def calculate_hash(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    while True:
        data=fobj.read(1024)
        if not data:
            break
            
        else:
            hobj.update(data)
    
    fobj.close()

    return hobj.hexdigest()

def BackUpFiles(Source , Destination):
    copied_files=[]

    print("reating the BackUp folder for backup process")

    os.makedirs(Destination,exist_ok=True)

    for root , dirs , files in os.walk(Source):
        for file in files:
            src_path=os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path=os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #copy the file if it is new

            if ((not os.path.exists(dest_path)) or (calculate_hash(src_path)!= calculate_hash(dest_path))):
                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)
                
    return copied_files

def MarvellousDataShieldStart(Source="Data"):
    Border="-"*50
    BackupName="MarvellousBackup"
    print(Border)

    print("BackUp process started Successfully at",time.ctime())
    print(Border)

    files=BackUpFiles(Source,BackupName)
    print(Border)
    zip_file=make_zip(BackupName)
    print("BackUp completed Successfully")
    print("File copied :",len(files))
    print("Zip file get created:",zip_file)
    print(Border)

def main():
    
    Border="-"*50
    print(Border)
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if(len(sys.argv)==2):
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to:")
            print("1:Takes Auto backup at given time")
            print("2:backup only new and updated files")
            print("3:Create An archrive of backup periodically")

        elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py Timeinterval SourceDirectory")
            print("TimeInterval: The Time in Minutes for periodic Scheduling")
            print("Source Directory:Name of Directory to backed up")
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
 
    # python Demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside Process Logic")
        print("Time Interval:",sys.argv[1])
        print("Directory Name:",sys.argv[2])

        #Apply the Scheduler

        schedule.every(int(sys.argv[1])).minutes.do( MarvellousDataShieldStart,sys.argv[2])
        print(Border)  
        print("Data Shield System Started Successfully")
        print("Time Interval in minutes:",sys.argv[1])
        print("Press CTRL+C to Stop the Execution")
        print(Border)
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