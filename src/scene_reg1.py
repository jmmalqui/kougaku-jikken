from mesa import *
import pygame as pg


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F6F6F6")
        self.container = MesaStackVertical(self)

        self.title1 = Title1(self.container,'ログイン') #上部ラベル
        self.MyButton1 = MyButton1(self.title1,'＜',"#818181","white")
        self.title2 = Title2(self.container,'Renteck')#RRenteck
        self.text1 = CustomText1(self.container,'メールアドレス',30)

        self.input1 = MyInputBox1(self.container)
        self.text2 = CustomText2(self.container, "パスワード", 30)
        self.input2 = MyInputBox2(self.container)

        self.MyButton2 = MyButton2(self.container, "ログイン", "white", "black")
        self.text2 = CustomText3(self.container, "アカウントをお持ちでない方", 15)
        self.MyButton3 = MyButton3(self.container, "新規会員登録", "blue", "#F6F6F6")

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


# 戻るボタン（画面左上）
class MyButton1(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_fixed_height(60)
        self.set_fixed_width(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    # ボタンが押されたときの処理（前画面に戻る）
    def show_press(self):
        ...


# Renteck文字
class Title2(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_height(120)
        self.set_width_as_display()
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(55)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.center_text()
        self.parent.add_element(self)


# テキスト（メールアドレス）
class CustomText1(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(30, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)


# 入力テキストボックス（メールアドレス）
class MyInputBox1(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(50)
        self.set_width_as_parent()
        self.set_margin(30, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("gray", 1)
        self.center_text_vertical()
        self.parent.add_element(self)


# テキスト（パスワード）
class CustomText2(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(30, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)


# 入力テキストボックス（パスワード）
class MyInputBox2(MesaTextBoxInput):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_height(50)
        self.set_width_as_parent()
        self.set_margin(30, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("gray", 1)
        self.center_text_vertical()
        self.parent.add_element(self)


# ログインボタン
class MyButton2(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(150)
        self.set_margin(100, 50)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(20)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.parent.add_element(self)
        self.set_signal(self.show_press)


# テキスト（アカウントをお持ちでない方）
class CustomText3(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.center_text()
        self.parent.add_element(self)


class MyButton3(MesaButtonText):
    def __init__(self, parent, text, textcolor, bgcolor) -> None:
        super().__init__(parent)
        self.set_fixed_width(360)
        self.set_fixed_height(18)
        self.set_margin(140, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color(textcolor)
        self.set_text(text)
        self.set_background_color(bgcolor)
        self.center_text()
        self.border_down("blue", 1)
        self.parent.add_element(self)
        self.set_signal(self.show_press)

    def show_press(self):
        ...


app = MyApplication()
app.run()
