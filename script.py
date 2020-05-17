#windows
import platform
if platform.system() == 'Windows':
	f = open("entries_Win10.log", "a")
	f.write("Platform: ")
	system = platform.system()
	release = platform.release()
	version = platform.version()
	f.write(str(platform.system_alias(system,release,version)))
	f.write("\n")

	import datetime
	f = open("entries_Win10.log", "a")
	now=datetime.datetime.now()
	f.write(now.strftime("%d-%m-%Y"))
	f.write("\n")
	f.write(now.strftime("%I:%M %p\n\n"))
	f.write("Direcory of c:\Windows\System32\n\n")
	f.close()

	import os
	for root, dirs, files in os.walk('c:\Windows\System32'):
		for file in files:
			if file.endswith('.exe'):
				f = open("entries_Win10.log", "a")
				f.write(os.path.join(root, file))
				f.write("\n")

				#print(os.path.join(root, file))
	f.close()
#linux
import platform
if platform.system() == 'Linux':
    f = open("entries_lin.log", "a")
    f.write("Platform: ")
    #test = platform.system(),platform.win32_ver()
    #f.write(platform.system())
    system = platform.system()
    release = platform.release()
    version = platform.version()
    f.write(str(platform.system_alias(system,release,version)))
    f.write("\n")

    import datetime
    f = open("entries_lin.log", "a")
    now=datetime.datetime.now()
    f.write(now.strftime("%d-%m-%Y"))
    f.write("\n")
    f.write(now.strftime("%I:%M %p\n\n"))
    f.write("Direcory of /lib\n\n")
    f.close()
    
    import os
    for root, dirs, files in os.walk('/lib'):
        for file in files:
            if file.endswith('.bin'):
                f = open("entries_lin.log", "a")
                f.write(file)
                f.write("\n")

                #print(os.path.join(root, file))
    f.close()
