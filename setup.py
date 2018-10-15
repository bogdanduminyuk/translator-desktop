from cx_Freeze import setup, Executable

base = "Win32GUI"
options = {
    'build_exe': {
        'packages': ["idna", "multiprocessing"],
    },
}

setup(
    name="main",
    options=options,
    version="2",
    description='None',
    executables=[Executable("main.py", base=base)]
)
