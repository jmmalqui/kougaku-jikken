from mesa import *
import pygame as pg


class Title(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-SemiBold.ttf")
        self.set_font_size(28)
        self.set_text_color("black")
        self.set_text(text)
        self.set_background_color("white")
        # self.border("black", 2)
        self.center_text()
        self.parent.add_element(self)

class modoru(MesaButtonText):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(60)
        self.set_fixed_height(82)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Bold.ttf")
        self.set_font_size(25)
        self.set_text_color("black")
        self.set_text("＜")
        self.set_background_color("white")
        self.center_text()
        self.center_vertical()
        self.set_margin(5,10)
        self.parent.add_element(self)


class PCname1(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(19)
        self.set_text_color("black")
        self.set_background_color("#F3F3F3")
        self.set_text("Lenovo")
        self.parent.add_element(self)


class PCname2(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(45)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(22)
        self.set_text_color("black")
        self.set_background_color("#F3F3F3")
        self.set_text("IdeaPad Slim 370i 82RK00BCJP")
        self.parent.add_element(self)


class PCtitle(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(500)
        self.set_fixed_height(100)
        self.set_color_as_parent()
        self.set_background_color("#F3F3F3")
        self.pcname1 = PCname1(self)
        self.pcname2 = PCname2(self)
        self.parent.add_element(self)

        self.set_margin(25,10)


class pcImage(MesaImage):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_height(200)
        self.set_fixed_width(275)
        self.pathimage = image
        self.set_image(image)
        self.set_color_as_parent()
        self.set_margin(25,0)
        self.parent.add_element(self)

    def late_init(self):
        self.resize_match_parent_width()

        return super().late_init()


class imagebox(MesaStackVertical):
    def __init__(self, parent, image) -> None:
        super().__init__(parent)
        self.set_fixed_width(350)
        self.set_fixed_height(210)
        self.set_background_color("#F3F3F3")
        self.image = pcImage(self, image)
        self.set_margin(40, 0)
        self.parent.add_element(self)


class rentarutext(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_fixed_width(180)
        self.set_fixed_height(57)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Medium.ttf")
        self.set_font_size(18)
        self.set_text_color("black")
        self.set_text(text)

        self.border("#424242", 2)
        self.set_background_color("white")
        self.center_text()
        self.set_margin(25,7)

    
        self.parent.add_element(self)



class daisu(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(250)
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(16)
        self.set_text_color("black")
        self.set_text("残り　　台")
        self.set_background_color("#F3F3F3")

        self.set_margin(60,5)

        self.center_text()
        self.parent.add_element(self)

#残り台数を更新する
class number(MesaTextLabel):
    def __init__(self, parent, number) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_parent()
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(27)
        self.set_text_color("black")
        self.set_text(number)
        self.set_background_color("#00000000")
        self.set_margin(0, 3)
        self.center_text()
        self.parent.add_element(self)


class NormalText(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(20)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(12)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        self.set_margin(2, 0)
        #self.center_text()
        #self.center_vertical()
        self.parent.add_element(self)

class subTitle(MesaTextLabel):
    def __init__(self, parent, text) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(30)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(19)
        self.set_text_color("black")
        self.set_text(text)
        self.set_color_as_parent()
        #self.border("black", 2)
        #self.center_text()
        self.parent.add_element(self)

class setumei(MesaStackVertical):
    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(300)
        self.set_background_color("#F3F3F3")
        self.text1=NormalText(self,"本体サイズ 　　:  359.2mm×236.5mm×19.9mm")
        self.text2=NormalText(self,"スクリーン 　　:  15.6インチ")
        self.text3=NormalText(self,"解像度 　　　　:  1920×1080")
        self.text4=NormalText(self,"メモリ　　 　　:  8GB DDDR4-3200MHz")
        self.text5=NormalText(self,"ストレージ 　　:  512GB SSD")
        self.text6=NormalText(self,"ソフトウェア 　:  Windows11 Home 64bit")
        self.text7=NormalText(self,"プロセッサ　 　:  インテルCore i5-1235U プロセッサー")
        self.text8=NormalText(self,"バッテリー　 　:  3セル リチウムイオンポリマーバッテリー45Wh")
        self.set_margin(0,6)
        self.parent.add_element(self)

class setumeibox(MesaStackVertical):
    def __init__(self,parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(240)
        self.set_background_color("#F3F3F3")
        self.title=subTitle(self,"詳細")
        self.setumeitext=setumei(self)
        self.set_margin(24,15)
        self.parent.add_element(self)

class CustomBox1(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(280)
        self.set_fixed_height(2)
        self.set_background_color("#F3F3F3")
        self.border_up("black",1)
        self.set_margin(24,0)
        self.parent.add_element(self)

class CustomBox2(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_fixed_width(220)
        self.set_fixed_height(2)
        self.set_background_color("#F3F3F3")
        self.border_up("black",1)
        self.set_margin(24,0)
        self.parent.add_element(self)


class textbox1(MesaStackHorizontal):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_display()
        self.set_fixed_height(80)
        self.set_background_color("#F3F3F3")
        self.rentaru = rentarutext(self, "レンタル可能")
        self.daisu = daisu(self)
        self.number = number(self.daisu, "  2")
        self.parent.add_element(self)


class calendarTitle(MesaTextLabel):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_fixed_height(60)
        self.declare_font_type("NOSYS")
        self.load_ttf("res/NotoSansJP-Regular.ttf")
        self.set_font_size(22)
        self.set_text_color("black")
        self.set_text("レンタル期間選択")
        #self.border("black", 2)
        self.set_color_as_parent()
        self.set_margin(0,10)
        self.center_text()
        self.parent.add_element(self)


class scroll(MesaStackVertical):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.set_width_as_parent()
        self.set_height_as_parent()
        self.set_background_color("#F3F3F3")
        self.enable_scrolling()

        self.PCname=PCtitle(self)
        self.image=imagebox(self,"res/pc2.png")
        self.text1=textbox1(self)
        self.sen1=CustomBox1(self)
        self.text2=setumeibox(self)
        self.sen=CustomBox2(self)
        self.text3=calendarTitle(self)

        self.parent.add_element(self)


class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("white")
        self.container = MesaStackVertical(self)
        self.title = Title(self.container, "Renteck")
        self.button = modoru(self.title)
        self.scroll = scroll(self.container)
        self.set_background_color("#E6E6E6")
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
