from setuptools import setup

setup(
    name='gtfoblookup',
    version='3',
    description='Offline command line lookup utility for GTFOBins, LOLBAS, WADComs, and HijackLibs',
    author='James Conlan',
    author_email='James.Conlan@nccgroup.com',
    url='https://github.com/nccgroup/GTFOBLookup',
    license='GPL-3.0',
    py_modules=[
        'gtfoblookup'
    ],
    install_requires=[
        'appdirs',
        'colorama',
        'gitpython',
        'pyyaml'
    ],
    python_requires='>=3.0.0',
    entry_points={
        'console_scripts': [
            'gtfoblookup = gtfoblookup:main'
        ]
    }
)