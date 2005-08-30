#-----------------------------------------------------------------------------
# Name:        janela.py
# Purpose:     Desenhar janela TODO: Separar logica de negocio)
#
# Author:      Andre Pinto
#
# Created:     2005/08/28
# RCS-ID:      $Id: janela.py $
# Copyright:   (c) 2005
# Licence:     GPL
#-----------------------------------------------------------------------------
#Boa:Frame:frJanela

import wx
import tocador

def create(parent):
    return frJanela(parent)

[wxID_FRJANELA, wxID_FRJANELABTSAIR, wxID_FRJANELABTTOCAR, 
 wxID_FRJANELACHLETRAS, wxID_FRJANELASTBESTADO, wxID_FRJANELASTLETRA, 
] = [wx.NewId() for _init_ctrls in range(6)]

class frJanela(wx.Frame):
    def _init_coll_stbEstado_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)
        parent.SetStatusText(number=0, text=u'')
        parent.SetStatusWidths([-1])

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRJANELA, name=u'frJanela', parent=prnt,
              pos=wx.Point(448, 344), size=wx.Size(311, 361),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Hand Talks!')
        self.SetClientSize(wx.Size(303, 327))

        self.stbEstado = wx.StatusBar(id=wxID_FRJANELASTBESTADO,
              name=u'stbEstado', parent=self, style=0)
        self._init_coll_stbEstado_Fields(self.stbEstado)
        self.SetStatusBar(self.stbEstado)

        self.stLetra = wx.StaticText(id=wxID_FRJANELASTLETRA, label=u'',
              name=u'stLetra', parent=self, pos=wx.Point(8, 16), size=wx.Size(0,
              228), style=0)
        self.stLetra.SetFont(wx.Font(150, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))

        self.btSair = wx.Button(id=wxID_FRJANELABTSAIR, label=u'Sair',
              name=u'btSair', parent=self, pos=wx.Point(8, 248),
              size=wx.Size(80, 40), style=0)
        self.btSair.Bind(wx.EVT_BUTTON, self.OnSairButton,
              id=wxID_FRJANELABTSAIR)

        self.chLetras = wx.Choice(choices=[], id=wxID_FRJANELACHLETRAS,
              name=u'chLetras', parent=self, pos=wx.Point(112, 256),
              size=wx.Size(80, 21), style=0)
        self.chLetras.Bind(wx.EVT_CHOICE, self.OnChLetrasChoice,
              id=wxID_FRJANELACHLETRAS)

        self.btTocar = wx.Button(id=wxID_FRJANELABTTOCAR, label=u'Tocar',
              name=u'btTocar', parent=self, pos=wx.Point(200, 248),
              size=wx.Size(88, 40), style=0)
        self.btTocar.SetMinSize(wx.Size(80, 30))
        self.btTocar.Bind(wx.EVT_BUTTON, self.OnBtTocarButton,
              id=wxID_FRJANELABTTOCAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.chLetras.AppendItems( [chr (ord('A') + x) for x in range (26)] )
        self.chLetras.Select(0)
        ib = wx.IconBundle()
        ib.AddIconFromFile("lib/handtalks.ico",wx.BITMAP_TYPE_ANY)
        self.SetIcons(ib)        

    def OnSairButton(self, event):
        # TODO: Confirmar saida
        self.Close()

    def OnChLetrasChoice(self, event):
        self.stLetra.SetLabel (self.chLetras.GetStringSelection())

    def OnBtTocarButton(self, event):
        self.stbEstado.SetStatusText(number=0, text=u'Reproduzindo audio...')
        if not tocador.toca_tudo ("lib/" + self.stLetra.GetLabel()):
            dlg = wx.MessageDialog(self, "Falha na execucao!",
                                   'Erro',
                                   wx.OK | wx.ICON_EXCLAMATION
                                   )
            dlg.ShowModal()
            dlg.Destroy()
        self.stbEstado.SetStatusText(number=0, text=u'')

