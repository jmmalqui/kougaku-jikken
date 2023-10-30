from mesa import *
import pygame as pg


class TextLabel(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(50)
        self.set_fixed_width(150)
        self.set_font_name("Arial")
        self.set_font_size(12)
        self.set_text_color("white")
        self.set_background_color("white")
        self.border("black", 2)

class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.text = TextLabel(self.container)
        self.container.add_element(self.text)
        self.container.set_as_core()
        self.container.build()

class MyApplication(MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("MyApp")
        self.set_rendering_flags(pg.SRCALPHA)
        self.set_display_size(360, 600)
        self.set_background_color("black")
        self.set_clock(60)
        self.main_scene = MainScene(self, "main2", self.scene_manager)
        self.scene_manager.set_init_scene("main2")

app = MyApplication()
app.run()
