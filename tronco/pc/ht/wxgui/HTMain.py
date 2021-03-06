#!/usr/bin/env python
# -*- coding: latin-1 -*-
# generated by wxGlade 0.4cvs on Thu Sep  1 12:47:22 2005

import wx
#import tocador
import serial
import threading
from HTSerialConfig import HTSerialConfig
from ht.HTTranslator import HTTranslator


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

ID_NOVO = wx.NewId()
ID_ABRIR = wx.NewId()
ID_GRAVAR = wx.NewId()
ID_GRAVAR_COMO = wx.NewId()
ID_AJUSTAR = wx.NewId()


TIMEOUT_SERIAL = 2 # segundos

"""
# Confere se est� na pasta wxgui
import sys,os
caminho=os.path.abspath (os.path.dirname (sys.argv[0]))
if not caminho.endswith ("wxgui"):
    caminho = os.path.join (caminho, "ht", "wxgui")
os.chdir (caminho)
"""

class HTMain(wx.Frame):
    def __init__(self, *args, **kwds):
        # �ltima leitura
        self.last_letter = ''
        self.last_valid_letter = ''
        self.letter_count = 0

        # Valores padr�es da serial
        self.serial = serial.Serial()
        self.serial.port = 0;
        self.serial.baudrate = 19200;
        self.serial.bytesize = 8;
        self.serial.parity = serial.PARITY_NONE;
        self.serial.stopbits = 1;
        self.serial.timeout = TIMEOUT_SERIAL;
        self.serial.rtscts = False;
        self.serial.xonxoff = False;

        # Tradutor
        contraido = [1, 2, 1, 1, 2]
        relaxado = [30, 30, 25, 20, 30]
        esticado = [180, 170, 180, 168, 120]
        self.translator = HTTranslator ()
        self.translator.adjust (esticado, relaxado, contraido)

        # Threading
        self.thread = None
        self.alive = threading.Event()               

        # begin wxGlade: HTMain.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.divisor = wx.SplitterWindow(self, -1, style=wx.SP_PERMIT_UNSPLIT)
        self.ladoDireito = wx.Panel(self.divisor, -1)
        self.ladoEsquerdo = wx.Panel(self.divisor, -1)
        self.sizerSaida_staticbox = wx.StaticBox(self.ladoEsquerdo, -1, u"Sa�da")
        self.sizerHistorico_staticbox = wx.StaticBox(self.ladoDireito, -1, u"Hist�rico")
        self.sizerEntrada_staticbox = wx.StaticBox(self.ladoEsquerdo, -1, "Entrada")
        
        # Menu Bar
        self.janela_menubar = wx.MenuBar()
        self.SetMenuBar(self.janela_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_NOVO, "&Novo", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_ABRIR, "&Abrir...", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_GRAVAR, "&Gravar", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(ID_GRAVAR_COMO, "Gravar &Como...", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_AJUSTAR, "Ajus&tar...", "", wx.ITEM_NORMAL)
        self.janela_menubar.Append(wxglade_tmp_menu, u"&Usu�rios")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_CONFIG, "Confi&gurar...", "Ajusta detalhes da porta serial", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_COMUNIC, "&Comunicar", u"Inicia/Interrompe comunica��o", wx.ITEM_CHECK)
        self.janela_menubar.Append(wxglade_tmp_menu, u"&Comunica��o")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(ID_SOBRE, "So&bre...", u"Informa��es sobre o HandTalks!", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(ID_SAIR, "&Sair", "Fecha o HandTalks!", wx.ITEM_NORMAL)
        self.janela_menubar.Append(wxglade_tmp_menu, "&Geral")
        # Menu Bar end
        self.janela_statusbar = self.CreateStatusBar(7, wx.ST_SIZEGRIP)
        
        # Tool Bar
        self.janela_toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT|wx.TB_DOCKABLE)
        self.SetToolBar(self.janela_toolbar)
        self.janela_toolbar.AddLabelTool(ID_ABRIR, u"Abrir usu�rio...", wx.Bitmap("imagem/Abrir.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Abrir usu�rio...", u"Carrega os ajustes da luva de um usu�rio")
        self.janela_toolbar.AddLabelTool(ID_GRAVAR, u"Gravar usu�rio...", wx.Bitmap("imagem/Gravar.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, u"Gravar usu�rio...", u"Grava os ajustes da luva de um usu�rio")
        self.janela_toolbar.AddSeparator()
        self.janela_toolbar.AddLabelTool(ID_AJUSTAR, "Ajustar...", wx.Bitmap("imagem/Usuario.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Ajustar...", u"Faz o ajuste das letras com a m�o do usu�rio")
        self.janela_toolbar.AddSeparator()
        self.janela_toolbar.AddLabelTool(ID_CONFIG, "Configurar...", wx.Bitmap("imagem/Config.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Configurar...", "Ajusta detalhes da porta serial")
        self.janela_toolbar.AddLabelTool(ID_COMUNIC, "Comunicar", wx.Bitmap("imagem/Parado.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Comunicar", u"Inicia/Interrompe comunica��o")
        self.janela_toolbar.AddSeparator()
        self.janela_toolbar.AddLabelTool(ID_SOBRE, "Sobre...", wx.Bitmap("imagem/Info.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Sobre...", u"Informa��es sobre o HandTalks!")
        self.janela_toolbar.AddLabelTool(ID_SAIR, "Sair", wx.Bitmap("imagem/Fechar.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Sair", "Fecha o HandTalks!")
        # Tool Bar end
        self.resposta = wx.TextCtrl(self.ladoEsquerdo, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.letraExibida = wx.StaticText(self.ladoEsquerdo, -1, "A", style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
        self.historico = wx.TextCtrl(self.ladoDireito, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.btLimpar = wx.Button(self.ladoDireito, -1, "Limpar")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.configuraSerial, id=ID_CONFIG)
        self.Bind(wx.EVT_MENU, self.alternaComunicacao, id=ID_COMUNIC)
        self.Bind(wx.EVT_MENU, self.sobreHandtalks, id=ID_SOBRE)
        self.Bind(wx.EVT_MENU, self.sair, id=ID_SAIR)
        self.Bind(wx.EVT_BUTTON, self.limpaHistorico, self.btLimpar)
        # end wxGlade

        # Mais eventos
        self.Bind(wx.EVT_CLOSE, self.fechaAplicacao)
        self.Bind(wx.EVT_MENU_HIGHLIGHT_ALL, self.mostraAjuda)
        self.Bind(wx.EVT_TOOL_ENTER, self.mostraAjuda)
        self.Bind(EVT_SERIALRX, self.OnSerialRead)

        # Associa um �cone
        ib = wx.IconBundle()
        ib.AddIconFromFile("imagem/handtalks.ico",wx.BITMAP_TYPE_ANY)
        self.SetIcons(ib)


    def __set_properties(self):
        # begin wxGlade: HTMain.__set_properties
        self.SetTitle("Hand Talks!")
        self.SetSize(wx.DLG_SZE(self, (340, 296)))
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DFACE))
        self.janela_statusbar.SetStatusWidths([-1, 80, 60, 20, 20, 20, 80])
        # statusbar fields
        janela_statusbar_fields = ["", "", "", "", "", "", ""]
        for i in range(len(janela_statusbar_fields)):
            self.janela_statusbar.SetStatusText(janela_statusbar_fields[i], i)
        self.janela_toolbar.SetToolBitmapSize((16, 16))
        self.janela_toolbar.Realize()
        self.resposta.SetToolTipString("Resposta da luva")
        self.resposta.Enable(False)
        self.letraExibida.SetFont(wx.Font(150, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, ""))
        self.historico.SetFont(wx.Font(30, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, ""))
        self.historico.SetToolTipString(u"Hist�rico da comunica��o com a luva")
        self.historico.Enable(False)
        # end wxGlade

        # Popula a caixa de letras
#        self.caixaLetras.AppendItems( [chr (ord('A') + x) for x in range (26)] )
#        self.caixaLetras.Select(0)
        
        # Vai ser um timer
        self.timerStatus = None

        # Barra de estado
        self.reportaErro (u'Bem-vindo ao HandTalks!')
        self.atualizaStatusSerial()


    def __do_layout(self):
        # begin wxGlade: HTMain.__do_layout
        sizerJanela = wx.BoxSizer(wx.HORIZONTAL)
        sizerHistorico = wx.StaticBoxSizer(self.sizerHistorico_staticbox, wx.VERTICAL)
        sizerPrincipal = wx.BoxSizer(wx.VERTICAL)
        sizerSaida = wx.StaticBoxSizer(self.sizerSaida_staticbox, wx.VERTICAL)
        sizerEntrada = wx.StaticBoxSizer(self.sizerEntrada_staticbox, wx.HORIZONTAL)
        sizerEntrada.Add(self.resposta, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 3)
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
        sizerHistorico.Add(self.btLimpar, 0, wx.ALL, 3)
        self.ladoDireito.SetAutoLayout(True)
        self.ladoDireito.SetSizer(sizerHistorico)
        sizerHistorico.Fit(self.ladoDireito)
        sizerHistorico.SetSizeHints(self.ladoDireito)
        self.divisor.SplitVertically(self.ladoEsquerdo, self.ladoDireito)
        sizerJanela.Add(self.divisor, 1, wx.ALL|wx.EXPAND, 3)
        self.SetAutoLayout(True)
        self.SetSizer(sizerJanela)
        self.Layout()
        self.Centre()
        # end wxGlade


    def mostraAjuda(self, event):
        try:
            msg = self.GetMenuBar().GetHelpString(event.GetId())
        except:
            try:
                msg = self.GetMenuBar().GetHelpString(event.GetSelection())
            except:
                msg = ''
        self.reportaErro (msg)


    def atualizaStatusSerial(self):
        janela_statusbar_fields = [ self.serial.portstr,
                                    str(self.serial.baudrate),
                                    str(self.serial.bytesize),
                                    self.serial.parity,
                                    str(self.serial.stopbits),
                                    (self.serial.rtscts and 'RTS/CTS ' or '') +
                                    (self.serial.xonxoff and 'XON/XOFF' or '') ]
        for i in range(len(janela_statusbar_fields)):
            self.janela_statusbar.SetStatusText(janela_statusbar_fields[i], i+1)

    def reportaErro (self, frase=''):
        self.janela_statusbar.SetStatusText(frase, 0)
        if len(frase) > 0:
            if self.timerStatus is not None:
                self.timerStatus.cancel()
            self.timerStatus = threading.Timer(3.0, self.reportaErro)
            self.timerStatus.start()


    def configuraSerial(self, event): # wxGlade: HTMain.<event_handler>
        if self.serial.isOpen():
            self.alternaComunicacao (event)

        dlg = HTSerialConfig (None, -1, "", serial=self.serial)
        
        if (dlg.ShowModal() == wx.ID_OK):
            self.atualizaStatusSerial()
        else:
            self.reportaErro (u"Opera��o cancelada!")

        dlg.Destroy()

    def exibeLetra (self, letra=None):
        if letra is None:
            letra = ''
            
        self.letraExibida.SetLabel (letra)
        self.reportaErro(u'Reproduzindo �udio...')


#        if not self.IsMaximized():
#            self.GetSizer().SetSizeHints(self)
#            self.Refresh()
#            self.Update()
        
        # Toca wav, mp3 etc, usando pymedia
#        if tocador.toca_tudo ("audio/" + letra):
#            self.reportaErro()
#        else:
#            self.reportaErro(u'Falha na execu��o!')

    def tocaLetra (self, letra=None):
        # Toca apenas wav, mas usa o pr�prio wxPython
        try:
            sound = wx.SoundFromData( open("audio/" + letra + ".wav", 'rb').read() )
            sound.Play(wx.SOUND_ASYNC)
            wx.YieldIfNeeded()
        except NotImplementedError, v:
            self.reportaErro(u'Recurso n�o implementado!')
        except IOError, v:
            self.reportaErro(u'Som n�o encontrado!')


        
    def trocouLetra(self, event): # wxGlade: HTMain.<event_handler>
#        letra = self.caixaLetras.GetStringSelection()
        self.exibeLetra (letra)
        

    def fechaAplicacao(self, event): # wxGlade: HTMain.<event_handler>
        if event.CanVeto:
            dlg = wx.MessageDialog(self, u"Tem certeza que deseja sair?",
                                   u'Confirma��o',
                                   wx.YES_NO | wx.ICON_QUESTION
                                   )
            veta = dlg.ShowModal() == wx.ID_NO
            dlg.Destroy()
            if veta:
                return
            
        if self.timerStatus is not None:
            self.timerStatus.cancel()
        self.alternaComunicacao (event, desejo=False) # For�a o "desligamento" da serial
        self.Destroy()


    def sair(self, event): # wxGlade: HTMain.<event_handler>
        self.Close()


    def enviarComando(self, event): # wxGlade: HTMain.<event_handler>
        if not self.serial.isOpen():
            self.reportaErro(u"Porta n�o est� aberta!")
            return
            
        self.serial.write (str(self.comando.GetValue()) + '\r\n')

#        self.historico.AppendText ('<- ' + str(self.comando.GetValue()) + '\r\n')
        self.comando.SetSelection (-1, -1)
        self.comando.SetFocus ()


    def alternaComunicacao(self, event, desejo=None): # wxGlade: HTMain.<event_handler>
        comunica = not self.serial.isOpen()
        if desejo is not None:
            if not comunica == desejo:
                return
        
        try:
            try:
                if comunica:
                    self.serial.open()
                    self.StartThread()
                else:
                    max = 10 * TIMEOUT_SERIAL
                    count = 0
                    dlg = wx.ProgressDialog("Aguarde...", "Fechando a porta serial.", maximum = max,
                                            parent = self, style = wx.PD_APP_MODAL)
                    while not self.StopThread():
                        if count < max-1:
                            count += 1
                        wx.MilliSleep(100)
                        keepGoing = dlg.Update(count)
                    dlg.Destroy()
                    
                    self.serial.close()
            except:
                comunica = not comunica
                self.reportaErro(u"Erro ao abrir a porta!")
        finally:
            self.janela_menubar.Check (ID_COMUNIC, comunica)
#            self.enviar.Enable (comunica)
            self.resposta.Enable (comunica)
            self.historico.Enable (comunica)
            if comunica:
                imagem = wx.Bitmap("imagem/Rodando.png", wx.BITMAP_TYPE_ANY)
            else:
                imagem = wx.Bitmap("imagem/Parado.png", wx.BITMAP_TYPE_ANY)
            self.janela_toolbar.FindById(ID_COMUNIC).SetBitmap1(imagem)
            self.janela_toolbar.ToggleTool (ID_COMUNIC, comunica)
            self.janela_toolbar.Realize()


    def sobreHandtalks(self, event): # wxGlade: HTMain.<event_handler>
        dlg = wx.MessageDialog(self,
u"""HandTalks!
Vers�o 0.5

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
        self.thread.setDaemon(True)
        self.thread.start()

    def StopThread(self):
        """Stop the receiver thread, return if it's finished."""
        vivo = False
        if self.thread is not None:
            if self.alive.isSet():
                self.alive.clear()          #clear alive event for thread
            vivo = self.thread.isAlive()
            if not vivo:
                self.thread = None
        return not vivo
        
    def OnSerialRead(self, event):
        """Handle input from the serial port."""
        # Extrai valores dos ADs
        fingers = [ int(x) for x in event.data[1:-3].split ('#') ]

        # Extrai valores dos contatos
        hex = int (event.data[-2], 16)
        contacts = []
        for i in range (4):
            bit = (hex & 2**i) > 0
            contacts.append (bit)

        result = self.translator.translate (fingers, contacts)
        text = ''.join([(' ' <= c < chr(128)) and c or '<%d>' % ord(c)  for c in event.data])
#        text += "\nContra�do:" + str(self.translator.u_in[0])
#        text += "\nRelaxado: " + str(self.translator.u_in[1])
#        text += "\nEsticado: " + str(self.translator.u_in[2])
#        text += "\nContra�do:" + 5*" %3.2f%%"
#        text += "\nRelaxado: " + 5*" %3.2f%%"
#        text += "\nEsticado: " + 5*" %3.2f%%"
#        lista = self.translator.u_in[0]
#        lista.extend (self.translator.u_in[1])
#        lista.extend (self.translator.u_in[2])
        self.resposta.SetValue (text)

        if result == self.last_letter:
            self.letter_count += 1
        else:
            self.last_letter = result
            self.letter_count = 1

        if self.letter_count == 20 and not result == self.last_valid_letter:
            if result is not None:
                self.tocaLetra (result)

                if result == 'CR':
                    result = '\n'
                    letra = u"\u21B5"
                elif result == 'VI':
                    result = letra = ','
                elif result == 'PT':
                    result = letra = '.'
                elif result == 'EX':
                    result = letra = '!'
                elif result == 'IN':
                    result = letra = '?'
                elif result == 'SP':
                    result = ' '
                    letra = '_'
                elif result == 'BS':
                    result = self.historico.GetValue()[:-1]
                    self.historico.Clear()
                    letra = u'\u2190'
                else:
                    letra = result
                    
                self.exibeLetra (letra)
                self.historico.AppendText (result)

            self.last_valid_letter = result
    # OnSerialRead


    def ComPortThread(self):
        """Thread that handles the incomming traffic. Does the basic input
           transformation (newlines) and generates an SerialRxEvent"""
        text = ''
        lastChar = ''
        while self.alive.isSet():               #loop while alive event is true
            char = self.serial.read(1)          #read one, with timout
            if char:                            #check if not timeout
                if char == '#' and lastChar == '#':
                    if text:
                        event = SerialRxEvent(self.GetId(), text)
                        self.GetEventHandler().AddPendingEvent(event)
                        text = ''
                else:
                    text += char

                lastChar = char
            


    def limpaHistorico(self, event): # wxGlade: HTMain.<event_handler>
        self.historico.Clear()

# end of class HTMain



