#this is used for creating the executable file
#of application
import sys
from cx_Freeze import setup, Executable
setup( name = "Any Name", version = "3.1",
       description = "Any Description you like",
       executables = [Executable("fox_the_obstacles.py",
                                 base = "Win32GUI")])
