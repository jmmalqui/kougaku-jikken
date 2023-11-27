from mesa import *
import pygame as pg


sentence1 = (
    "※まだ会員登録は完了してません。\n\n"
    "ご登録いただいたメールアドレス宛に、本登録を行うためのメールをお送りいたしました。"
    "メール本文に記載されている認証コードを入力して会員登録を完了させてください。\n\n"
    "※本登録手続きメールが届かない場合、入力したメールアドレスが間違っている可能性があります。"
    "再度、最初から新規会員登録を行ってください"
)


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F6F6F6")
        self.container = MesaStackVertical(self)

        self.title1 = Title1(self.container, "仮登録完了")  # 上部ラベル
        self.title2 = Title2(self.container, "仮登録が完了しました")
        self.box = box(self.container)
        self.text2 = CustomText2(self.container, sentence1, 160)

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
        self.main_scene = MainScene(self, "main", self.scene_manager)
        self.scene_manager.set_init_scene("main")


# ラベル（上部）
class Title1(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)

        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        self.center_text()
        self.parent.add_element(self)


# テキスト（仮登録が完了しました）
class Title2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()

        self.set_fixed_height(60)
        self.set_margin(50, 0)

        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.center_text()
        self.parent.add_element(self)


class CustomText1(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(20, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.center_text()
        self.parent.add_element(self)


class MyInputBox1(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(50)
        self.set_width_as_parent()
        self.set_margin(70, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("gray", 1)
        self.center_text_vertical()
        self.parent.add_element(self)


class MyButton1(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(77)
        self.set_margin(70, 15)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        ...


# テキスト（sentence1）
class CustomText2(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        # self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_fixed_width(360)
        self.set_margin(20, 0)
        # self.set_margin(0,)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(10)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.center_text()
        self.parent.add_element(self)


class box(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(180)
        self.set_color_as_parent()
        self.text1 = CustomText1(self, "認証コードを入力してください", 30)
        self.input = MyInputBox1(self)
        self.MyButton1 = MyButton1(self, "本登録へ進む", "white", "black")
        self.set_margin(0, 15)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)


app = MyApplication()
app.run()
