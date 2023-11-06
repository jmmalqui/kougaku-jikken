from mesa import *
import pygame as pg


class Item(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_margin(10, 0)
        self.set_height_as_parent()
        self.set_fixed_width(100)
        self.set_image("res/wanchan.jpg")
        self.set_background_color("black")
        self.center_element()
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_height()
        return super().late_init()

    def update(self):
        if self._is_container_hovered():
            self.border("white", 5)
        else:
            self.borderless()
        return super().update()


class SubInternal(MesaStackVertical):
    def __init__(self, parent, margin) -> None:
        super().__init__(parent)
        self.margin = margin
        self.set_height_as_parent()
        self.set_fixed_width(50)
        self.set_background_color("blue")
        self.parent.add_element(self)


class InternalPadding(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(100)
        self.set_background_color("lightgreen")
        self.item = Item(self)
        self.set_margin(0, 5)
        self.parent.add_element(self)


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("red")
        self.container = MesaStackVertical(self)
        self.internal = InternalPadding(self.container)
        self.internal = InternalPadding(self.container)
        self.internal = InternalPadding(self.container)
        self.internal = InternalPadding(self.container)

        self.container.set_as_core()
        self.container.build()


class MyApplication(MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("MyApp")
        self.set_rendering_flags(pg.SRCALPHA, pg.RESIZABLE)
        self.set_display_size(360, 600)
        self.set_background_color("black")
        self.set_clock(60)
        self.main_scene = MainScene(self, "main2", self.scene_manager)
        self.scene_manager.set_init_scene("main2")


app = MyApplication()
app.run()
