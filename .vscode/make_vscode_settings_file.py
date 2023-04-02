"""Programmatically finds some paths and creates the settings.json file acordingly."""


import sys
import os
import re
import pathlib
import json
import datetime
from typing import Iterable
import shutil

# this is borrowed from a python script that is included in fusion.
def locatePythonToolFolder() -> str:

    vscodeExtensionPath = ''
    if sys.platform.startswith('win'):
        vscodeExtensionPath = os.path.expandvars(r'%USERPROFILE%\.vscode\extensions')
    else:
        vscodeExtensionPath = os.path.expanduser('~/.vscode/extensions')

    if os.path.exists(vscodeExtensionPath) == False:
        return ''

    msPythons = []
    versionPattern = re.compile(r'ms-python.python-(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)')
    for entry in os.scandir(vscodeExtensionPath):
        if entry.is_dir(follow_symlinks=False):
            match = versionPattern.match(entry.name)
            if match:
                try:
                    version = tuple(int(match[key]) for key in ('major', 'minor', 'patch'))
                    msPythons.append((entry, version))
                except:
                    pass

    msPythons.sort(key=lambda pair: pair[1], reverse=True)
    if (msPythons):
        if None == msPythons[0]:
            return ''
        msPythonPath = os.path.expandvars(msPythons[0][0].path)
        index = msPythonPath.rfind('.')
        version  = int(msPythonPath[index+1:])
        msPythonPath = os.path.join(msPythonPath, 'pythonFiles', 'lib','python')
        msPythonPath = os.path.normpath(msPythonPath)
        if os.path.exists(msPythonPath) and os.path.isdir(msPythonPath):
            return msPythonPath
    return ''



pathOfVscodeSettingsFile = pathlib.Path(__file__).parent.joinpath('settings.json')
print(f"Now generating (and overwriting) {pathOfVscodeSettingsFile}")

debugpyPath = pathlib.Path(locatePythonToolFolder()).resolve()
pathOfFreeCADExecutable = pathlib.Path(shutil.which("freecad")).resolve()
pathOfFreeCADInstallDirectory = pathOfFreeCADExecutable.parent.parent
pathOfPythonExecutableBundledWithFreeCAD = pathOfFreeCADInstallDirectory.joinpath("bin").joinpath("python.exe").resolve() 



preferredPythonAutocompleteAndAnalysisExtraPaths = [
        pathOfFreeCADInstallDirectory.joinpath("bin").as_posix(),
        pathOfFreeCADInstallDirectory.joinpath("bin").joinpath("Lib").as_posix(),
        pathOfFreeCADInstallDirectory.joinpath("bin").joinpath("Lib").joinpath("site-packages").as_posix(),
        pathOfFreeCADInstallDirectory.joinpath("bin").joinpath("DLLs").as_posix(),
        pathOfFreeCADInstallDirectory.joinpath("lib").as_posix(),
        pathOfFreeCADInstallDirectory.joinpath("Ext").as_posix(),
        pathOfFreeCADInstallDirectory.joinpath("Mod").as_posix(),
        pathOfFreeCADInstallDirectory.as_posix(),
		# it does not seem to work to define one setting value in terms of another, unfortunately.
		# "${config:neil.debugpyPath}",
		# "${config:neil.debugpyPath}/debugpy/_vendored/pydevd",
		f"{debugpyPath.as_posix()}",
		f"{debugpyPath.as_posix()}/debugpy/_vendored/pydevd",
		"."
	]

vscodeSettings = {
    "neil.debugpyPath": debugpyPath.as_posix(),
    "neil.pathOfFreeCADInstallDirectory": pathOfFreeCADInstallDirectory.as_posix(),
    "neil.pathOfPythonExecutableBundledWithFreeCAD": pathOfPythonExecutableBundledWithFreeCAD.as_posix(),
    "neil.pathOfFreeCADExecutable": pathOfFreeCADExecutable.as_posix(),

    # "python.languageServer": "Jedi",
	"python.defaultInterpreterPath":	f"{pathOfPythonExecutableBundledWithFreeCAD.as_posix()}",
	"python.linting.pylintEnabled": False,
	"python.linting.enabled": False,
    "python.linting.lintOnSave" : False,
    "python.pipenvPath": f"{pathOfFreeCADInstallDirectory.joinpath('bin').joinpath('Scripts').joinpath('pipenv.exe').as_posix()}",
	"python.analysis.extraPaths": preferredPythonAutocompleteAndAnalysisExtraPaths,
    "python.autoComplete.extraPaths": preferredPythonAutocompleteAndAnalysisExtraPaths	,
    # "python.analysis.stubPath": "typings"
    "python.analysis.stubPath": pathOfFreeCADInstallDirectory.joinpath("bin").joinpath("Lib").joinpath("site-packages").as_posix(),
	# "VsCodeTaskButtons.tasks": [ 
	# 		{"label":"restart_fusion" , "task":"restart_fusion"}
	# ],

    # "terminal.integrated.profiles.windows": {
    #     "Command Prompt": {
    #         "path": [
    #             "${env:windir}\\Sysnative\\cmd.exe",
    #             "${env:windir}\\System32\\cmd.exe"
    #         ],
    #         "args": [],
    #         "icon": "terminal-cmd"
    #     }
    # },

	# https://stackoverflow.com/questions/69047142/vscode-is-suddenly-defaulting-to-powershell-for-integrated-terminal-and-tasks?noredirect=1
	# "terminal.integrated.defaultProfile.windows": "Command Prompt",
	"terminal.integrated.defaultProfile.windows": "PowerShell",

    "selectby.regexes": {
        "regex1": {
            # selects the content of the current "cell" (i.e. region of the
            # document delimited by lines containing "# %%" (with arbitrary
            # whitespace anywhere on the line)
            "flags": "",
            "backward": "(^|$|(\\r?\\n))[ \\t]*#[ \\t]*%%[ \\t]*(^|$|\\r?\\n)",
            "forward": "(^|$|(\\r?\\n))[ \\t]*#[ \\t]*%%[ \\t]*(^|$|\\r?\\n)",
            "backwardInclude": False,
            "forwardInclude": False
          }
    },
    "task.allowAutomaticTasks": "on"
}


import textwrap
with open(pathOfVscodeSettingsFile, 'w') as vscodeSettingsFile:
    lineWidth = 80
    messageParagraphs = [
        f"DO NOT EDIT THIS FILE MANUALLY.",
        f"THIS VSCODE SETTINGS FILE HAS BEEN GENERATED PROGRAMMATICALLY BY {__file__}.",
        f"CREATED {datetime.datetime.now()}"
        # Although it might be useful to have a hard-coded date in the settings file, it is better not to
        # have it so as not to make version control think that the settings file has changed when it really hasn't.
    ]

    formattedBoxedMessage = "\n".join(
        [
            "/**" + "*"*( lineWidth - 6) + "** ",
            *[
                " * " + ( line + " "*(lineWidth - 6 - len(line)) ) +  " * "
                for paragraph in messageParagraphs
                for line in textwrap.wrap(paragraph, width=lineWidth - 6) + [""]
            ],
            "***" + "*"*( lineWidth - 6) + "**/"
        ]
    )
    vscodeSettingsFile.write(formattedBoxedMessage + "\n\n\n")

    json.dump(vscodeSettings, vscodeSettingsFile, indent=4)