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

class calendarTitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(32)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(21)
        self.set_text_color("black")
        self.set_text("レンタル期間選択")
        #self.border("black", 2)
        self.set_color_as_parent()
        self.center_text()
        self.parent.add_element(self)

class NormalText(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(18)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text("レンタル開始日時と終了日時を選択してください")
        self.set_color_as_parent()
        self.center_text()
        self.set_margin(0,2)
        #self.center_vertical()
        self.parent.add_element(self)

class textbox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(75)
        self.set_color_as_parent()
        self.title=calendarTitle(self)
        self.text=NormalText1(self)
        self.parent.add_element(self)
        self.set_margin(0,12)

class NormalText1(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(18)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text("レンタル開始日時と終了日時を選択してください")
        self.set_color_as_parent()
        self.center_text()
        self.set_margin(0,2)
        #self.center_vertical()
        self.parent.add_element(self)

class NormalText2(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(160)
        self.set_fixed_height(27)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("black")
        self.set_text("●レンタル開始日時")
        self.set_color_as_parent()
        self.set_margin(20,2)
        self.parent.add_element(self)

class rentarubox(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(75)
        self.set_color_as_parent()
        self.start=NormalText2(self)
        self.parent.add_element(self)
        self.set_margin(0,12)

class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_parent()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()
        self.text1=textbox(self)
        self.text2=rentarubox(self)
        self.parent.add_element(self)

class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F3F3F3")
        self.container = MesaStackVertical(self)
        self.title=Title(self.container, "Renteck")
        self.scroll=scroll(self.container)
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
