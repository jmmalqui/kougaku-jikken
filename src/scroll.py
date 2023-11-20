from mesa import *
import pygame as pg


class NormalText(MesaTextLabel):
    def __init__(self, parent, message) -> None:
        super().__init__(parent)
        self.set_fixed_width(100)
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("#463f3a")
        self.set_text(message)
        self.set_bold()
        self.set_color_as_parent()
        self.set_margin(5, 5)
        self.center_text()
        self.center_vertical()
        self.parent.add_element(self)


class DogVerticalScroller(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(300)
        self.set_fixed_height(150)
        self.set_margin(20, 20)
        self.center_horizontal()
        self.set_color_as_parent()
        self.border("#bcb8b1", 2)

        """この関数さえ入れたらスクロール機能が有効となる"""
        self.enable_scrolling()

        self.text1 = NormalText(self, "か")
        self.text1 = NormalText(self, "き")
        self.text1 = NormalText(self, "く")
        self.dog = MovingDogButton(self, "res/wanchan.jpg")
        self.text1 = NormalText(self, "け")
        self.text1 = NormalText(self, "こ")
        self.text1 = NormalText(self, "?")
        self.parent.add_element(self)


class MovingDogButton(MesaImageButton):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_margin(3, 3)
        self.set_fixed_height(90)
        self.set_fixed_width(90)
        self.pathimage = image
        self.set_image(image)
        self.set_color_as_parent()
        self.center_vertical()
        self.center_element()
        self.set_signal(self.add)
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_height()

        return super().late_init()

    def update(self):
        return super().update()

    def add(self):
        self.scene.dogimage.update_image(self.pathimage)


class TitleText(MesaTextLabel):
    def __init__(self, parent, message) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_parent()
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(18)
        self.set_text_color("#463f3a")
        self.set_text(message)
        self.set_bold()
        self.set_color_as_parent()
        self.set_margin(5, 5)
        self.center_text()
        self.center_vertical()
        self.parent.add_element(self)


class Title(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(50)
        self.set_color_as_parent()
        self.border_down("#bcb8b1", 2)
        self.container = self.parent
        self.message = TitleText(self, "Dog Collection")
        self.set_margin(5, 5)
        self.parent.add_element(self)


class DogImage(MesaImage):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(300)
        self.set_color_as_parent()
        self.set_image(self.parent.parent.dogselector.dog1.pathimage)
        self.center_element()
        self.set_margin(40, 40)
        self.center_vertical()
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()

        return super().late_init()

    def update_image(self, image):
        self.set_image(image)
        self.center_element()
        self.resize_match_parent_width()


class DogSelectorPanel(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(100)
        self.set_color_as_parent()
        self.set_margin(10, 10)
        """この関数さえ入れたらスクロール機能が有効となる"""
        self.enable_scrolling()
        self.dog1 = MovingDogButton(self, "res/wanchan.jpg")
        self.dog2 = MovingDogButton(self, "res/wanchan2.jpeg")
        self.dog3 = MovingDogButton(self, "res/wanchan3.jpeg")
        self.dog5 = MovingDogButton(self, "res/wanchan5.jpeg")
        self.dog1 = MovingDogButton(self, "res/wanchan.jpg")
        self.dog2 = MovingDogButton(self, "res/wanchan2.jpeg")
        self.dog3 = MovingDogButton(self, "res/wanchan3.jpeg")
        self.dog1 = MovingDogButton(self, "res/wanchan.jpg")
        self.dog2 = MovingDogButton(self, "res/wanchan2.jpeg")
        self.dog3 = MovingDogButton(self, "res/wanchan3.jpeg")
        self.parent.add_element(self)


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#f4f3ee")
        self.container = MesaStackVertical(self)
        self.container.set_color_as_parent()
        self.internal = Title(self.container)
        self.dogselector = DogSelectorPanel(self.container)
        self.dogimage = DogImage(self.container)
        self.dogscroll = DogVerticalScroller(self.container)
        self.container.set_as_core()
        self.container.build()

        self.animator = Animation()
        self.hand_position = DynamicObject(self.animator, pg.Vector2(450, 140))
        self.hand_position2 = DynamicObject(self.animator, pg.Vector2(450, 840))

        self.hand = load_image("res/tap.png")
        self.hand = resize(self.hand, [50, 50])

        self.hand2 = load_image("res/tap.png")
        self.hand2 = resize(self.hand, [50, 50])

        self.HANDANIMATION = pg.USEREVENT
        pg.time.set_timer(self.HANDANIMATION, 3000)
        self.hand_position.pulse(
            pg.Vector2(450, 240),
            pg.Vector2(250, 140),
            pg.Vector2(60, 140),
            120,
            120,
            MesaAnimationCurves.EASE_OUT_BACK,
            MesaAnimationCurves.EASE_IN_BACK,
        )
        self.hand_position2.pulse(
            pg.Vector2(-150, 740),
            pg.Vector2(130, 550),
            pg.Vector2(130, 450),
            120,
            120,
            MesaAnimationCurves.EASE_OUT_BACK,
            MesaAnimationCurves.EASE_IN_BACK,
        )

    def update(self):
        self.animator.update()
        for event in self.manager.get_events():
            if event.type == self.HANDANIMATION:
                self.hand_position.pulse(
                    pg.Vector2(450, 240),
                    pg.Vector2(250, 140),
                    pg.Vector2(60, 140),
                    120,
                    120,
                    MesaAnimationCurves.EASE_OUT_BACK,
                    MesaAnimationCurves.EASE_IN_BACK,
                )
                self.hand_position2.pulse(
                    pg.Vector2(-150, 740),
                    pg.Vector2(130, 550),
                    pg.Vector2(130, 450),
                    120,
                    120,
                    MesaAnimationCurves.EASE_OUT_BACK,
                    MesaAnimationCurves.EASE_IN_BACK,
                )
        return super().update()

    def render(self):
        self.surface.blit(self.hand, self.hand_position.get_value())
        self.surface.blit(self.hand2, self.hand_position2.get_value())

        return super().render()


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
