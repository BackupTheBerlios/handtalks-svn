#Boa:Frame:frJanela
#-----------------------------------------------------------------------------
# Name:        janela.py
# Purpose:     
#
# Author:      Andre Pinto
#
# Created:     2005/08/28
# RCS-ID:      $Id: janela.py $
# Copyright:   (c) 2005
# Licence:     GPL
#-----------------------------------------------------------------------------

import wx

def create(parent):
    return frJanela(parent)

[wxID_FRJANELA, wxID_FRJANELABTSAIR, wxID_FRJANELABTTOCAR, 
 wxID_FRJANELACHLETRAS, wxID_FRJANELASBESTADO, wxID_FRJANELASTLETRA, 
] = [wx.NewId() for _init_ctrls in range(6)]

class frJanela(wx.Frame):
    def _init_coll_sbEstado_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'acao')

        parent.SetStatusWidths([-1])

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRJANELA, name=u'frJanela', parent=prnt,
              pos=wx.Point(323, 277), size=wx.Size(524, 379),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Hand Talks!')
        self.SetClientSize(wx.Size(516, 345))

        self.sbEstado = wx.StatusBar(id=wxID_FRJANELASBESTADO, name=u'sbEstado',
              parent=self, style=0)
        self._init_coll_sbEstado_Fields(self.sbEstado)
        self.SetStatusBar(self.sbEstado)

        self.stLetra = wx.StaticText(id=wxID_FRJANELASTLETRA, label=u'A',
              name=u'stLetra', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(121, 190), style=0)
        self.stLetra.SetFont(wx.Font(100, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))
        self.stLetra.SetAutoLayout(False)
        self.stLetra.SetThemeEnabled(False)
        self.stLetra.SetWindowVariant(wx.WINDOW_VARIANT_LARGE)

        self.btSair = wx.Button(id=wxID_FRJANELABTSAIR, label=u'Sair',
              name=u'btSair', parent=self, pos=wx.Point(152, 152),
              size=wx.Size(64, 32), style=0)
        self.btSair.Bind(wx.EVT_BUTTON, self.OnSairButton,
              id=wxID_FRJANELABTSAIR)

        self.chLetras = wx.Choice(choices=[], id=wxID_FRJANELACHLETRAS,
              name=u'chLetras', parent=self, pos=wx.Point(160, 24),
              size=wx.Size(56, 21), style=0)

        self.btTocar = wx.Button(id=wxID_FRJANELABTTOCAR, label=u'Tocar',
              name=u'btTocar', parent=self, pos=wx.Point(160, 56),
              size=wx.Size(56, 24), style=0)
        self.btTocar.SetMinSize(wx.Size(80, 30))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.chLetras.AppendItems(['A', 'B'])
        self.chLetras.Select(0)
        ib = wx.IconBundle()
        ib.AddIconFromFile("handtalks.ico",wx.BITMAP_TYPE_ANY)
        self.SetIcons(ib)        

    def OnSairButton(self, event):
        # TODO: Confirmar saida

        self.Close()

