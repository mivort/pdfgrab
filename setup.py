import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

include_files = []
excludes = []
packages = ["os", "queue", "idna", "requests", "splinter", ]

setup(
    name = "pdfgrab",
    description='PDF Grab',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("pdfgrab.py")]
)
