from mesa import *
import pygame as pg
import random


class CustomText(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F8FFE5")
        self.border("black", 2)
        self.center_text()
        self.parent.add_element(self)


class CustomTitle(MesaTextLabel):
    def __init__(self, parent, text, width) -> None:
        super().__init__(parent)
        self.set_fixed_width(width)
        self.set_fixed_height(20)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("white")
        self.set_text(text)
        self.set_background_color("#141115")
        self.border("black", 2)
        self.center_text()
        self.parent.add_element(self)


class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("white")
        self.set_text(text)
        self.set_background_color("#D80032")
        self.border("black", 2)
        self.center_text()
        self.parent.add_element(self)


class MyButton(MesaButtonText):
    def __init__(
        self, parent, text, textcolor, bgcolor, displ_msg, bordercolor
    ) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(40)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.border(bordercolor, 2)
        self.center_text()
        self.parent.add_element(self)
        self.displ_msg = displ_msg
        self.set_signal(self.show_press)

    def show_press(self):
        self.scene.informer.inform(self.displ_msg)


class DescriptorVerticalPanel(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(200)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.cus = CustomTitle(self, "MesaStackVertical", 200)
        self.description = CustomText(self, "コンポネントを縦に揃える。", 150)
        self.cus = CustomTitle(self, "MesaStackHorizontal", 200)
        self.description = CustomText(self, "コンポネントを横に揃える。", 150)
        self.cus = CustomTitle(self, "MesaButtonText", 200)
        self.description = CustomText(self, "普通のボタン", 30)
        self.button = MyButton(self, "押す", "white", "black", "押された(黒)", "white")
        self.button = MyButton(self, "押す", "black", "white", "押された（白）", "black")
        self.parent.add_element(self)


class DogImage(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(260)
        self.set_height_as_parent()
        self.set_background_color("#141115")
        self.set_image("res/wanchan.jpg")
        self.center_element()
        self.border("black", 2)
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()
        return super().late_init()


class DogImage2(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(260)
        self.set_height_as_parent()
        self.set_background_color("#141115")
        self.set_image("res/wanchan.jpg")
        self.center_element()
        self.border("black", 2)
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_height()
        return super().late_init()


class MyInputBox(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(25)
        self.set_width_as_parent()
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("black", 2)
        self.center_text_vertical()
        self.parent.add_element(self)


class AnimationZone(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_remaining_area()
        self.set_background_color("#071013")
        self.parent.add_element(self)
        self.anim = Animation()
        self.color = DynamicObject(self.anim, pg.Vector3(255, 255, 255))
        self.pos = DynamicObject(self.anim, pg.Vector2(60, 60))

    def update(self):
        self.anim.update()
        for event in self.scene.manager.get_events():
            if event.type == pg.MOUSEBUTTONDOWN:
                target = pg.Vector2(pg.mouse.get_pos()) - self.get_absolute_position()
                self.color.go_to(
                    pg.Vector3(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                    ),
                    50,
                    MesaAnimationCurves.EASE_IN_OUT_SINE,
                )
                self.pos.go_to(target, 50, MesaAnimationCurves.EASE_IN_OUT_EXPO)
        return super().update()

    def render(self):
        pg.draw.circle(
            self.surface, self.color.get_value(), self.pos.get_value(), 50, 0
        )
        return super().render()


class DescriptorMiddlePanel(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(520)
        self.set_height_as_parent()
        self.set_color_as_parent()
        self.cus = CustomTitle(self, "MesaImage", 520)
        self.dogcontainer = MesaStackHorizontal(self)
        self.dogcontainer.set_width_as_parent()
        self.dogcontainer.set_fixed_height(200)
        self.description = DogImage(self.dogcontainer)
        self.description = DogImage2(self.dogcontainer)
        self.add_element(self.dogcontainer)
        self.cus = CustomTitle(self, "MesaTextBoxInput", 520)
        self.description = CustomText(self, "テキスト入力", 30)
        self.cus = MyInputBox(self)
        self.cus = MyInputBox(self)

        self.cus = CustomTitle(self, "Animation", 520)
        self.animzone = AnimationZone(self)
        self.parent.add_element(self)


class Descriptor(MesaStackHorizontal):
    def __init__(
        self,
        parent,
    ) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_height_as_display()
        self.set_background_color("#2b2d42")
        self.vpanel = DescriptorVerticalPanel(self)
        self.mpanel = DescriptorMiddlePanel(self)

        self.parent.add_element(self)


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color([10, 10, 10])
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "コンポネントの種類")
        self.descriptor = Descriptor(self.container)

        self.container.set_as_core()
        self.container.build()


class MyApplication(MesaCore):
    def __init__(self) -> None:
        super().__init__()

        self.set_application_name("MyApp")
        self.set_rendering_flags(pg.SRCALPHA)
        self.set_display_size(720, 500)
        self.set_background_color("black")
        self.set_clock(60)
        self.main_scene = MainScene(self, "main2", self.scene_manager)
        self.scene_manager.set_init_scene("main2")


app = MyApplication()
app.run()
