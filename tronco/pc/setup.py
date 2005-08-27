
from distutils.core import setup
import py2exe

setup(name = 'default',
    version = '0.1', 
    scripts = [], 
    windows = [
        {
            "script": "handtalks.py",
            "icon_resources": [(1, "handtalks.ico")]
        }
    ],
)
