# -*- coding: latin-1 -*-
# generated by wxGlade 0.4cvs on Thu Sep  1 12:47:22 2005

import wx
import tocador
import serial
import threading
from ConfigSerial import ConfigSerial

# begin wxGlade: dependencies
# end wxGlade

#----------------------------------------------------------------------
# Create an own event type, so that GUI updates can be delegated
# this is required as on some platforms only the main thread can
# access the GUI without crashing. wxMutexGuiEnter/wxMutexGuiLeave
# could be used too, but an event is more elegant.

SERIALRX = wx.NewEventType()
# bind to serial data receive events
EVT_SERIALRX = wx.PyEventBinder(SERIALRX, 0)

class SerialRxEvent(wx.PyCommandEvent):
    eventType = SERIALRX
    def __init__(self, windowID, data):
        wx.PyCommandEvent.__init__(self, self.eventType, windowID)
        self.data = data

    def Clone(self):
        self.__class__(self.GetId(), self.data)

#----------------------------------------------------------------------

ID_SAIR = wx.NewId()
ID_CONFIG = wx.NewId()
ID_COMUNIC = wx.NewId()
ID_SOBRE = wx.NewId()

class JanelaPrincipal(wx.Frame):
    def __init__(self, *args, **kwds):
        # Valores padr�es da serial
        self.serial = serial.Serial()
        self.serial.port = 0;
        self.serial.baudrate = 9600;
        self.serial.bytesize = 8;
        self.serial.parity = serial.PARITY_NONE;
        self.serial.stopbits = 1;
        self.serial.timeout = 2;
        self.serial.rtscts = False;
        self.serial.xonxoff = False;

        # Threading
        self.thread = None
        self.alive = threading.Event()               

        # begin wxGlade: JanelaPrincipal.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.divisor = wx.SplitterWindow(self, -1, style=wx.SP_NOBORDER)
        self.ladoDireito = wx.Panel(self.divisor, -1)
        self.ladoEsquerdo = wx.Panel(self.divisor, -1)
        self.sizerSaida_staticbox = wx.StaticBox(self.ladoEsquerdo, -1, u"Sa�da")
        self.sizerHistorico_staticbox = wx.StaticBox(self.ladoDireito, -1, u"Hist�rico")
        self.sizerEntrada_staticbox = wx.StaticBox(self.ladoEsquerdo, -1, "Entrada")
        
        # Menu Bar
        self.janela_menubar = wx.MenuBar()
        self.SetMenuBar(self.janela_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_CONFIG, "Confi&gurar...", "Ajusta detalhes da porta serial", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_COMUNIC, "&Comunicar", u"Inicia/Interrompe comunica��o", wx.ITEM_CHECK)
        self.janela_menubar.Append(wxglade_tmp_menu, u"&Comunica��o")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_SOBRE, "So&bre...", u"Informa��es sobre o HandTalks!", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_SAIR, "&Sair", "", wx.ITEM_NORMAL)
        self.janela_menubar.Append(wxglade_tmp_menu, "&Geral")
        # Menu Bar end
        self.janela_statusbar = self.CreateStatusBar(7, wx.ST_SIZEGRIP)
        
        # Tool Bar
        self.janela_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT|wx.TB_DOCKABLE)
        self.SetToolBar(self.janela_toolbar)
        self.janela_toolbar.AddLabelTool(ID_CONFIG, "Configurar...", wx.Bitmap("lib/Config.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Configurar...", "Ajusta detalhes da porta serial")
        self.janela_toolbar.AddLabelTool(ID_COMUNIC, "Comunicar", wx.Bitmap("lib/Parado.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Comunicar", u"Inicia/Interrompe comunica��o")
        self.janela_toolbar.AddSeparator()
        self.janela_toolbar.AddLabelTool(ID_SOBRE, "Sobre...", wx.Bitmap("lib/Info.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Sobre...", u"Informa��es sobre o HandTalks!")
        self.janela_toolbar.AddLabelTool(ID_SAIR, "Sair", wx.Bitmap("lib/Fechar.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Sair", "Fecha o HandTalks!")
        # Tool Bar end
        self.comando = wx.TextCtrl(self.ladoEsquerdo, -1, "")
        self.enviar = wx.BitmapButton(self.ladoEsquerdo, -1, wx.Bitmap("lib/Enviar.png", wx.BITMAP_TYPE_ANY))
        self.resposta = wx.TextCtrl(self.ladoEsquerdo, -1, "", style=wx.TE_READONLY)
        self.caixaLetras = wx.Choice(self.ladoEsquerdo, -1, choices=[])
        self.letraExibida = wx.StaticText(self.ladoEsquerdo, -1, "A", style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
        self.historico = wx.TextCtrl(self.ladoDireito, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.configuraSerial, id=ID_CONFIG)
        self.Bind(wx.EVT_MENU, self.alternaComunicacao, id=ID_COMUNIC)
        self.Bind(wx.EVT_MENU, self.sobreHandtalks, id=ID_SOBRE)
        self.Bind(wx.EVT_MENU, self.sair, id=ID_SAIR)
        self.Bind(wx.EVT_TEXT_ENTER, self.enviarComando, self.comando)
        self.Bind(wx.EVT_BUTTON, self.enviarComando, self.enviar)
        self.Bind(wx.EVT_CHOICE, self.trocouLetra, self.caixaLetras)
        # end wxGlade

        # Mais eventos
        self.Bind(wx.EVT_CLOSE, self.fechaAplicacao)
        self.Bind(EVT_SERIALRX, self.OnSerialRead)

        # Associa um �cone
        ib = wx.IconBundle()
        ib.AddIconFromFile("lib/handtalks.ico",wx.BITMAP_TYPE_ANY)
        self.SetIcons(ib)


    def __set_properties(self):
        # begin wxGlade: JanelaPrincipal.__set_properties
        self.SetTitle("Hand Talks!")
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        self.janela_statusbar.SetStatusWidths([-1, 60, 60, 20, 20, 20, 120])
        # statusbar fields
        janela_statusbar_fields = ["", "", "", "", "", "", ""]
        for i in range(len(janela_statusbar_fields)):
            self.janela_statusbar.SetStatusText(janela_statusbar_fields[i], i)
        self.janela_toolbar.SetToolBitmapSize((16, 16))
        self.janela_toolbar.Realize()
        self.comando.SetToolTipString(u"Digite um comando para enviar � luva")
        self.enviar.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        self.enviar.SetToolTipString("Enviar Comando")
        self.enviar.Enable(False)
        self.enviar.SetSize(self.enviar.GetBestSize())
        self.resposta.SetToolTipString("Resposta da luva")
        self.resposta.Enable(False)
        self.caixaLetras.SetMinSize((50, 21))
        self.caixaLetras.SetSelection(0)
        self.letraExibida.SetFont(wx.Font(200, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.historico.SetToolTipString(u"Hist�rico da comunica��o com a luva")
        self.historico.Enable(False)
        # end wxGlade

        # Popula a caixa de letras
        self.caixaLetras.AppendItems( [chr (ord('A') + x) for x in range (26)] )
        self.caixaLetras.Select(0)
        
        # Barra de estado
        self.atualizaStatusSerial(inicio=True)


    def __do_layout(self):
        # begin wxGlade: JanelaPrincipal.__do_layout
        sizerJanela = wx.BoxSizer(wx.HORIZONTAL)
        sizerHistorico = wx.StaticBoxSizer(self.sizerHistorico_staticbox, wx.VERTICAL)
        sizerPrincipal = wx.BoxSizer(wx.VERTICAL)
        sizerSaida = wx.StaticBoxSizer(self.sizerSaida_staticbox, wx.VERTICAL)
        sizerEntrada = wx.StaticBoxSizer(self.sizerEntrada_staticbox, wx.HORIZONTAL)
        sizerEntrada.Add(self.comando, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        sizerEntrada.Add(self.enviar, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        sizerEntrada.Add(self.resposta, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        sizerEntrada.Add(self.caixaLetras, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 3)
        sizerPrincipal.Add(sizerEntrada, 0, wx.ALL|wx.EXPAND, 3)
        sizerSaida.Add((1, 1), 1, wx.ADJUST_MINSIZE, 0)
        sizerSaida.Add(self.letraExibida, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        sizerSaida.Add((1, 1), 1, wx.ADJUST_MINSIZE, 0)
        sizerPrincipal.Add(sizerSaida, 1, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 3)
        self.ladoEsquerdo.SetAutoLayout(True)
        self.ladoEsquerdo.SetSizer(sizerPrincipal)
        sizerPrincipal.Fit(self.ladoEsquerdo)
        sizerPrincipal.SetSizeHints(self.ladoEsquerdo)
        sizerHistorico.Add(self.historico, 1, wx.ALL|wx.EXPAND, 3)
        self.ladoDireito.SetAutoLayout(True)
        self.ladoDireito.SetSizer(sizerHistorico)
        sizerHistorico.Fit(self.ladoDireito)
        sizerHistorico.SetSizeHints(self.ladoDireito)
        self.divisor.SplitVertically(self.ladoEsquerdo, self.ladoDireito)
        sizerJanela.Add(self.divisor, 1, wx.ALL|wx.EXPAND, 3)
        self.SetAutoLayout(True)
        self.SetSizer(sizerJanela)
        sizerJanela.Fit(self)
        sizerJanela.SetSizeHints(self)
        self.Layout()
        self.Centre()
        # end wxGlade


    def atualizaStatusSerial(self, inicio=False):
        janela_statusbar_fields = [ inicio and u'Bem-vindo ao HandTalks!' or u"Altera��es efetuadas com sucesso.",
                                    self.serial.portstr,
                                    str(self.serial.baudrate),
                                    str(self.serial.bytesize),
                                    self.serial.parity,
                                    str(self.serial.stopbits),
                                    (self.serial.rtscts and 'RTS/CTS ' or '') +
                                    (self.serial.xonxoff and 'XON/XOFF' or '') ]
        for i in range(len(janela_statusbar_fields)):
            self.janela_statusbar.SetStatusText(janela_statusbar_fields[i], i)

    def reportaErro (self, frase=''):
        self.janela_statusbar.SetStatusText(frase, 0)


    def configuraSerial(self, event): # wxGlade: JanelaPrincipal.<event_handler>
        if self.serial.isOpen():
            self.alternaComunicacao (event)

        dlg = ConfigSerial (None, -1, "", serial=self.serial)
        
        if (dlg.ShowModal() == wx.ID_OK):
            self.atualizaStatusSerial()
        else:
            self.reportaErro (u"Opera��o cancelada!")

        dlg.Destroy()

        
    def trocouLetra(self, event): # wxGlade: JanelaPrincipal.<event_handler>
        letra = self.caixaLetras.GetStringSelection()
        
        self.letraExibida.SetLabel (letra)
        self.reportaErro(u'Reproduzindo �udio...')

        if not self.IsMaximized():
            self.GetSizer().SetSizeHints(self)
            self.Refresh()
            self.Update()
        
        if tocador.toca_tudo ("audio/" + letra):
            self.reportaErro()
        else:
            self.reportaErro(u'Falha na execu��o!')


    def fechaAplicacao(self, event): # wxGlade: JanelaPrincipal.<event_handler>
        if event.CanVeto:
            dlg = wx.MessageDialog(self, u"Tem certeza que deseja sair?",
                                   u'Confirma��o',
                                   wx.YES_NO | wx.ICON_QUESTION
                                   )
            veta = dlg.ShowModal() == wx.ID_NO
            dlg.Destroy()
            if veta:
                return

        self.StopThread()               #stop reader thread
        self.serial.close()             #cleanup
        self.Destroy()


    def sair(self, event): # wxGlade: JanelaPrincipal.<event_handler>
        self.Close()


    def enviarComando(self, event): # wxGlade: JanelaPrincipal.<event_handler>
        self.reportaErro()
        if not self.serial.isOpen():
            self.reportaErro(u"Porta n�o est� aberta!")
            return
            
        self.serial.write (str(self.comando.GetValue()) + '\r\n')

        self.historico.AppendText ('<- ' + str(self.comando.GetValue()) + '\r\n')
        self.comando.SetSelection (-1, -1)
        self.comando.SetFocus ()


    def alternaComunicacao(self, event): # wxGlade: JanelaPrincipal.<event_handler>

"""
        max = 80

        dlg = wx.ProgressDialog("Aguarde...",
                               "Abrindo/Fechando a porta serial.",
                               maximum = max,
                               parent=self,
                               style = wx.PD_APP_MODAL
                                | wx.PD_ELAPSED_TIME
                                #| wx.PD_ESTIMATED_TIME
                                | wx.PD_REMAINING_TIME
                                )

        keepGoing = True
        count = 0

        while keepGoing and count < max:
            count += 1
            wx.MilliSleep(250)

            if count >= max / 2:
                keepGoing = dlg.Update(count, "Half-time!")
            else:
                keepGoing = dlg.Update(count)

        dlg.Destroy()
"""
        comunica = not self.serial.isOpen()
        self.reportaErro()
        
        try:
            try:
                if comunica:
                    self.serial.open()
                    self.StartThread()
                else:
                    self.StopThread()
                    self.serial.close()
            except:
                comunica = not comunica
                self.reportaErro(u"Erro ao abrir a porta!")
        finally:
            self.janela_toolbar.ToggleTool (ID_COMUNIC, comunica)
            self.janela_menubar.Check (ID_COMUNIC, comunica)
            self.enviar.Enable (comunica)
            self.resposta.Enable (comunica)
            self.historico.Enable (comunica)


    def sobreHandtalks(self, event): # wxGlade: JanelaPrincipal.<event_handler>
        dlg = wx.MessageDialog(self,
u"""HandTalks!
Vers�o 0.2

Tradutor do alfabeto LIBRAS.

Alunos: Andr�, Hilton e Hugo.
Orientador: Prof. Jorge Kinoshita""",
                                'Sobre...', wx.OK | wx.ICON_INFORMATION )
        dlg.ShowModal()
        dlg.Destroy()

    def StartThread(self):
        """Start the receiver thread"""        
        self.alive.set()
        self.thread = threading.Thread(target=self.ComPortThread)
        self.thread.setDaemon(1)
        self.thread.start()

    def StopThread(self):
        """Stop the receiver thread, wait util it's finished."""
        if self.thread is not None:
            self.alive.clear()          #clear alive event for thread
            self.thread.join()          #wait until thread has finished
            self.thread = None
        
    def OnSerialRead(self, event):
        """Handle input from the serial port."""
        text = ''.join([(c >= ' ') and c or '<%d>' % ord(c)  for c in event.data])
        self.resposta.SetValue (text)
        self.historico.AppendText ('-> ' + text + '\n')

    def ComPortThread(self):
        """Thread that handles the incomming traffic. Does the basic input
           transformation (newlines) and generates an SerialRxEvent"""
        text = ''
        while self.alive.isSet():               #loop while alive event is true
            char = self.serial.read(1)          #read one, with timout
            if char:                            #check if not timeout
                if char == '\n' or char == '\r':
                    if text:
                        event = SerialRxEvent(self.GetId(), text)
                        self.GetEventHandler().AddPendingEvent(event)
                        text = ''
                else:
                    text += char


# end of class JanelaPrincipal


