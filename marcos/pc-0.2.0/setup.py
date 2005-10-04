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
        "icon_resources": [(1, r"lib\handtalks.ico")]
    }],
    data_files = [ ("lib", glob.glob(r"lib\*")),
                   ("audio", glob.glob(r"audio\*"))   ],
    zipfile = r"lib\handtalks_lib.zip",
    options = {'py2exe': {'excludes': ['javax.comm', 'TERMIOS', 'FCNTL']}},
)
