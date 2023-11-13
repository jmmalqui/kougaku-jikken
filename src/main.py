from mesa import *
import pygame as pg
import scene_0
import scene_1
import scene_reg1
import scene_reg2
import scene_reg3


class MyApplication(MesaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("MyApp")
        self.set_rendering_flags(pg.SRCALPHA)
        self.set_display_size(360, 600)
        self.set_background_color("black")
        self.set_clock(60)
        self.init_scene = scene_0.MainScene(self, "init", self.scene_manager)
        self.registration = scene_reg1.MainScene(self, "regist", self.scene_manager)
        self.items = scene_1.MainScene(self, "items", self.scene_manager)
        self.new_register = scene_reg2.MainScene(self, "newreg", self.scene_manager)
        self.register_finish = scene_reg3.MainScene(
            self, "regist-end", self.scene_manager
        )
        self.scene_manager.set_init_scene("items")


app = MyApplication()
app.run()
