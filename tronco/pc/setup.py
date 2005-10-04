#!/usr/bin/env python
# -*- coding: latin-1 -*-

from distutils.core import setup
import py2exe
import glob

setup (
    name = 'HandTalks!',
    description = 'Tradutor do alfabeto LIBRAS',
    version = '0.2', 
    
    windows = [{
        "script": "handtalks.pyw",
        "icon_resources": [(1, r"imagem\handtalks.ico")]
    }],
    data_files = [ ("imagem", glob.glob(r"imagem\*")),
                   ("audio", glob.glob(r"audio\*"))   ],
#    zipfile = r"handtalks_lib.zip",
#    zipfile = r"lib\handtalks_lib.zip",
    zipfile = None,
    options = {'py2exe': {'excludes': ['javax.comm', 'TERMIOS', 'FCNTL']}},
)
