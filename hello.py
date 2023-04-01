import datetime
import FreeCAD
import FreeCADGui


open("a.txt","a").write(f"{datetime.datetime.now()} ahoy" + "\n")
print("hello there")

FreeCADGui.showMainWindow()
FreeCAD.
