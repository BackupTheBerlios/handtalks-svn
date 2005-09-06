#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Boa:App:BoaApp
#-----------------------------------------------------------------------------
# Name:        handtalks.py
# Purpose:     Projeto Hand Talks!
#
# Author:      André Pinto
#
# Created:     2005/08/28
# SVN-ID:      $Id: handtalks.py $
# Copyright:   (c) 2005
# Licence:     GPL
#-----------------------------------------------------------------------------

import wx
import janela

modules ={u'janela': [1, u'Janela Principal', u'janela.py'],
 u'tocador': [0, u'Tocador de áudio', u'tocador.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = janela.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
