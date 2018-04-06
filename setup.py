from cx_Freeze import setup, Executable

base = None

executables = [Executable("gam.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Gam Frontend",
    options = options,
    version = "1.0.1",
    description = 'Front End to Gam by Jay Lee',
    executables = executables
)