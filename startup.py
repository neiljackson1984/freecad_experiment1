import datetime
import FreeCADGui
import FreeCAD
import debugpy
import pathlib
import os
import sys
import subprocess
import threading
import rpyc
import rpyc.core
import rpyc.utils.server

PORT_NUMBER_FOR_RPYC_SLAVE_SERVER = 18812

myStdout = None

def driveConsole():
    
    process = subprocess.Popen(
        
        args=[
            pathlib.Path("C:\\cygwin64\\bin\\cat.exe").as_posix(),
            pathlib.Path("C:\\work\\freecad1\\intoFreeCAD").as_posix()
        ],
        # capture_output = True,
        text=True,
        stdout=subprocess.PIPE
    ) 

    while True:
        line = process.stdout.readline()
        if(line):
            # print(f"{datetime.datetime.now()}: {line}", end="")
            FreeCAD.Console.PrintMessage(f"{datetime.datetime.now()}: FreeCAD.Console.PrintMessage: {line}")
            # sys.stdout.write(f"{datetime.datetime.now()}: sys.stdout.write: {line}")
            myStdout.write(f"{datetime.datetime.now()}: myStdout.write: {line}")
            # FreeCADGui.doCommand(f"{datetime.datetime.now()}: FreeCADGui.doCommand: {line}")
            # try:
            #     FreeCADGui.doCommand(f"{line}")
            # except Exception as e:
            #     FreeCAD.Console.PrintMessage(f"{e}")

        else:
            break
        # FreeCADGui.updateGui()
        # FreeCADGui.exec_loop()


def start():
    global myStdout
    myStdout = sys.stdout
    consoleDriverThread = threading.Thread(target=driveConsole, daemon=True)
    consoleDriverThread.start()


    _rpyc_slave_server = rpyc.ThreadedServer(
        rpyc.SlaveService,
        hostname='localhost',
        port=PORT_NUMBER_FOR_RPYC_SLAVE_SERVER,
        reuse_addr=True,
        # ipv6=False, 
        authenticator=None,
        registrar=None, 
        auto_register=False
    )

    rpyc_slave_server_thread = threading.Thread(target=_rpyc_slave_server.start, daemon=True)
    rpyc_slave_server_thread.start()



start()




open("b.txt","a").write(f"{datetime.datetime.now()} ahoy" + "\n")
print("hello there")

# debugpy.configure(
#     # python= str(pathlib.Path(os.__file__).parent.joinpath('python'))
#     python= str(pathlib.Path(sys.executable).parent.joinpath('python.exe'))
#     # python= str(pathlib.Path(os.__file__).parent)
#     # this is a bit of a hack to get the path of the python executable that is bundled with Fusion.
# )

# debugpy.listen(5678)

# process = subprocess.Popen(
    
#     args=[
#         pathlib.Path("C:\\cygwin64\\bin\\cat.exe").as_posix(),
#         pathlib.Path("C:\\work\\freecad1\\intoFreeCAD").as_posix()
#     ],
#     # capture_output = True,
#     text=True,
#     stdout=subprocess.PIPE
# ) 

# while True:
#     line = process.stdout.readline()
#     if(line):
#         print(f"{datetime.datetime.now()}: {line}", end="")
#     else:
#         break
#     FreeCADGui.updateGui()
#     # FreeCADGui.exec_loop()


# for line in iter(process.stdout.readline, None):
#     print(f"{datetime.datetime.now()}: {line}" + "\n")