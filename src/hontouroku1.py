from mesa import *
import pygame as pg

sentence1="※仮登録の際に入力したメールアドレスを入力してください"


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("#F6F6F6")
        self.container = MesaStackVertical(self)
        self.title1 = Title1(self.container,'会員本登録') #上部ラベル
        self.text0 = CustomText0(self.container,'お客様情報を入力してください',50)
        self.box1=box1(self.container)
        self.box2=box2(self.container)
        self.box3=box3(self.container)
        self.MyButton2 = MyButton2(self.container,'確認画面へ',"white","black")
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

#ラベル（上部）
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

#テキスト
class CustomText0(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(30,15)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.center_text()
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)


#メールアドレス
class CustomText1a(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(110)
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)
class CustomText1b(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(40)
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("white")
        self.set_text(text)
        self.center_text()
        self.border("#F6F6F6",3)
        self.set_background_color("#DD4242")
        self.parent.add_element(self)
class MyInputBox1(MesaTextBoxInput):
    def __init__(self, parent,height) -> None:
        super().__init__(parent)
        self.set_fixed_height(height)
        self.set_width_as_parent()
        self.set_margin(0, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.parent.add_element(self)
class CustomText1d(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(10)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

class AnimationZone1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.text1a = CustomText1a(self,'メールアドレス',30)
        self.text1b = CustomText1b(self,'必須',27)
        self.set_height_as_remaining_area()
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

class box1(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(110)
        self.set_color_as_parent()
        self.yoko1=AnimationZone1(self)
        self.input1 = MyInputBox1(self,50)
        self.text1d = CustomText1d(self,sentence1,20)
        self.set_margin(30,5)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

#ニックネーム
class CustomText2a(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(94)
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)
class CustomText2b(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(40)
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("white")
        self.set_text(text)
        self.center_text()
        self.border("#F6F6F6",3)
        self.set_background_color("#DD4242")
        self.parent.add_element(self)
class MyInputBox2(MesaTextBoxInput):
    def __init__(self, parent,height) -> None:
        super().__init__(parent)
        self.set_fixed_height(height)
        self.set_width_as_parent()
        self.set_margin(0, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.parent.add_element(self)
class CustomText2c(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(10)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

class AnimationZone2(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.text2a = CustomText2a(self,'ニックネーム',30)
        self.text2b = CustomText2b(self,'必須',27)
        self.set_height_as_remaining_area()
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

class box2(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(105)
        self.set_color_as_parent()
        self.yoko2=AnimationZone2(self)
        self.input2 = MyInputBox2(self,50)
        self.text2c = CustomText2c(self,'　　　　　　　　　　　　　　　　　　　　　　　※10文字以内',15)
        self.set_margin(30,5)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

#パスワード
class CustomText3a(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(80)
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(15)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)
class CustomText3b(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_fixed_width(40)
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(13)
        self.set_text_color("white")
        self.set_text(text)
        self.center_text()
        self.border("#F6F6F6",3)
        self.set_background_color("#DD4242")
        self.parent.add_element(self)
class MyInputBox3(MesaTextBoxInput):
    def __init__(self, parent,height) -> None:
        super().__init__(parent)
        self.set_fixed_height(height)
        self.set_width_as_parent()
        self.set_margin(0, 0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/JetBrainsMonoNerdFont-LightItalic.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_background_color("white")
        self.border("#818181", 2)
        self.center_text_vertical()
        self.parent.add_element(self)
class CustomText3c(MesaTextLabel):
    def __init__(self, parent, text, height) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(height)
        self.set_margin(0,0)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(10)
        self.set_text_color("#0D1321")
        self.set_text(text)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

class AnimationZone3(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.text3a = CustomText3a(self,'パスワード',30)
        self.text3b = CustomText3b(self,'必須',27)
        self.set_height_as_remaining_area()
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)

class box3(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(105)
        self.set_color_as_parent()
        self.yoko3=AnimationZone3(self)
        self.input3 = MyInputBox3(self,50)
        self.text3c = CustomText2c(self,'　　　　　　　　　　　　　　　　※半角英数字で７～２０文字',15)
        self.set_margin(30,5)
        self.set_background_color("#F6F6F6")
        self.parent.add_element(self)




#ログインボタン
class MyButton2(MesaButtonText):
    def __init__(
        self, parent, text, textcolor, bgcolor
    ) -> None:
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
    def show_press(self):...

app = MyApplication()
app.run()
