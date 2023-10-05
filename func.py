def TelaDrawerConstrutor(self):
    self.root.ids.drawSc.clear_widgets()
    self.root.ids['drawSc'].add_widget(MDRaisedButton(
        text="Sortear\nJogador",
        font_size="20sp",
        pos_hint={"center_x": .5, "center_y": .5},
        size_hint=(.5, .4),
        on_release=lambda x: self.ButtonDrawer(),
    ))
    self.root.ids['drawSc'].add_widget(MDLabel(
        #######################################################
        id="DrLabel",
        text="teste",
        font_size="20sp",
        halign="center",
        pos_hint={"center_x": .5, "center_y": .2}
    ))