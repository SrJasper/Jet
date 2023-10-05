from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
import random as rd
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen

Window.size = (300, 500)
Builder.load_file("KV.kv")

class MontadorTime(MDScreen):
    pass
class TelaListaTimes(MDScreen):
    pass
class PLScreen (MDScreen):
    pass
class Ger(MDScreenManager):
    pass
class ContentNavigationDrawer(MDBoxLayout):
    pass

class JeT(MDApp):
    c = 0
    jogadores = []
    jog = []
    locais = []
    loc = []
    jogos = []
    jogosAUX = []



    #############################   Manipulando os arquivos txt   #############################
    def on_start(self):
        pass
        nomes = open("nomes.txt", "r")
        self.jogadores = nomes.readline()
        self.jogadores = self.jogadores.split(",")
        if self.jogadores[-1] == "":
            self.jogadores.pop(-1)
        nomes.close()

        loc = open("Jogos.txt", "r")
        self.locais = loc.readline()
        self.locais = self.locais.split(",")
        if self.locais[-1] == "":
            self.locais.pop(-1)
        loc.close()

        loc = open("Locais.txt", "r")
        self.jogos = loc.readline()
        self.jogos = self.jogos.split(",")
        if self.jogos[-1] == "":
            self.jogos.pop(-1)
        loc.close()
    def on_stop(self):
        nomes = open("nomes.txt", "w")
        for i in self.jogadores:
            nomes.write(i + ",")
        nomes.close()
        loc = open("Jogos.txt", "w")
        for i in self.locais:
            loc.write(i + ",")
        loc.close()
        loc = open("Locais.txt", "w")
        for i in self.jogos:
            loc.write(i + ",")
        loc.close()
    #############################   Manipulando os arquivos txt   #############################

    #############################   Setando os jogadores   #############################
    def At(self, nome):
        self.root.ids['lista'].add_widget(MDLabel(
            text=nome,
            pos_hint={"center_x": .35, "center_y": .8 - self.c},
            halign="center",
        ))
        self.root.ids['lista'].add_widget(MDIconButton(
            icon="minus-circle",
            icon_size="20sp",
            pos_hint={"center_x": .8, "center_y": .8 - self.c},
            halign="center",
            on_release=lambda x: self.remPlayer(nome)
        ))
    def onNomes(self):
        self.c = 0
        self.root.ids.lista.clear_widgets()
        for i in self.jogadores:
            self.At(i)
            self.c += 0.06
    def addPlayer(self, nome):
        self.jogadores.append(nome)
        self.onNomes()
    def remPlayer(self, nome):
        self.jogadores.remove(nome)
        self.onNomes()
    def restaurarJogadores(self):
        self.jog = []
        for i in self.jogadores:
            self.jog.append(i)
        ####Opah
        self.root.ids.ButtonDrawerId.text = "Sortear\nJogador"
    #############################   Setando os jogadores   #############################

    #############################   Setando os locais   #############################
    def AtualizaLocais(self, local):
        self.root.ids['LayoutLocais'].add_widget(MDLabel(
            text=local,
            pos_hint={"center_x": .4, "center_y": .8 - self.c},
            halign="center",
        ))
        self.root.ids['LayoutLocais'].add_widget(MDIconButton(
            icon="minus-circle",
            icon_size="20sp",
            pos_hint={"center_x": .8, "center_y": .8 - self.c},
            halign="center",
            on_release=lambda x: self.remLocal(local)
        ))
    def AbrirLocais(self):
        self.c = 0
        self.root.ids.LayoutLocais.clear_widgets()
        for i in self.locais:
            self.AtualizaLocais(i)
            self.c += 0.06
    def restaurarLocais(self):
        self.loc = []
        for i in self.locais:
            self.loc.append(i)
    def addLocal(self, local):
        self.locais.append(local)
        self.AbrirLocais()
    def remLocal(self, local):
        self.locais.remove(local)
        self.AbrirLocais()
    #############################   Setando os locais   #############################

    #############################   Setando os locais   #############################
    def AtualizaJogos(self, jogo):
        self.root.ids['LayoutJogos'].add_widget(MDLabel(
            text=jogo,
            pos_hint={"center_x": .4, "center_y": .8 - self.c},
            halign="center",
        ))
        self.root.ids['LayoutJogos'].add_widget(MDIconButton(
            icon="minus-circle",
            icon_size="20sp",
            pos_hint={"center_x": .8, "center_y": .8 - self.c},
            halign="center",
            on_release=lambda x: self.remJogo(jogo)
        ))
    def AbrirJogos(self):
        self.c = 0
        self.root.ids.LayoutJogos.clear_widgets()
        for i in self.jogos:
            self.AtualizaJogos(i)
            self.c += 0.06
    def restaurarJogos(self):
        self.jogosAUX = []
        for i in self.jogos:
            self.jogosAUX.append(i)
    def addJogo(self, jogo):
        self.jogos.append(jogo)
        self.AbrirJogos()
    def remJogo(self, jogo):
        self.jogos.remove(jogo)
        self.AbrirJogos()
    #############################   Setando os locais   #############################

    spy = []
    locSec = []
    lad = []
    pes = True

    def comecar(self, jogo):
        lad = []
        self.restaurarJogadores()
        self.restaurarLocais()
        if jogo == "Espião":
            self.root.current = "Spy"
            self.spy = rd.choice(self.jogadores)
            self.locSec = rd.choice(self.jogos)
            self.root.ids.SpyText.text = self.jogadores[0]
            self.cont = 0
            self.pes = True


        elif jogo == "Povo e ladrão":
            self.root.current = "PL"
            self.root.ids.PL.ids.jogador.text = self.jogadores[0]
            self.lad = int(len(self.jogadores)/4)
            for i in range(2):
                lad.append(rd.choice(self.jog))
                self.jog.remove(lad[i])
            self.lad = lad
            self.cont = 0
            self.pes = True

        elif jogo == "Drawer":
            self.root.current = "Drawer"
        elif jogo == "Times":
            self.root.current = "MontTimes"

    jogsTime = 0
    #############################   Lógica do "Times"   #############################
    def SortTimes(self):
        self.root.ids.TelaTimes.ids.listaTime.clear_widgets()
        self.restaurarJogadores()
        self.SortJogo()
        c = 0
        times = ("3659b1", "ff2a00", "008f3d", "ff9601")
        timeCor = 0
        cont = 0
        for x in self.jogadores:
            if timeCor > 3:
                timeCor = 0
            i = rd.choice(self.jog)
            self.root.ids.TelaTimes.ids.listaTime.add_widget(MDLabel(
                text=i,
                pos_hint={"center_x": .5, "center_y": .75 - c},
                halign="center",
                theme_text_color="Custom",
                text_color=times[timeCor]
            ))
            cont+=1
            if cont == int(self.jogsTime):
                cont = 0
                timeCor += 1
                c+= 0.03

            if self.jog:
                self.jog.remove(i)
            c += 0.04
        else:
            timeCor = 0
            cont = 0
    def ButtonTim(self):
        self.jogsTime = self.root.ids.MontTimes.ids.jogsPorTime.text
        self.root.current = "TelaTimes"
        self.SortTimes()
    def SortJogo(self):
        if self.loc:
            i = rd.choice(self.loc)
            self.root.ids.TelaTimes.ids.listaTime.add_widget(MDLabel(
                text=str(i),
                pos_hint={"center_x": .5, "center_y": .85},
                halign="center",
                theme_text_color="Custom",
                text_color="white"
            ))
            self.loc.remove(i)
            if not self.loc:
                self.restaurarLocais()
    #############################   Lógica do "Times"   #############################


    #############################   Lógica do "Drawer"   #############################
    def ButtonDrawer(self):
        if self.jog:
            i = rd.choice(self.jog)
            self.root.ids.DrLabel.text = i
            self.jog.remove(i)
            if not self.jog:
                self.root.ids.ButtonDrawerId.text = "Voltar"
        elif self.root.ids.ButtonDrawerId.text == "Voltar":
            self.root.current = "nomes"
            self.root.ids.ButtonDrawerId.text = "Sortear\nJogador"
        else:
            self.root.ids.ButtonDrawerId.text = "Voltar"
    #############################   Lógica do "Drawer"   #############################

    r = 0
    cont = 0
    #############################   Lógica do Povo e Ladrão   #############################
    def JogButton(self):
        if self.pes:
            self.r = 0
            for i in self.lad:
                if str(self.root.ids.PL.ids.jogador.text) == i:
                    self.r += 1
            if self.r == 0:
                self.root.ids.PL.ids.jogador.text = "Povo"
            else:
                self.root.ids.PL.ids.jogador.text = "Ladrão"
            self.pes = False
            self.cont += 1
        else:
            if self.cont < len(self.jogadores):
                self.root.ids.PL.ids.jogador.text = self.jogadores[self.cont]
            else:
                self.root.current = "nomes"
            self.pes = True
    #############################   Lógica do Povo e Ladrão   #############################

    #############################   Lógica do Espião   #############################
    def Spy(self):
        if self.pes:
            if self.root.ids.SpyText.text == self.spy:
                self.root.ids.SpyText.text = "Espião"
            else:
                self.root.ids.SpyText.text = str(self.locSec)

            self.pes = False
            self.cont += 1

        else:
            if self.cont < len(self.jogadores):
                self.root.ids.SpyText.text = self.jogadores[self.cont]
            else:
                self.root.current = "nomes"
            self.pes= True

    #############################   Lógica do Espião   #############################




    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return Ger()


JeT().run()