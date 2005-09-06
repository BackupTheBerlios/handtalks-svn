# -*- coding: UTF-8 -*-
#Boa:Frame:mainFrame
#-----------------------------------------------------------------------------
# Name:        janela.py
# Purpose:     Desenhar janela TODO: Separar lógica de negócio)
#
# Author:      André Pinto
#
# Created:     2005/08/28
# RCS-ID:      $Id: janela.py $
# Copyright:   (c) 2005
# Licence:     GPL
#-----------------------------------------------------------------------------

import wx
import tocador

def create(parent):
    return mainFrame(parent)

[wxID_MAINFRAME, wxID_MAINFRAMELETTER, wxID_MAINFRAMELETTERBOX, 
 wxID_MAINFRAMESTATUSBAR, wxID_MAINFRAMETOOLBAR, 
] = [wx.NewId() for _init_ctrls in range(5)]

[wxID_MAINFRAMETOOLBARCONFIG, wxID_MAINFRAMETOOLBARSAIR, 
] = [wx.NewId() for _init_coll_toolBar_Tools in range(2)]

class mainFrame(wx.Frame):
    def _init_coll_boxSizer_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.letterBox, 0, border=0, flag=0)
        parent.AddWindow(self.letter, 0, border=0, flag=0)

    def _init_coll_toolBar_Tools(self, parent):
        # generated method, don't edit

        parent.DoAddTool(bitmap=wx.Bitmap(u'lib/Config.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_MAINFRAMETOOLBARCONFIG, kind=wx.ITEM_NORMAL,
              label=u'Configurar', longHelp=u'Configurar Serial',
              shortHelp=u'Configurar')
        parent.AddSeparator()
        parent.DoAddTool(bitmap=wx.Bitmap(u'lib/CloseWindow.png',
              wx.BITMAP_TYPE_PNG), bmpDisabled=wx.NullBitmap,
              id=wxID_MAINFRAMETOOLBARSAIR, kind=wx.ITEM_NORMAL, label=u'Sair',
              longHelp=u'Fechar o Hand Talks!', shortHelp=u'Sair')
        self.Bind(wx.EVT_TOOL, self.OnSairButton, id=wxID_MAINFRAMETOOLBARSAIR)

        parent.Realize()

    def _init_coll_statusBar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'')

        parent.SetStatusWidths([-1])

    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

        self._init_coll_boxSizer_Items(self.boxSizer)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'mainFrame',
              parent=prnt, pos=wx.Point(585, 255), size=wx.Size(304, 326),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Hand Talks!')
        self.SetClientSize(wx.Size(304, 326))
        self.Bind(wx.EVT_CLOSE, self.OnJanelaClose)

        self.statusBar = wx.StatusBar(id=wxID_MAINFRAMESTATUSBAR,
              name=u'statusBar', parent=self, style=0)
        self._init_coll_statusBar_Fields(self.statusBar)
        self.SetStatusBar(self.statusBar)

        self.letter = wx.StaticText(id=wxID_MAINFRAMELETTER, label=u'',
              name=u'letter', parent=self, pos=wx.Point(0, 32), size=wx.Size(0,
              228), style=0)
        self.letter.SetFont(wx.Font(150, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))

        self.letterBox = wx.Choice(choices=[], id=wxID_MAINFRAMELETTERBOX,
              name=u'letterBox', parent=self, pos=wx.Point(0, 2),
              size=wx.Size(80, 30), style=0)
        self.letterBox.Bind(wx.EVT_CHOICE, self.OnCaixaLetrasChoice,
              id=wxID_MAINFRAMELETTERBOX)

        self.toolBar = wx.ToolBar(id=wxID_MAINFRAMETOOLBAR, name=u'toolBar',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(70, 30),
              style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.SetToolBar(self.toolBar)

        self._init_coll_toolBar_Tools(self.toolBar)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)

        # Popula a caixa de letras
        self.letterBox.AppendItems( [chr (ord('A') + x) for x in range (26)] )
        self.letterBox.Select(0)

        # Associa um ícone
        ib = wx.IconBundle()
        ib.AddIconFromFile("lib/handtalks.ico",wx.BITMAP_TYPE_ANY)
        self.SetIcons(ib)        

    def OnSairButton(self, event):
        self.Close()

    def OnCaixaLetrasChoice(self, event):
        inputLetter = self.letterBox.GetStringSelection()

        self.letter.SetLabel (inputLetter)

        self.statusBar.SetStatusText(number=0, text=u'Reproduzindo áudio...')
        if tocador.toca_tudo ("audio/" + inputLetter):
            self.statusBar.SetStatusText(number=0, text=u'')
        else:
            self.statusBar.SetStatusText(number=0, text=u'Falha na execução!')

    def OnJanelaClose(self, event):
        if event.CanVeto:
            dlg = wx.MessageDialog(self, u"Tem certeza que deseja sair?",
                                   'Confirmação',
                                   wx.YES_NO | wx.ICON_QUESTION
                                   )
            veta = dlg.ShowModal() == wx.ID_NO
            dlg.Destroy()
            if veta:
                return
        self.Destroy()

