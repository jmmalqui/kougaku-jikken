from mesa import *
import pygame as pg

class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(30)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        #self.border("black", 2)
        self.center_text()
        self.parent.add_element(self)
    
class CustomBox(MesaStackVertical):
    def __init__(self, parent, width, height, color) -> None:
        super().__init__(parent)
        self.set_fixed_width(width)
        self.set_fixed_height(height)
        self.set_background_color(color)
        

class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#E6E6E6")
        self.container = MesaStackVertical(self)
        self.title=Title(self.container,"Renteck")
        self.whitebox=CustomBox(self.container,30,30,"white")
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
