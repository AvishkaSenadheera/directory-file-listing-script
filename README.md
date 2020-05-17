# directory-file-listing-script
This python script is created to write list of files in a directory to a log file according to the Operating System.

The script will log the .exe files in c:\Windows\System32 when ran on windows.
When executed on linux this will write all .bin files in the /lib directory.
The extension of the file and the directory being searched can be changed easily inside the script.

#if platform.system() == 'Windows':
platform module is used to check the os the script is running on and run the relevent code block

#for root, dirs, files in os.walk('c:\Windows\System32'): 
change the directory that is being searched here.

#if file.endswith('.exe'):
change the type of the file here
