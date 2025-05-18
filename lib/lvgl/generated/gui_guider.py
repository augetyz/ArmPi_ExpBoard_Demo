# Copyright 2022 NXP
# SPDX-License-Identifier: MIT
# The auto-generated can only be used on NXP devices

import SDL
import utime as time
import usys as sys
import lvgl as lv
import lodepng as png
import ustruct

lv.init()
SDL.init(w=172,h=320)

# Register SDL display driver.
disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytearray(172*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 172
disp_drv.ver_res = 320
disp_drv.register()

# Regsiter SDL mouse driver
indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER
indev_drv.read_cb = SDL.mouse_read
indev_drv.register()

# Below: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

COLOR_SIZE = lv.color_t.__SIZE__
COLOR_IS_SWAPPED = hasattr(lv.color_t().ch,'green_h')

class lodepng_error(RuntimeError):
    def __init__(self, err):
        if type(err) is int:
            super().__init__(png.error_text(err))
        else:
            super().__init__(err)

# Parse PNG file header
# Taken from https://github.com/shibukawa/imagesize_py/blob/ffef30c1a4715c5acf90e8945ceb77f4a2ed2d45/imagesize.py#L63-L85

def get_png_info(decoder, src, header):
    # Only handle variable image types

    if lv.img.src_get_type(src) != lv.img.SRC.VARIABLE:
        return lv.RES.INV

    data = lv.img_dsc_t.__cast__(src).data
    if data == None:
        return lv.RES.INV

    png_header = bytes(data.__dereference__(24))

    if png_header.startswith(b'\211PNG\r\n\032\n'):
        if png_header[12:16] == b'IHDR':
            start = 16
        # Maybe this is for an older PNG version.
        else:
            start = 8
        try:
            width, height = ustruct.unpack(">LL", png_header[start:start+8])
        except ustruct.error:
            return lv.RES.INV
    else:
        return lv.RES.INV

    header.always_zero = 0
    header.w = width
    header.h = height
    header.cf = lv.img.CF.TRUE_COLOR_ALPHA

    return lv.RES.OK

def convert_rgba8888_to_bgra8888(img_view):
    for i in range(0, len(img_view), lv.color_t.__SIZE__):
        ch = lv.color_t.__cast__(img_view[i:i]).ch
        ch.red, ch.blue = ch.blue, ch.red

# Read and parse PNG file

def open_png(decoder, dsc):
    img_dsc = lv.img_dsc_t.__cast__(dsc.src)
    png_data = img_dsc.data
    png_size = img_dsc.data_size
    png_decoded = png.C_Pointer()
    png_width = png.C_Pointer()
    png_height = png.C_Pointer()
    error = png.decode32(png_decoded, png_width, png_height, png_data, png_size)
    if error:
        raise lodepng_error(error)
    img_size = png_width.int_val * png_height.int_val * 4
    img_data = png_decoded.ptr_val
    img_view = img_data.__dereference__(img_size)

    if COLOR_SIZE == 4:
        convert_rgba8888_to_bgra8888(img_view)
    else:
        raise lodepng_error("Error: Color mode not supported yet!")

    dsc.img_data = img_data
    return lv.RES.OK

# Above: Taken from https://github.com/lvgl/lv_binding_micropython/blob/master/driver/js/imagetools.py#L22-L94

decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

def anim_x_cb(obj, v):
    obj.set_x(v)

def anim_y_cb(obj, v):
    obj.set_y(v)

def ta_event_cb(e,kb):
    code = e.get_code()
    ta = e.get_target()
    if code == lv.EVENT.FOCUSED:
        kb.set_textarea(ta)
        kb.move_foreground()
        kb.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        kb.set_textarea(None)
        kb.move_background()
        kb.add_flag(lv.obj.FLAG.HIDDEN)



# create screen
screen = lv.obj()
screen.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_main_main_default
style_screen_main_main_default = lv.style_t()
style_screen_main_main_default.init()
style_screen_main_main_default.set_bg_color(lv.color_make(0xe0,0xe8,0xee))
style_screen_main_main_default.set_bg_opa(249)

# add style for screen
screen.add_style(style_screen_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_arc_1
screen_arc_1 = lv.arc(screen)
screen_arc_1.set_pos(int(3),int(50))
screen_arc_1.set_size(100,100)
screen_arc_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_arc_1.set_mode(lv.arc.MODE.NORMAL)
screen_arc_1.set_range(0, 100)
screen_arc_1.set_bg_angles(0, 360)
screen_arc_1.set_angles(0, 0)
screen_arc_1.set_rotation(90)
# create style style_screen_arc_1_main_main_default
style_screen_arc_1_main_main_default = lv.style_t()
style_screen_arc_1_main_main_default.init()
style_screen_arc_1_main_main_default.set_radius(6)
style_screen_arc_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_arc_1_main_main_default.set_bg_grad_color(lv.color_make(0xf6,0xf6,0xf6))
style_screen_arc_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_arc_1_main_main_default.set_bg_opa(255)
style_screen_arc_1_main_main_default.set_border_width(0)
style_screen_arc_1_main_main_default.set_pad_left(5)
style_screen_arc_1_main_main_default.set_pad_right(5)
style_screen_arc_1_main_main_default.set_pad_top(5)
style_screen_arc_1_main_main_default.set_pad_bottom(5)
style_screen_arc_1_main_main_default.set_arc_color(lv.color_make(0xE6,0xE6,0xE6))
style_screen_arc_1_main_main_default.set_arc_width(11)

# add style for screen_arc_1
screen_arc_1.add_style(style_screen_arc_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_arc_1_main_indicator_default
style_screen_arc_1_main_indicator_default = lv.style_t()
style_screen_arc_1_main_indicator_default.init()
style_screen_arc_1_main_indicator_default.set_arc_color(lv.color_make(0x26,0xB0,0x8C))
style_screen_arc_1_main_indicator_default.set_arc_width(11)

# add style for screen_arc_1
screen_arc_1.add_style(style_screen_arc_1_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

# create style style_screen_arc_1_main_knob_default
style_screen_arc_1_main_knob_default = lv.style_t()
style_screen_arc_1_main_knob_default.init()
style_screen_arc_1_main_knob_default.set_bg_color(lv.color_make(0x26,0xB0,0x8C))
style_screen_arc_1_main_knob_default.set_bg_grad_color(lv.color_make(0xff,0x00,0x27))
style_screen_arc_1_main_knob_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_arc_1_main_knob_default.set_bg_opa(255)
style_screen_arc_1_main_knob_default.set_pad_all(0)

# add style for screen_arc_1
screen_arc_1.add_style(style_screen_arc_1_main_knob_default, lv.PART.KNOB|lv.STATE.DEFAULT)


# create screen_arc_2
screen_arc_2 = lv.arc(screen)
screen_arc_2.set_pos(int(3),int(153))
screen_arc_2.set_size(100,100)
screen_arc_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_arc_2.set_mode(lv.arc.MODE.NORMAL)
screen_arc_2.set_range(0, 100)
screen_arc_2.set_bg_angles(0, 360)
screen_arc_2.set_angles(0, 0)
screen_arc_2.set_rotation(90)
# create style style_screen_arc_2_main_main_default
style_screen_arc_2_main_main_default = lv.style_t()
style_screen_arc_2_main_main_default.init()
style_screen_arc_2_main_main_default.set_radius(6)
style_screen_arc_2_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_arc_2_main_main_default.set_bg_grad_color(lv.color_make(0xFA,0xAB,0xAB))
style_screen_arc_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_arc_2_main_main_default.set_bg_opa(255)
style_screen_arc_2_main_main_default.set_border_width(0)
style_screen_arc_2_main_main_default.set_pad_left(5)
style_screen_arc_2_main_main_default.set_pad_right(5)
style_screen_arc_2_main_main_default.set_pad_top(5)
style_screen_arc_2_main_main_default.set_pad_bottom(5)
style_screen_arc_2_main_main_default.set_arc_color(lv.color_make(0xe6,0xe6,0xe6))
style_screen_arc_2_main_main_default.set_arc_width(11)

# add style for screen_arc_2
screen_arc_2.add_style(style_screen_arc_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_arc_2_main_indicator_default
style_screen_arc_2_main_indicator_default = lv.style_t()
style_screen_arc_2_main_indicator_default.init()
style_screen_arc_2_main_indicator_default.set_arc_color(lv.color_make(0x21,0x95,0xf6))
style_screen_arc_2_main_indicator_default.set_arc_width(11)

# add style for screen_arc_2
screen_arc_2.add_style(style_screen_arc_2_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)

# create style style_screen_arc_2_main_knob_default
style_screen_arc_2_main_knob_default = lv.style_t()
style_screen_arc_2_main_knob_default.init()
style_screen_arc_2_main_knob_default.set_bg_color(lv.color_make(0x21,0x95,0xf6))
style_screen_arc_2_main_knob_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_arc_2_main_knob_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_arc_2_main_knob_default.set_bg_opa(255)
style_screen_arc_2_main_knob_default.set_pad_all(0)

# add style for screen_arc_2
screen_arc_2.add_style(style_screen_arc_2_main_knob_default, lv.PART.KNOB|lv.STATE.DEFAULT)


# create screen_cont_1
screen_cont_1 = lv.obj(screen)
screen_cont_1.set_pos(int(1),int(2))
screen_cont_1.set_size(170,45)
screen_cont_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create screen_datetext_1
screen_datetext_1 = lv.label(screen_cont_1)
screen_datetext_1.set_text("2022/07/28")
screen_datetext_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, 0)

try:
    screen_datetext_1_calendar
except NameError:
    screen_datetext_1_calendar = lv.calendar(lv.layer_top())
    screen_datetext_1_calendar.set_size(240, 240)
    screen_datetext_1_calendar.set_pos(1,0)
    screen_datetext_1_calendar.set_showed_date(2022, 5)
    screen_datetext_1_calendar.align(lv.ALIGN.CENTER, 20, 20)
    lv.calendar_header_arrow(screen_datetext_1_calendar)

screen_datetext_1_calendar.add_flag(lv.obj.FLAG.HIDDEN)

def screen_datetext_1_calendar_event_handler(e, textV):
    code = e.get_code()
    obj = e.get_current_target()
    if code == lv.EVENT.VALUE_CHANGED:
        date = lv.calendar_date_t()
        obj.get_pressed_date(date) == lv.RES.OK
        textV.set_text("%02d/%02d/%02d"%(date.year, date.month, date.day))

def screen_datetext_1_event(e, date_ca):
    code = e.get_code()
    if code == lv.EVENT.FOCUSED:
        date_ca.add_event_cb(lambda e: screen_datetext_1_calendar_event_handler(e, screen_datetext_1), lv.EVENT.ALL, None)
        date_ca.move_foreground()
        date_ca.clear_flag(lv.obj.FLAG.HIDDEN)

    if code == lv.EVENT.DEFOCUSED:
        date_ca.move_background()
        date_ca.add_flag(lv.obj.FLAG.HIDDEN)

screen_datetext_1.add_flag(lv.obj.FLAG.CLICKABLE)
screen_datetext_1.add_event_cb(lambda e: screen_datetext_1_event(e, screen_datetext_1_calendar), lv.EVENT.ALL, None)
screen_datetext_1.set_pos(int(0),int(0))
screen_datetext_1.set_size(67,40)
screen_datetext_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_datetext_1_main_main_default
style_screen_datetext_1_main_main_default = lv.style_t()
style_screen_datetext_1_main_main_default.init()
style_screen_datetext_1_main_main_default.set_radius(0)
style_screen_datetext_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_datetext_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_datetext_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_datetext_1_main_main_default.set_bg_opa(119)
style_screen_datetext_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_datetext_1_main_main_default.set_text_font(lv.font_consola_12)
except AttributeError:
    try:
        style_screen_datetext_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_screen_datetext_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_datetext_1_main_main_default.set_text_letter_space(0)
style_screen_datetext_1_main_main_default.set_pad_left(0)
style_screen_datetext_1_main_main_default.set_pad_right(0)
style_screen_datetext_1_main_main_default.set_pad_top(12)

# add style for screen_datetext_1
screen_datetext_1.add_style(style_screen_datetext_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_digital_clock_1

screen_digital_clock_1 = lv.dclock(screen_cont_1, "11:25:50")
screen_digital_clock_1.set_text("11:25:50")



class screen_digital_clock_1_timerClass():
    def __init__(self):
        self.hour = 11
        self.minute = 25
        self.second = 50
  
    def count_24(self, timer):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
	
        if self.minute == 60:
            self.minute = 0
            self.hour +=1
            
        if self.hour == 24:
            self.hour = 0

        screen_digital_clock_1.set_text("%02d:%02d:%02d" %(self.hour, self.minute, self.second))

    def count_12(self, timer):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            if self.hour < 12:
                self.hour += 1
            else:
                self.hour += 1
                self.hour = self.hour % 12
        if (self.hour == 12 and self.second == 0 and self.minute == 0):
            if(self.meridiem == "PM"):
                self.meridiem = "AM"
            else:
                self.meridiem = "PM"
		
        screen_digital_clock_1.set_text("%02d:%02d:%02d %s" %(self.hour, self.minute, self.second, self.meridiem))

screen_digital_clock_1_timerInstance = screen_digital_clock_1_timerClass()

screen_digital_clock_1_timer = lv.timer_create_basic()
screen_digital_clock_1_timer.set_period(1000)

screen_digital_clock_1_timer.set_cb(lambda src: screen_digital_clock_1_timerInstance.count_24(screen_digital_clock_1_timer))
lv.dclock.set_style_text_align(screen_digital_clock_1, lv.TEXT_ALIGN.CENTER, 0);

screen_digital_clock_1.set_pos(int(107),int(0))
screen_digital_clock_1.set_size(59,40)
screen_digital_clock_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# create style style_screen_digital_clock_1_main_main_default
style_screen_digital_clock_1_main_main_default = lv.style_t()
style_screen_digital_clock_1_main_main_default.init()
style_screen_digital_clock_1_main_main_default.set_radius(0)
style_screen_digital_clock_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_digital_clock_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_digital_clock_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_digital_clock_1_main_main_default.set_bg_opa(255)
style_screen_digital_clock_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_digital_clock_1_main_main_default.set_text_font(lv.font_consola_12)
except AttributeError:
    try:
        style_screen_digital_clock_1_main_main_default.set_text_font(lv.font_montserrat_12)
    except AttributeError:
        style_screen_digital_clock_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_digital_clock_1_main_main_default.set_text_letter_space(0)
style_screen_digital_clock_1_main_main_default.set_pad_left(0)
style_screen_digital_clock_1_main_main_default.set_pad_right(0)
style_screen_digital_clock_1_main_main_default.set_pad_top(12)
style_screen_digital_clock_1_main_main_default.set_pad_bottom(0)

# add style for screen_digital_clock_1
screen_digital_clock_1.add_style(style_screen_digital_clock_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_Wifi_disconnected
screen_Wifi_disconnected = lv.img(screen_cont_1)
screen_Wifi_disconnected.set_pos(int(81),int(10))
screen_Wifi_disconnected.set_size(15,15)
screen_Wifi_disconnected.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_Wifi_disconnected.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-335811916.png','rb') as f:
        screen_Wifi_disconnected_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-335811916.png')
    sys.exit()

screen_Wifi_disconnected_img = lv.img_dsc_t({
  'data_size': len(screen_Wifi_disconnected_img_data),
  'header': {'always_zero': 0, 'w': 15, 'h': 15, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_Wifi_disconnected_img_data
})

screen_Wifi_disconnected.set_src(screen_Wifi_disconnected_img)
screen_Wifi_disconnected.set_pivot(50,50)
screen_Wifi_disconnected.set_angle(0)
# create style style_screen_wifi_disconnected_main_main_default
style_screen_wifi_disconnected_main_main_default = lv.style_t()
style_screen_wifi_disconnected_main_main_default.init()
style_screen_wifi_disconnected_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_wifi_disconnected_main_main_default.set_img_recolor_opa(0)
style_screen_wifi_disconnected_main_main_default.set_img_opa(255)

# add style for screen_Wifi_disconnected
screen_Wifi_disconnected.add_style(style_screen_wifi_disconnected_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_WIfi_connected
screen_WIfi_connected = lv.img(screen_cont_1)
screen_WIfi_connected.set_pos(int(81),int(10))
screen_WIfi_connected.set_size(15,15)
screen_WIfi_connected.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_WIfi_connected.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1339354119.png','rb') as f:
        screen_WIfi_connected_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1339354119.png')
    sys.exit()

screen_WIfi_connected_img = lv.img_dsc_t({
  'data_size': len(screen_WIfi_connected_img_data),
  'header': {'always_zero': 0, 'w': 15, 'h': 15, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_WIfi_connected_img_data
})

screen_WIfi_connected.set_src(screen_WIfi_connected_img)
screen_WIfi_connected.set_pivot(50,50)
screen_WIfi_connected.set_angle(0)
# create style style_screen_wifi_connected_main_main_default
style_screen_wifi_connected_main_main_default = lv.style_t()
style_screen_wifi_connected_main_main_default.init()
style_screen_wifi_connected_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_wifi_connected_main_main_default.set_img_recolor_opa(0)
style_screen_wifi_connected_main_main_default.set_img_opa(255)

# add style for screen_WIfi_connected
screen_WIfi_connected.add_style(style_screen_wifi_connected_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_cont_1_main_main_default
style_screen_cont_1_main_main_default = lv.style_t()
style_screen_cont_1_main_main_default.init()
style_screen_cont_1_main_main_default.set_radius(8)
style_screen_cont_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_1_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_cont_1_main_main_default.set_bg_opa(255)
style_screen_cont_1_main_main_default.set_border_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_1_main_main_default.set_border_width(2)
style_screen_cont_1_main_main_default.set_border_opa(255)
style_screen_cont_1_main_main_default.set_pad_left(0)
style_screen_cont_1_main_main_default.set_pad_right(0)
style_screen_cont_1_main_main_default.set_pad_top(0)
style_screen_cont_1_main_main_default.set_pad_bottom(0)

# add style for screen_cont_1
screen_cont_1.add_style(style_screen_cont_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_label_1
screen_label_1 = lv.label(screen)
screen_label_1.set_pos(int(30),int(85))
screen_label_1.set_size(46,31)
screen_label_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_1.set_text("99.1%\nCPU")
screen_label_1.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_1_main_main_default
style_screen_label_1_main_main_default = lv.style_t()
style_screen_label_1_main_main_default.init()
style_screen_label_1_main_main_default.set_radius(0)
style_screen_label_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_1_main_main_default.set_bg_opa(0)
style_screen_label_1_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_label_1_main_main_default.set_text_font(lv.font_consola_10)
except AttributeError:
    try:
        style_screen_label_1_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_label_1_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_1_main_main_default.set_text_letter_space(0)
style_screen_label_1_main_main_default.set_text_line_space(0)
style_screen_label_1_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_1_main_main_default.set_pad_left(0)
style_screen_label_1_main_main_default.set_pad_right(0)
style_screen_label_1_main_main_default.set_pad_top(4)
style_screen_label_1_main_main_default.set_pad_bottom(0)

# add style for screen_label_1
screen_label_1.add_style(style_screen_label_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_label_2
screen_label_2 = lv.label(screen)
screen_label_2.set_pos(int(30),int(189))
screen_label_2.set_size(46,29)
screen_label_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_2.set_text("15.8%\nRAM")
screen_label_2.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_2_main_main_default
style_screen_label_2_main_main_default = lv.style_t()
style_screen_label_2_main_main_default.init()
style_screen_label_2_main_main_default.set_radius(0)
style_screen_label_2_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_2_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_2_main_main_default.set_bg_opa(0)
style_screen_label_2_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_label_2_main_main_default.set_text_font(lv.font_consola_10)
except AttributeError:
    try:
        style_screen_label_2_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_label_2_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_2_main_main_default.set_text_letter_space(0)
style_screen_label_2_main_main_default.set_text_line_space(0)
style_screen_label_2_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_2_main_main_default.set_pad_left(0)
style_screen_label_2_main_main_default.set_pad_right(0)
style_screen_label_2_main_main_default.set_pad_top(4)
style_screen_label_2_main_main_default.set_pad_bottom(0)

# add style for screen_label_2
screen_label_2.add_style(style_screen_label_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_cont_2
screen_cont_2 = lv.obj(screen)
screen_cont_2.set_pos(int(105),int(50))
screen_cont_2.set_size(66,120)
screen_cont_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create screen_img_1
screen_img_1 = lv.img(screen_cont_2)
screen_img_1.set_pos(int(21),int(11))
screen_img_1.set_size(20,20)
screen_img_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_img_1.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1106025274.png','rb') as f:
        screen_img_1_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1106025274.png')
    sys.exit()

screen_img_1_img = lv.img_dsc_t({
  'data_size': len(screen_img_1_img_data),
  'header': {'always_zero': 0, 'w': 20, 'h': 20, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_img_1_img_data
})

screen_img_1.set_src(screen_img_1_img)
screen_img_1.set_pivot(50,50)
screen_img_1.set_angle(0)
# create style style_screen_img_1_main_main_default
style_screen_img_1_main_main_default = lv.style_t()
style_screen_img_1_main_main_default.init()
style_screen_img_1_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_img_1_main_main_default.set_img_recolor_opa(0)
style_screen_img_1_main_main_default.set_img_opa(255)

# add style for screen_img_1
screen_img_1.add_style(style_screen_img_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_img_4
screen_img_4 = lv.img(screen_cont_2)
screen_img_4.set_pos(int(0),int(94))
screen_img_4.set_size(15,15)
screen_img_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_img_4.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1565058120.png','rb') as f:
        screen_img_4_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1565058120.png')
    sys.exit()

screen_img_4_img = lv.img_dsc_t({
  'data_size': len(screen_img_4_img_data),
  'header': {'always_zero': 0, 'w': 15, 'h': 15, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_img_4_img_data
})

screen_img_4.set_src(screen_img_4_img)
screen_img_4.set_pivot(50,50)
screen_img_4.set_angle(0)
# create style style_screen_img_4_main_main_default
style_screen_img_4_main_main_default = lv.style_t()
style_screen_img_4_main_main_default.init()
style_screen_img_4_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_img_4_main_main_default.set_img_recolor_opa(0)
style_screen_img_4_main_main_default.set_img_opa(255)

# add style for screen_img_4
screen_img_4.add_style(style_screen_img_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_cont_2_main_main_default
style_screen_cont_2_main_main_default = lv.style_t()
style_screen_cont_2_main_main_default.init()
style_screen_cont_2_main_main_default.set_radius(5)
style_screen_cont_2_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_2_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_2_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_cont_2_main_main_default.set_bg_opa(255)
style_screen_cont_2_main_main_default.set_border_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_2_main_main_default.set_border_width(2)
style_screen_cont_2_main_main_default.set_border_opa(255)
style_screen_cont_2_main_main_default.set_pad_left(0)
style_screen_cont_2_main_main_default.set_pad_right(0)
style_screen_cont_2_main_main_default.set_pad_top(0)
style_screen_cont_2_main_main_default.set_pad_bottom(0)

# add style for screen_cont_2
screen_cont_2.add_style(style_screen_cont_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_img_2
screen_img_2 = lv.img(screen)
screen_img_2.set_pos(int(110),int(95))
screen_img_2.set_size(10,10)
screen_img_2.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_img_2.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp666395419.png','rb') as f:
        screen_img_2_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp666395419.png')
    sys.exit()

screen_img_2_img = lv.img_dsc_t({
  'data_size': len(screen_img_2_img_data),
  'header': {'always_zero': 0, 'w': 10, 'h': 10, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_img_2_img_data
})

screen_img_2.set_src(screen_img_2_img)
screen_img_2.set_pivot(50,50)
screen_img_2.set_angle(0)
# create style style_screen_img_2_main_main_default
style_screen_img_2_main_main_default = lv.style_t()
style_screen_img_2_main_main_default.init()
style_screen_img_2_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_img_2_main_main_default.set_img_recolor_opa(0)
style_screen_img_2_main_main_default.set_img_opa(255)

# add style for screen_img_2
screen_img_2.add_style(style_screen_img_2_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_img_3
screen_img_3 = lv.img(screen)
screen_img_3.set_pos(int(110),int(120))
screen_img_3.set_size(10,10)
screen_img_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_img_3.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1521341534.png','rb') as f:
        screen_img_3_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1521341534.png')
    sys.exit()

screen_img_3_img = lv.img_dsc_t({
  'data_size': len(screen_img_3_img_data),
  'header': {'always_zero': 0, 'w': 10, 'h': 10, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_img_3_img_data
})

screen_img_3.set_src(screen_img_3_img)
screen_img_3.set_pivot(50,50)
screen_img_3.set_angle(0)
# create style style_screen_img_3_main_main_default
style_screen_img_3_main_main_default = lv.style_t()
style_screen_img_3_main_main_default.init()
style_screen_img_3_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_img_3_main_main_default.set_img_recolor_opa(0)
style_screen_img_3_main_main_default.set_img_opa(255)

# add style for screen_img_3
screen_img_3.add_style(style_screen_img_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_label_3
screen_label_3 = lv.label(screen)
screen_label_3.set_pos(int(120),int(87))
screen_label_3.set_size(52,26)
screen_label_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_3.set_text("1.0 KB/s")
screen_label_3.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_3_main_main_default
style_screen_label_3_main_main_default = lv.style_t()
style_screen_label_3_main_main_default.init()
style_screen_label_3_main_main_default.set_radius(0)
style_screen_label_3_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_3_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_3_main_main_default.set_bg_opa(255)
style_screen_label_3_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_label_3_main_main_default.set_text_font(lv.font_consola_10)
except AttributeError:
    try:
        style_screen_label_3_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_label_3_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_3_main_main_default.set_text_letter_space(0)
style_screen_label_3_main_main_default.set_text_line_space(0)
style_screen_label_3_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_3_main_main_default.set_pad_left(0)
style_screen_label_3_main_main_default.set_pad_right(0)
style_screen_label_3_main_main_default.set_pad_top(7)
style_screen_label_3_main_main_default.set_pad_bottom(0)

# add style for screen_label_3
screen_label_3.add_style(style_screen_label_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_animimg_1
screen_animimg_1 = lv.animimg(screen)
screen_animimg_1.set_pos(int(107),int(172))
screen_animimg_1.set_size(61,81)
screen_animimg_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_animimg_1_animimgs = [None]*100
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp998528621.png','rb') as f:
        screen_animimg_1_animimg_data_0 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp998528621.png')
    sys.exit()

screen_animimg_1_animimgs[0] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_0),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_0
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp705125614.png','rb') as f:
        screen_animimg_1_animimg_data_1 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp705125614.png')
    sys.exit()

screen_animimg_1_animimgs[1] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_1),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_1
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp411722607.png','rb') as f:
        screen_animimg_1_animimg_data_2 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp411722607.png')
    sys.exit()

screen_animimg_1_animimgs[2] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_2),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_2
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp118319600.png','rb') as f:
        screen_animimg_1_animimg_data_3 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp118319600.png')
    sys.exit()

screen_animimg_1_animimgs[3] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_3),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_3
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-175083407.png','rb') as f:
        screen_animimg_1_animimg_data_4 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-175083407.png')
    sys.exit()

screen_animimg_1_animimgs[4] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_4),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_4
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-468486414.png','rb') as f:
        screen_animimg_1_animimg_data_5 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-468486414.png')
    sys.exit()

screen_animimg_1_animimgs[5] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_5),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_5
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-761889421.png','rb') as f:
        screen_animimg_1_animimg_data_6 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-761889421.png')
    sys.exit()

screen_animimg_1_animimgs[6] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_6),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_6
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1055292428.png','rb') as f:
        screen_animimg_1_animimg_data_7 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1055292428.png')
    sys.exit()

screen_animimg_1_animimgs[7] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_7),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_7
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1348695435.png','rb') as f:
        screen_animimg_1_animimg_data_8 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1348695435.png')
    sys.exit()

screen_animimg_1_animimgs[8] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_8),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_8
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1642098442.png','rb') as f:
        screen_animimg_1_animimg_data_9 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1642098442.png')
    sys.exit()

screen_animimg_1_animimgs[9] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_9),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_9
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp492969996.png','rb') as f:
        screen_animimg_1_animimg_data_10 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp492969996.png')
    sys.exit()

screen_animimg_1_animimgs[10] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_10),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_10
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp199566989.png','rb') as f:
        screen_animimg_1_animimg_data_11 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp199566989.png')
    sys.exit()

screen_animimg_1_animimgs[11] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_11),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_11
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-93836018.png','rb') as f:
        screen_animimg_1_animimg_data_12 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-93836018.png')
    sys.exit()

screen_animimg_1_animimgs[12] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_12),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_12
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-387239025.png','rb') as f:
        screen_animimg_1_animimg_data_13 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-387239025.png')
    sys.exit()

screen_animimg_1_animimgs[13] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_13),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_13
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-680642032.png','rb') as f:
        screen_animimg_1_animimg_data_14 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-680642032.png')
    sys.exit()

screen_animimg_1_animimgs[14] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_14),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_14
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-974045039.png','rb') as f:
        screen_animimg_1_animimg_data_15 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-974045039.png')
    sys.exit()

screen_animimg_1_animimgs[15] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_15),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_15
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1267448046.png','rb') as f:
        screen_animimg_1_animimg_data_16 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1267448046.png')
    sys.exit()

screen_animimg_1_animimgs[16] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_16),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_16
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1560851053.png','rb') as f:
        screen_animimg_1_animimg_data_17 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1560851053.png')
    sys.exit()

screen_animimg_1_animimgs[17] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_17),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_17
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1854254060.png','rb') as f:
        screen_animimg_1_animimg_data_18 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1854254060.png')
    sys.exit()

screen_animimg_1_animimgs[18] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_18),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_18
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp2147310229.png','rb') as f:
        screen_animimg_1_animimg_data_19 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp2147310229.png')
    sys.exit()

screen_animimg_1_animimgs[19] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_19),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_19
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-12588629.png','rb') as f:
        screen_animimg_1_animimg_data_20 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-12588629.png')
    sys.exit()

screen_animimg_1_animimgs[20] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_20),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_20
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-305991636.png','rb') as f:
        screen_animimg_1_animimg_data_21 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-305991636.png')
    sys.exit()

screen_animimg_1_animimgs[21] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_21),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_21
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-599394643.png','rb') as f:
        screen_animimg_1_animimg_data_22 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-599394643.png')
    sys.exit()

screen_animimg_1_animimgs[22] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_22),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_22
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-892797650.png','rb') as f:
        screen_animimg_1_animimg_data_23 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-892797650.png')
    sys.exit()

screen_animimg_1_animimgs[23] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_23),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_23
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1186200657.png','rb') as f:
        screen_animimg_1_animimg_data_24 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1186200657.png')
    sys.exit()

screen_animimg_1_animimgs[24] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_24),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_24
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1479603664.png','rb') as f:
        screen_animimg_1_animimg_data_25 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1479603664.png')
    sys.exit()

screen_animimg_1_animimgs[25] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_25),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_25
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1773006671.png','rb') as f:
        screen_animimg_1_animimg_data_26 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1773006671.png')
    sys.exit()

screen_animimg_1_animimgs[26] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_26),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_26
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-2066409678.png','rb') as f:
        screen_animimg_1_animimg_data_27 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-2066409678.png')
    sys.exit()

screen_animimg_1_animimgs[27] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_27),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_27
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1935154611.png','rb') as f:
        screen_animimg_1_animimg_data_28 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1935154611.png')
    sys.exit()

screen_animimg_1_animimgs[28] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_28),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_28
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1641751604.png','rb') as f:
        screen_animimg_1_animimg_data_29 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1641751604.png')
    sys.exit()

screen_animimg_1_animimgs[29] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_29),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_29
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-518147254.png','rb') as f:
        screen_animimg_1_animimg_data_30 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-518147254.png')
    sys.exit()

screen_animimg_1_animimgs[30] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_30),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_30
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-811550261.png','rb') as f:
        screen_animimg_1_animimg_data_31 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-811550261.png')
    sys.exit()

screen_animimg_1_animimgs[31] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_31),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_31
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1104953268.png','rb') as f:
        screen_animimg_1_animimg_data_32 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1104953268.png')
    sys.exit()

screen_animimg_1_animimgs[32] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_32),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_32
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1398356275.png','rb') as f:
        screen_animimg_1_animimg_data_33 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1398356275.png')
    sys.exit()

screen_animimg_1_animimgs[33] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_33),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_33
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1691759282.png','rb') as f:
        screen_animimg_1_animimg_data_34 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1691759282.png')
    sys.exit()

screen_animimg_1_animimgs[34] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_34),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_34
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1985162289.png','rb') as f:
        screen_animimg_1_animimg_data_35 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1985162289.png')
    sys.exit()

screen_animimg_1_animimgs[35] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_35),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_35
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp2016402000.png','rb') as f:
        screen_animimg_1_animimg_data_36 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp2016402000.png')
    sys.exit()

screen_animimg_1_animimgs[36] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_36),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_36
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1722998993.png','rb') as f:
        screen_animimg_1_animimg_data_37 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1722998993.png')
    sys.exit()

screen_animimg_1_animimgs[37] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_37),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_37
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1429595986.png','rb') as f:
        screen_animimg_1_animimg_data_38 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1429595986.png')
    sys.exit()

screen_animimg_1_animimgs[38] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_38),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_38
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1136192979.png','rb') as f:
        screen_animimg_1_animimg_data_39 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1136192979.png')
    sys.exit()

screen_animimg_1_animimgs[39] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_39),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_39
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1023705879.png','rb') as f:
        screen_animimg_1_animimg_data_40 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1023705879.png')
    sys.exit()

screen_animimg_1_animimgs[40] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_40),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_40
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1317108886.png','rb') as f:
        screen_animimg_1_animimg_data_41 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1317108886.png')
    sys.exit()

screen_animimg_1_animimgs[41] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_41),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_41
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1610511893.png','rb') as f:
        screen_animimg_1_animimg_data_42 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1610511893.png')
    sys.exit()

screen_animimg_1_animimgs[42] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_42),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_42
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1903914900.png','rb') as f:
        screen_animimg_1_animimg_data_43 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1903914900.png')
    sys.exit()

screen_animimg_1_animimgs[43] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_43),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_43
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp2097649389.png','rb') as f:
        screen_animimg_1_animimg_data_44 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp2097649389.png')
    sys.exit()

screen_animimg_1_animimgs[44] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_44),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_44
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1804246382.png','rb') as f:
        screen_animimg_1_animimg_data_45 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1804246382.png')
    sys.exit()

screen_animimg_1_animimgs[45] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_45),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_45
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1510843375.png','rb') as f:
        screen_animimg_1_animimg_data_46 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1510843375.png')
    sys.exit()

screen_animimg_1_animimgs[46] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_46),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_46
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1217440368.png','rb') as f:
        screen_animimg_1_animimg_data_47 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1217440368.png')
    sys.exit()

screen_animimg_1_animimgs[47] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_47),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_47
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp924037361.png','rb') as f:
        screen_animimg_1_animimg_data_48 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp924037361.png')
    sys.exit()

screen_animimg_1_animimgs[48] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_48),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_48
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp630634354.png','rb') as f:
        screen_animimg_1_animimg_data_49 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp630634354.png')
    sys.exit()

screen_animimg_1_animimgs[49] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_49),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_49
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1529264504.png','rb') as f:
        screen_animimg_1_animimg_data_50 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1529264504.png')
    sys.exit()

screen_animimg_1_animimgs[50] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_50),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_50
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1822667511.png','rb') as f:
        screen_animimg_1_animimg_data_51 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1822667511.png')
    sys.exit()

screen_animimg_1_animimgs[51] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_51),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_51
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-2116070518.png','rb') as f:
        screen_animimg_1_animimg_data_52 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-2116070518.png')
    sys.exit()

screen_animimg_1_animimgs[52] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_52),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_52
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1885493771.png','rb') as f:
        screen_animimg_1_animimg_data_53 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1885493771.png')
    sys.exit()

screen_animimg_1_animimgs[53] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_53),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_53
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1592090764.png','rb') as f:
        screen_animimg_1_animimg_data_54 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1592090764.png')
    sys.exit()

screen_animimg_1_animimgs[54] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_54),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_54
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1298687757.png','rb') as f:
        screen_animimg_1_animimg_data_55 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1298687757.png')
    sys.exit()

screen_animimg_1_animimgs[55] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_55),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_55
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1005284750.png','rb') as f:
        screen_animimg_1_animimg_data_56 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1005284750.png')
    sys.exit()

screen_animimg_1_animimgs[56] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_56),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_56
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp711881743.png','rb') as f:
        screen_animimg_1_animimg_data_57 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp711881743.png')
    sys.exit()

screen_animimg_1_animimgs[57] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_57),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_57
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp418478736.png','rb') as f:
        screen_animimg_1_animimg_data_58 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp418478736.png')
    sys.exit()

screen_animimg_1_animimgs[58] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_58),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_58
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp125075729.png','rb') as f:
        screen_animimg_1_animimg_data_59 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp125075729.png')
    sys.exit()

screen_animimg_1_animimgs[59] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_59),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_59
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-2034823129.png','rb') as f:
        screen_animimg_1_animimg_data_60 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-2034823129.png')
    sys.exit()

screen_animimg_1_animimgs[60] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_60),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_60
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1966741160.png','rb') as f:
        screen_animimg_1_animimg_data_61 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1966741160.png')
    sys.exit()

screen_animimg_1_animimgs[61] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_61),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_61
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1673338153.png','rb') as f:
        screen_animimg_1_animimg_data_62 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1673338153.png')
    sys.exit()

screen_animimg_1_animimgs[62] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_62),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_62
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1379935146.png','rb') as f:
        screen_animimg_1_animimg_data_63 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1379935146.png')
    sys.exit()

screen_animimg_1_animimgs[63] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_63),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_63
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1086532139.png','rb') as f:
        screen_animimg_1_animimg_data_64 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1086532139.png')
    sys.exit()

screen_animimg_1_animimgs[64] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_64),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_64
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp793129132.png','rb') as f:
        screen_animimg_1_animimg_data_65 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp793129132.png')
    sys.exit()

screen_animimg_1_animimgs[65] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_65),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_65
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp499726125.png','rb') as f:
        screen_animimg_1_animimg_data_66 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp499726125.png')
    sys.exit()

screen_animimg_1_animimgs[66] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_66),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_66
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp206323118.png','rb') as f:
        screen_animimg_1_animimg_data_67 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp206323118.png')
    sys.exit()

screen_animimg_1_animimgs[67] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_67),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_67
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-87079889.png','rb') as f:
        screen_animimg_1_animimg_data_68 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-87079889.png')
    sys.exit()

screen_animimg_1_animimgs[68] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_68),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_68
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-380482896.png','rb') as f:
        screen_animimg_1_animimg_data_69 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-380482896.png')
    sys.exit()

screen_animimg_1_animimgs[69] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_69),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_69
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1754585542.png','rb') as f:
        screen_animimg_1_animimg_data_70 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1754585542.png')
    sys.exit()

screen_animimg_1_animimgs[70] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_70),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_70
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1461182535.png','rb') as f:
        screen_animimg_1_animimg_data_71 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1461182535.png')
    sys.exit()

screen_animimg_1_animimgs[71] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_71),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_71
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1167779528.png','rb') as f:
        screen_animimg_1_animimg_data_72 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1167779528.png')
    sys.exit()

screen_animimg_1_animimgs[72] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_72),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_72
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp874376521.png','rb') as f:
        screen_animimg_1_animimg_data_73 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp874376521.png')
    sys.exit()

screen_animimg_1_animimgs[73] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_73),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_73
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp580973514.png','rb') as f:
        screen_animimg_1_animimg_data_74 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp580973514.png')
    sys.exit()

screen_animimg_1_animimgs[74] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_74),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_74
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp287570507.png','rb') as f:
        screen_animimg_1_animimg_data_75 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp287570507.png')
    sys.exit()

screen_animimg_1_animimgs[75] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_75),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_75
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-5832500.png','rb') as f:
        screen_animimg_1_animimg_data_76 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-5832500.png')
    sys.exit()

screen_animimg_1_animimgs[76] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_76),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_76
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-299235507.png','rb') as f:
        screen_animimg_1_animimg_data_77 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-299235507.png')
    sys.exit()

screen_animimg_1_animimgs[77] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_77),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_77
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-592638514.png','rb') as f:
        screen_animimg_1_animimg_data_78 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-592638514.png')
    sys.exit()

screen_animimg_1_animimgs[78] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_78),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_78
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-886041521.png','rb') as f:
        screen_animimg_1_animimg_data_79 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-886041521.png')
    sys.exit()

screen_animimg_1_animimgs[79] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_79),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_79
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1249026917.png','rb') as f:
        screen_animimg_1_animimg_data_80 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp1249026917.png')
    sys.exit()

screen_animimg_1_animimgs[80] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_80),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_80
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp955623910.png','rb') as f:
        screen_animimg_1_animimg_data_81 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp955623910.png')
    sys.exit()

screen_animimg_1_animimgs[81] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_81),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_81
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp662220903.png','rb') as f:
        screen_animimg_1_animimg_data_82 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp662220903.png')
    sys.exit()

screen_animimg_1_animimgs[82] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_82),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_82
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp368817896.png','rb') as f:
        screen_animimg_1_animimg_data_83 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp368817896.png')
    sys.exit()

screen_animimg_1_animimgs[83] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_83),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_83
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp75414889.png','rb') as f:
        screen_animimg_1_animimg_data_84 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp75414889.png')
    sys.exit()

screen_animimg_1_animimgs[84] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_84),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_84
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-217988118.png','rb') as f:
        screen_animimg_1_animimg_data_85 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-217988118.png')
    sys.exit()

screen_animimg_1_animimgs[85] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_85),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_85
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-511391125.png','rb') as f:
        screen_animimg_1_animimg_data_86 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-511391125.png')
    sys.exit()

screen_animimg_1_animimgs[86] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_86),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_86
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-804794132.png','rb') as f:
        screen_animimg_1_animimg_data_87 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-804794132.png')
    sys.exit()

screen_animimg_1_animimgs[87] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_87),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_87
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1098197139.png','rb') as f:
        screen_animimg_1_animimg_data_88 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1098197139.png')
    sys.exit()

screen_animimg_1_animimgs[88] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_88),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_88
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1391600146.png','rb') as f:
        screen_animimg_1_animimg_data_89 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1391600146.png')
    sys.exit()

screen_animimg_1_animimgs[89] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_89),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_89
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp743468292.png','rb') as f:
        screen_animimg_1_animimg_data_90 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp743468292.png')
    sys.exit()

screen_animimg_1_animimgs[90] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_90),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_90
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp450065285.png','rb') as f:
        screen_animimg_1_animimg_data_91 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp450065285.png')
    sys.exit()

screen_animimg_1_animimgs[91] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_91),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_91
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp156662278.png','rb') as f:
        screen_animimg_1_animimg_data_92 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp156662278.png')
    sys.exit()

screen_animimg_1_animimgs[92] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_92),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_92
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-136740729.png','rb') as f:
        screen_animimg_1_animimg_data_93 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-136740729.png')
    sys.exit()

screen_animimg_1_animimgs[93] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_93),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_93
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-430143736.png','rb') as f:
        screen_animimg_1_animimg_data_94 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-430143736.png')
    sys.exit()

screen_animimg_1_animimgs[94] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_94),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_94
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-723546743.png','rb') as f:
        screen_animimg_1_animimg_data_95 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-723546743.png')
    sys.exit()

screen_animimg_1_animimgs[95] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_95),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_95
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1016949750.png','rb') as f:
        screen_animimg_1_animimg_data_96 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1016949750.png')
    sys.exit()

screen_animimg_1_animimgs[96] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_96),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_96
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1310352757.png','rb') as f:
        screen_animimg_1_animimg_data_97 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1310352757.png')
    sys.exit()

screen_animimg_1_animimgs[97] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_97),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_97
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1603755764.png','rb') as f:
        screen_animimg_1_animimg_data_98 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1603755764.png')
    sys.exit()

screen_animimg_1_animimgs[98] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_98),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_98
})
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1897158771.png','rb') as f:
        screen_animimg_1_animimg_data_99 = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-1897158771.png')
    sys.exit()

screen_animimg_1_animimgs[99] = lv.img_dsc_t({
  'data_size': len(screen_animimg_1_animimg_data_99),
  'header': {'always_zero': 0, 'w': 61, 'h': 81, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_animimg_1_animimg_data_99
})

screen_animimg_1.set_src(screen_animimg_1_animimgs, 100)
screen_animimg_1.set_duration(60 * 100)
screen_animimg_1.set_repeat_count(1410065408)
screen_animimg_1.start()

# create screen_label_4
screen_label_4 = lv.label(screen)
screen_label_4.set_pos(int(120),int(112))
screen_label_4.set_size(52,26)
screen_label_4.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_4.set_text("100.0 MB/s")
screen_label_4.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_4_main_main_default
style_screen_label_4_main_main_default = lv.style_t()
style_screen_label_4_main_main_default.init()
style_screen_label_4_main_main_default.set_radius(0)
style_screen_label_4_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_4_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_4_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_4_main_main_default.set_bg_opa(255)
style_screen_label_4_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_label_4_main_main_default.set_text_font(lv.font_consola_10)
except AttributeError:
    try:
        style_screen_label_4_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_label_4_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_4_main_main_default.set_text_letter_space(0)
style_screen_label_4_main_main_default.set_text_line_space(0)
style_screen_label_4_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_4_main_main_default.set_pad_left(0)
style_screen_label_4_main_main_default.set_pad_right(0)
style_screen_label_4_main_main_default.set_pad_top(8)
style_screen_label_4_main_main_default.set_pad_bottom(0)

# add style for screen_label_4
screen_label_4.add_style(style_screen_label_4_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_label_5
screen_label_5 = lv.label(screen)
screen_label_5.set_pos(int(120),int(140))
screen_label_5.set_size(52,26)
screen_label_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_5.set_text("0.0 ℃")
screen_label_5.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_5_main_main_default
style_screen_label_5_main_main_default = lv.style_t()
style_screen_label_5_main_main_default.init()
style_screen_label_5_main_main_default.set_radius(0)
style_screen_label_5_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_5_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_5_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_5_main_main_default.set_bg_opa(255)
style_screen_label_5_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_label_5_main_main_default.set_text_font(lv.font_consola_10)
except AttributeError:
    try:
        style_screen_label_5_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_label_5_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_5_main_main_default.set_text_letter_space(0)
style_screen_label_5_main_main_default.set_text_line_space(0)
style_screen_label_5_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_5_main_main_default.set_pad_left(0)
style_screen_label_5_main_main_default.set_pad_right(0)
style_screen_label_5_main_main_default.set_pad_top(8)
style_screen_label_5_main_main_default.set_pad_bottom(0)

# add style for screen_label_5
screen_label_5.add_style(style_screen_label_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_cont_3
screen_cont_3 = lv.obj(screen)
screen_cont_3.set_pos(int(3),int(256))
screen_cont_3.set_size(166,62)
screen_cont_3.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

# create screen_img_5
screen_img_5 = lv.img(screen_cont_3)
screen_img_5.set_pos(int(0),int(38))
screen_img_5.set_size(20,20)
screen_img_5.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_img_5.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp210848309.png','rb') as f:
        screen_img_5_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp210848309.png')
    sys.exit()

screen_img_5_img = lv.img_dsc_t({
  'data_size': len(screen_img_5_img_data),
  'header': {'always_zero': 0, 'w': 20, 'h': 20, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_img_5_img_data
})

screen_img_5.set_src(screen_img_5_img)
screen_img_5.set_pivot(50,50)
screen_img_5.set_angle(0)
# create style style_screen_img_5_main_main_default
style_screen_img_5_main_main_default = lv.style_t()
style_screen_img_5_main_main_default.init()
style_screen_img_5_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_img_5_main_main_default.set_img_recolor_opa(0)
style_screen_img_5_main_main_default.set_img_opa(255)

# add style for screen_img_5
screen_img_5.add_style(style_screen_img_5_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_bar_1
screen_bar_1 = lv.bar(screen_cont_3)
screen_bar_1.set_pos(int(23),int(42))
screen_bar_1.set_size(90,12)
screen_bar_1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_bar_1.set_style_anim_time(1000, 0)
screen_bar_1.set_mode(lv.bar.MODE.NORMAL)
screen_bar_1.set_value(50, lv.ANIM.OFF)
# create style style_screen_bar_1_main_main_default
style_screen_bar_1_main_main_default = lv.style_t()
style_screen_bar_1_main_main_default.init()
style_screen_bar_1_main_main_default.set_radius(10)
style_screen_bar_1_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_bar_1_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_bar_1_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_bar_1_main_main_default.set_bg_opa(255)

# add style for screen_bar_1
screen_bar_1.add_style(style_screen_bar_1_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_bar_1_main_indicator_default
style_screen_bar_1_main_indicator_default = lv.style_t()
style_screen_bar_1_main_indicator_default.init()
style_screen_bar_1_main_indicator_default.set_radius(10)
style_screen_bar_1_main_indicator_default.set_bg_color(lv.color_make(0xff,0x9b,0xaa))
style_screen_bar_1_main_indicator_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_bar_1_main_indicator_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_bar_1_main_indicator_default.set_bg_opa(255)

# add style for screen_bar_1
screen_bar_1.add_style(style_screen_bar_1_main_indicator_default, lv.PART.INDICATOR|lv.STATE.DEFAULT)


# create screen_img_6
screen_img_6 = lv.img(screen_cont_3)
screen_img_6.set_pos(int(0),int(9))
screen_img_6.set_size(20,20)
screen_img_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_img_6.add_flag(lv.obj.FLAG.CLICKABLE)
try:
    with open('E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-656495659.png','rb') as f:
        screen_img_6_img_data = f.read()
except:
    print('Could not open E:\\NXP_Gui\\GUI_Project\\ST7789_Demo\\generated\\mPythonImages\\mp-656495659.png')
    sys.exit()

screen_img_6_img = lv.img_dsc_t({
  'data_size': len(screen_img_6_img_data),
  'header': {'always_zero': 0, 'w': 20, 'h': 20, 'cf': lv.img.CF.TRUE_COLOR_ALPHA},
  'data': screen_img_6_img_data
})

screen_img_6.set_src(screen_img_6_img)
screen_img_6.set_pivot(50,50)
screen_img_6.set_angle(0)
# create style style_screen_img_6_main_main_default
style_screen_img_6_main_main_default = lv.style_t()
style_screen_img_6_main_main_default.init()
style_screen_img_6_main_main_default.set_img_recolor(lv.color_make(0xff,0xff,0xff))
style_screen_img_6_main_main_default.set_img_recolor_opa(0)
style_screen_img_6_main_main_default.set_img_opa(255)

# add style for screen_img_6
screen_img_6.add_style(style_screen_img_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_label_7
screen_label_7 = lv.label(screen_cont_3)
screen_label_7.set_pos(int(24),int(9))
screen_label_7.set_size(136,18)
screen_label_7.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_7.set_text("IP Address")
screen_label_7.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_7_main_main_default
style_screen_label_7_main_main_default = lv.style_t()
style_screen_label_7_main_main_default.init()
style_screen_label_7_main_main_default.set_radius(0)
style_screen_label_7_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_7_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_7_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_7_main_main_default.set_bg_opa(255)
style_screen_label_7_main_main_default.set_text_color(lv.color_make(0xFF,0x9B,0xAA))
try:
    style_screen_label_7_main_main_default.set_text_font(lv.font_consola_16)
except AttributeError:
    try:
        style_screen_label_7_main_main_default.set_text_font(lv.font_montserrat_16)
    except AttributeError:
        style_screen_label_7_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_7_main_main_default.set_text_letter_space(0)
style_screen_label_7_main_main_default.set_text_line_space(0)
style_screen_label_7_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_7_main_main_default.set_pad_left(0)
style_screen_label_7_main_main_default.set_pad_right(0)
style_screen_label_7_main_main_default.set_pad_top(2)
style_screen_label_7_main_main_default.set_pad_bottom(0)

# add style for screen_label_7
screen_label_7.add_style(style_screen_label_7_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)

# create style style_screen_cont_3_main_main_default
style_screen_cont_3_main_main_default = lv.style_t()
style_screen_cont_3_main_main_default.init()
style_screen_cont_3_main_main_default.set_radius(5)
style_screen_cont_3_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_3_main_main_default.set_bg_grad_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_3_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_cont_3_main_main_default.set_bg_opa(255)
style_screen_cont_3_main_main_default.set_border_color(lv.color_make(0xff,0xff,0xff))
style_screen_cont_3_main_main_default.set_border_width(2)
style_screen_cont_3_main_main_default.set_border_opa(255)
style_screen_cont_3_main_main_default.set_pad_left(0)
style_screen_cont_3_main_main_default.set_pad_right(0)
style_screen_cont_3_main_main_default.set_pad_top(0)
style_screen_cont_3_main_main_default.set_pad_bottom(0)

# add style for screen_cont_3
screen_cont_3.add_style(style_screen_cont_3_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)


# create screen_label_6
screen_label_6 = lv.label(screen)
screen_label_6.set_pos(int(118),int(298))
screen_label_6.set_size(50,15)
screen_label_6.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
screen_label_6.set_text("16/64 GB")
screen_label_6.set_long_mode(lv.label.LONG.WRAP)
# create style style_screen_label_6_main_main_default
style_screen_label_6_main_main_default = lv.style_t()
style_screen_label_6_main_main_default.init()
style_screen_label_6_main_main_default.set_radius(0)
style_screen_label_6_main_main_default.set_bg_color(lv.color_make(0xff,0xff,0xff))
style_screen_label_6_main_main_default.set_bg_grad_color(lv.color_make(0x21,0x95,0xf6))
style_screen_label_6_main_main_default.set_bg_grad_dir(lv.GRAD_DIR.NONE)
style_screen_label_6_main_main_default.set_bg_opa(255)
style_screen_label_6_main_main_default.set_text_color(lv.color_make(0x00,0x00,0x00))
try:
    style_screen_label_6_main_main_default.set_text_font(lv.font_consola_10)
except AttributeError:
    try:
        style_screen_label_6_main_main_default.set_text_font(lv.font_montserrat_10)
    except AttributeError:
        style_screen_label_6_main_main_default.set_text_font(lv.font_montserrat_16)
style_screen_label_6_main_main_default.set_text_letter_space(0)
style_screen_label_6_main_main_default.set_text_line_space(0)
style_screen_label_6_main_main_default.set_text_align(lv.TEXT_ALIGN.CENTER)
style_screen_label_6_main_main_default.set_pad_left(0)
style_screen_label_6_main_main_default.set_pad_right(0)
style_screen_label_6_main_main_default.set_pad_top(3)
style_screen_label_6_main_main_default.set_pad_bottom(0)

# add style for screen_label_6
screen_label_6.add_style(style_screen_label_6_main_main_default, lv.PART.MAIN|lv.STATE.DEFAULT)




# content from custom.py

# Load the default screen
lv.scr_load(screen)

while SDL.check():
    time.sleep_ms(5)
