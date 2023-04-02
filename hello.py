import datetime
import FreeCADGui
import FreeCAD



open("a.txt","a").write(f"{datetime.datetime.now()} ahoy" + "\n")
print("hello there")

# FreeCAD.App.Console.GetObservers()
# in freecad's python console, sys.stdout and sys.stdin appear to be connected to the python console.  Therefore,
# we might be able to use standard python libraries to redirect (or tee) to a pseudoterminal (or SSH server, or such)

