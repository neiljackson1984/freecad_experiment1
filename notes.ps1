see [https://forum.freecad.org/viewtopic.php?f=22&t=28901&p=350160] "Debugging macros with VS 2017"
see [https://forum.freecad.org/viewtopic.php?style=10&p=533299] "Advice requested on developing python workbench in VS Code"
see [https://github.com/microsoft/vscode-python/issues/5660] "How do I get visual studio code to load the modules of the pyd file"

see [https://wiki.freecad.org/Debugging]
That article mentions the ptvsd python package (https://github.com/Microsoft/ptvsd/, https://pypi.org/project/ptvsd/),
but it looks like ptvsd is deprecated and debugpy is the successor.


& "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pip install pipenv
& "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pipenv install


& "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pip install pylance

$env:PATH = "C:\Program Files\FreeCAD 0.20\bin;$($env:PATH)"; & "C:/Program Files/FreeCAD 0.20/bin/Scripts/pipenv.exe" install
$env:PATH = "C:\Program Files\FreeCAD 0.20\bin;$($env:PATH)"; & "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pipenv install
which python

$($(& "C:/Program Files/FreeCAD 0.20/bin/python.exe" --version) -replace "^.*?([\d\.]+).*`$","`$1")

$env:PYTHONPATH
$env:*
dir env:
pwsh

# struggling to create a venv with the FreeCAD-bundled python interpreter -- pipenv tends to try to find the latest version of python -- even if it is not the first python.exe on the path.
# this works:
$env:PATH = "C:\Program Files\FreeCAD 0.20\bin;$($env:PATH)"; & "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pipenv --python "$($(& "C:/Program Files/FreeCAD 0.20/bin/python.exe" --version) -replace "^.*?([\d\.]+).*`$","`$1")" install


$env:PATH = "C:\Program Files\FreeCAD 0.20\bin;$($env:PATH)"; & "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pipenv --python "$($(& "C:/Program Files/FreeCAD 0.20/bin/python.exe" --version) -replace "^.*?([\d\.]+).*`$","`$1")" install
which python

& "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pip uninstall pylance


# visual studio code intellisense is not picking up on the contents of the FreeCAD and FreeCADGui modules.  I think this has something to do with the fact that
# these modules are not pure-python modules but are instead binary modules (specifically, .pyd files, which are dll files).
# 
# thus, a set of stub files is needed for pylance (or whatever language server vs code is using) to inspect.
# see [https://github.com/CyrilWaechter/freecad-stubs]
# see [https://forum.freecad.org/viewtopic.php?t=39032] "FreeCAD python type definitions, code documentation"
# see [https://pypi.org/project/freecad-stubs/]

& "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pip install freecad-stubs

# merely installing freecad-stubs pip package was not sufficient.  We also had to set the vscode setting "python.analysis.stubPath" to pathOfFreeCADInstallDirectory.joinpath("bin").joinpath("Lib").joinpath("site-packages")


& "C:/Program Files/FreeCAD 0.20/bin/FreeCadCmd.exe" --python-path "C:/Users/Admin/.vscode/extensions/ms-python.python-2023.4.1/pythonFiles/lib/python"
& "C:/Program Files/FreeCAD 0.20/bin/FreeCad.exe" --python-path "C:/Users/Admin/.vscode/extensions/ms-python.python-2023.4.1/pythonFiles/lib/python"

& "C:/Program Files/FreeCAD 0.20/bin/FreeCad.exe" 
& "C:/Program Files/FreeCAD 0.20/bin/FreeCad.exe" --single-instance hello.py
& "C:/Program Files/FreeCAD 0.20/bin/FreeCad.exe" hello.py
& "C:/Program Files/FreeCAD 0.20/bin/FreeCad.exe" --single-instance "C:/work/fusion_programmatic_experiment/a.FCStd"
& "C:/Program Files/FreeCAD 0.20/bin/FreeCad.exe" "C:/work/fusion_programmatic_experiment/a.FCStd"

mkfifo --help

mkfifo outOfFreeCAD; 
mkfifo intoFreeCAD; 

(while true; do cat < outOfFreeCAD; done) &
while true; do cat < outOfFreeCAD; done &

cat > intoFreeCAD

while true; do cat < intoFreeCAD; done &

process = subprocess.Popen(
    
    args=subprocessArgs,
    # capture_output = True,
    text=True,
    stdout=subprocess.PIPE
) 

& "C:/Program Files/FreeCAD 0.20/bin/python.exe" 

& "C:/Program Files/FreeCAD 0.20/bin/python.exe" -m pip install rpyc