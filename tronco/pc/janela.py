#Boa:Frame:Janela

import wx

def create(parent):
    return Janela(parent)

[wxID_JANELA, wxID_JANELABTSAIR, wxID_JANELABTTOCAR, wxID_JANELACHOICE1, 
 wxID_JANELAPNPRINCIPAL, wxID_JANELASTESTADO, wxID_JANELASTLETRA, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Janela(wx.Frame):
    def _init_coll_stEstado_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'acao')

        parent.SetStatusWidths([-1])

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_JANELA, name=u'Janela', parent=prnt,
              pos=wx.Point(391, 346), size=wx.Size(516, 345),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Hand Talks!')
        self.SetClientSize(wx.Size(516, 345))

        self.pnPrincipal = wx.Panel(id=wxID_JANELAPNPRINCIPAL,
              name=u'pnPrincipal', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(516, 350), style=wx.TAB_TRAVERSAL)
        self.pnPrincipal.SetMinSize(wx.Size(500, 350))

        self.stLetra = wx.StaticText(id=wxID_JANELASTLETRA, label=u'A',
              name=u'stLetra', parent=self.pnPrincipal, pos=wx.Point(128, 20),
              size=wx.Size(67, 111), style=0)
        self.stLetra.SetFont(wx.Font(72, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))
        self.stLetra.SetAutoLayout(False)

        self.btTocar = wx.Button(id=wxID_JANELABTTOCAR, label=u'Tocar',
              name=u'btTocar', parent=self.pnPrincipal, pos=wx.Point(200, 152),
              size=wx.Size(80, 30), style=0)
        self.btTocar.SetMinSize(wx.Size(80, 30))

        self.btSair = wx.Button(id=wxID_JANELABTSAIR, label=u'Sair',
              name=u'btSair', parent=self.pnPrincipal, pos=wx.Point(16, 152),
              size=wx.Size(80, 32), style=0)
        self.btSair.Bind(wx.EVT_BUTTON, self.OnSairButton, id=wxID_JANELABTSAIR)

        self.stEstado = wx.StatusBar(id=wxID_JANELASTESTADO, name=u'stEstado',
              parent=self, style=0)
        self._init_coll_stEstado_Fields(self.stEstado)
        self.SetStatusBar(self.stEstado)

        self.choice1 = wx.Choice(choices=[], id=wxID_JANELACHOICE1,
              name='choice1', parent=self.pnPrincipal, pos=wx.Point(120, 224),
              size=wx.Size(80, 29), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.choice1.AppendItems(['A', 'B'])
        self.choice1.Select(0)

    def OnSairButton(self, event):
        self.Close()

