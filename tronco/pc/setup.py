
from distutils.core import setup
import py2exe
import glob

setup (
    name = 'HandTalks!',
    description = 'Tradutor do alfabeto LIBRAS',
    version = '0.1', 
    
    windows = [{
        "script": "handtalks.py",
        "icon_resources": [(1, r"lib\handtalks.ico")]
    }],
    data_files = [ ("lib", glob.glob(r"lib\*")),
                   ("audio", glob.glob(r"audio\*"))   ],
    zipfile = r"lib\handtalks.lib",
)
