#Boa:Frame:frJanela

import wx

def create(parent):
    return frJanela(parent)

[wxID_FRJANELA, wxID_FRJANELABTSAIR, wxID_FRJANELABTTOCAR, 
 wxID_FRJANELACHLETRAS, wxID_FRJANELAPANEL1, wxID_FRJANELASBESTADO, 
 wxID_FRJANELASTLETRA, 
] = [wx.NewId() for _init_ctrls in range(7)]

class frJanela(wx.Frame):
    def _init_coll_fsGrid_Growables(self, parent):
        # generated method, don't edit

        parent.AddGrowableRow(2)
        parent.AddGrowableCol(0)

    def _init_coll_fsGrid_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.stLetra, 0, border=0, flag=0)

    def _init_coll_sbEstado_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'acao')

        parent.SetStatusWidths([-1])

    def _init_sizers(self):
        # generated method, don't edit
        self.fsGrid = wx.FlexGridSizer(cols=2, hgap=0, rows=5, vgap=0)

        self._init_coll_fsGrid_Items(self.fsGrid)
        self._init_coll_fsGrid_Growables(self.fsGrid)

        self.btSair.SetSizer(self.fsGrid)

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

        self.panel1 = wx.Panel(id=wxID_FRJANELAPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(516, 322),
              style=wx.TAB_TRAVERSAL)

        self.chLetras = wx.Choice(choices=[], id=wxID_FRJANELACHLETRAS,
              name=u'chLetras', parent=self.panel1, pos=wx.Point(160, 24),
              size=wx.Size(56, 21), style=0)

        self.btTocar = wx.Button(id=wxID_FRJANELABTTOCAR, label=u'Tocar',
              name=u'btTocar', parent=self.panel1, pos=wx.Point(160, 56),
              size=wx.Size(56, 24), style=0)
        self.btTocar.SetMinSize(wx.Size(80, 30))

        self.stLetra = wx.StaticText(id=wxID_FRJANELASTLETRA, label=u'A',
              name=u'stLetra', parent=self.panel1, pos=wx.Point(0, 0),
              size=wx.Size(121, 190), style=0)
        self.stLetra.SetFont(wx.Font(100, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))
        self.stLetra.SetAutoLayout(False)
        self.stLetra.SetThemeEnabled(False)
        self.stLetra.SetWindowVariant(wx.WINDOW_VARIANT_LARGE)

        self.btSair = wx.Button(id=wxID_FRJANELABTSAIR, label=u'Sair',
              name=u'btSair', parent=self.panel1, pos=wx.Point(152, 152),
              size=wx.Size(64, 32), style=0)
        self.btSair.Bind(wx.EVT_BUTTON, self.OnSairButton,
              id=wxID_FRJANELABTSAIR)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.chLetras.AppendItems(['A', 'B'])
        self.chLetras.Select(0)

    def OnSairButton(self, event):
        self.Close()

