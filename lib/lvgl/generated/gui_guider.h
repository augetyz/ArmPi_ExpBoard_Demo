/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#ifndef GUI_GUIDER_H
#define GUI_GUIDER_H
#ifdef __cplusplus
extern "C" {
#endif

#include "lvgl.h"
#include "guider_fonts.h"

typedef struct
{
	lv_obj_t *screen;
	bool screen_del;
	lv_obj_t *screen_arc_1;
	lv_obj_t *screen_arc_2;
	lv_obj_t *screen_cont_1;
	lv_obj_t *screen_datetext_1;
	lv_obj_t *screen_digital_clock_1;
	lv_obj_t *screen_Wifi_disconnected;
	lv_obj_t *screen_WIfi_connected;
	lv_obj_t *screen_label_1;
	lv_obj_t *screen_label_2;
	lv_obj_t *screen_cont_2;
	lv_obj_t *screen_img_1;
	lv_obj_t *screen_img_4;
	lv_obj_t *screen_img_2;
	lv_obj_t *screen_img_3;
	lv_obj_t *screen_label_3;
	lv_obj_t *screen_animimg_1;
	lv_obj_t *screen_label_4;
	lv_obj_t *screen_label_5;
	lv_obj_t *screen_cont_3;
	lv_obj_t *screen_img_5;
	lv_obj_t *screen_bar_1;
	lv_obj_t *screen_img_6;
	lv_obj_t *screen_label_7;
	lv_obj_t *screen_label_6;
}lv_ui;

void init_scr_del_flag(lv_ui *ui);
void setup_ui(lv_ui *ui);
extern lv_ui guider_ui;
void setup_scr_screen(lv_ui *ui);

#include "extra/widgets/animimg/lv_animimg.h"
LV_IMG_DECLARE(screen_animimg_1biubiu_00)
LV_IMG_DECLARE(screen_animimg_1biubiu_01)
LV_IMG_DECLARE(screen_animimg_1biubiu_02)
LV_IMG_DECLARE(screen_animimg_1biubiu_03)
LV_IMG_DECLARE(screen_animimg_1biubiu_04)
LV_IMG_DECLARE(screen_animimg_1biubiu_05)
LV_IMG_DECLARE(screen_animimg_1biubiu_06)
LV_IMG_DECLARE(screen_animimg_1biubiu_07)
LV_IMG_DECLARE(screen_animimg_1biubiu_08)
LV_IMG_DECLARE(screen_animimg_1biubiu_09)
LV_IMG_DECLARE(screen_animimg_1biubiu_10)
LV_IMG_DECLARE(screen_animimg_1biubiu_11)
LV_IMG_DECLARE(screen_animimg_1biubiu_12)
LV_IMG_DECLARE(screen_animimg_1biubiu_13)
LV_IMG_DECLARE(screen_animimg_1biubiu_14)
LV_IMG_DECLARE(screen_animimg_1biubiu_15)
LV_IMG_DECLARE(screen_animimg_1biubiu_16)
LV_IMG_DECLARE(screen_animimg_1biubiu_17)
LV_IMG_DECLARE(screen_animimg_1biubiu_18)
LV_IMG_DECLARE(screen_animimg_1biubiu_19)
LV_IMG_DECLARE(screen_animimg_1biubiu_20)
LV_IMG_DECLARE(screen_animimg_1biubiu_21)
LV_IMG_DECLARE(screen_animimg_1biubiu_22)
LV_IMG_DECLARE(screen_animimg_1biubiu_23)
LV_IMG_DECLARE(screen_animimg_1biubiu_24)
LV_IMG_DECLARE(screen_animimg_1biubiu_25)
LV_IMG_DECLARE(screen_animimg_1biubiu_26)
LV_IMG_DECLARE(screen_animimg_1biubiu_27)
LV_IMG_DECLARE(screen_animimg_1biubiu_28)
LV_IMG_DECLARE(screen_animimg_1biubiu_29)
LV_IMG_DECLARE(screen_animimg_1biubiu_30)
LV_IMG_DECLARE(screen_animimg_1biubiu_31)
LV_IMG_DECLARE(screen_animimg_1biubiu_32)
LV_IMG_DECLARE(screen_animimg_1biubiu_33)
LV_IMG_DECLARE(screen_animimg_1biubiu_34)
LV_IMG_DECLARE(screen_animimg_1biubiu_35)
LV_IMG_DECLARE(screen_animimg_1biubiu_36)
LV_IMG_DECLARE(screen_animimg_1biubiu_37)
LV_IMG_DECLARE(screen_animimg_1biubiu_38)
LV_IMG_DECLARE(screen_animimg_1biubiu_39)
LV_IMG_DECLARE(screen_animimg_1biubiu_40)
LV_IMG_DECLARE(screen_animimg_1biubiu_41)
LV_IMG_DECLARE(screen_animimg_1biubiu_42)
LV_IMG_DECLARE(screen_animimg_1biubiu_43)
LV_IMG_DECLARE(screen_animimg_1biubiu_44)
LV_IMG_DECLARE(screen_animimg_1biubiu_45)
LV_IMG_DECLARE(screen_animimg_1biubiu_46)
LV_IMG_DECLARE(screen_animimg_1biubiu_47)
LV_IMG_DECLARE(screen_animimg_1biubiu_48)
LV_IMG_DECLARE(screen_animimg_1biubiu_49)
LV_IMG_DECLARE(screen_animimg_1biubiu_50)
LV_IMG_DECLARE(screen_animimg_1biubiu_51)
LV_IMG_DECLARE(screen_animimg_1biubiu_52)
LV_IMG_DECLARE(screen_animimg_1biubiu_53)
LV_IMG_DECLARE(screen_animimg_1biubiu_54)
LV_IMG_DECLARE(screen_animimg_1biubiu_55)
LV_IMG_DECLARE(screen_animimg_1biubiu_56)
LV_IMG_DECLARE(screen_animimg_1biubiu_57)
LV_IMG_DECLARE(screen_animimg_1biubiu_58)
LV_IMG_DECLARE(screen_animimg_1biubiu_59)
LV_IMG_DECLARE(screen_animimg_1biubiu_60)
LV_IMG_DECLARE(screen_animimg_1biubiu_61)
LV_IMG_DECLARE(screen_animimg_1biubiu_62)
LV_IMG_DECLARE(screen_animimg_1biubiu_63)
LV_IMG_DECLARE(screen_animimg_1biubiu_64)
LV_IMG_DECLARE(screen_animimg_1biubiu_65)
LV_IMG_DECLARE(screen_animimg_1biubiu_66)
LV_IMG_DECLARE(screen_animimg_1biubiu_67)
LV_IMG_DECLARE(screen_animimg_1biubiu_68)
LV_IMG_DECLARE(screen_animimg_1biubiu_69)
LV_IMG_DECLARE(screen_animimg_1biubiu_70)
LV_IMG_DECLARE(screen_animimg_1biubiu_71)
LV_IMG_DECLARE(screen_animimg_1biubiu_72)
LV_IMG_DECLARE(screen_animimg_1biubiu_73)
LV_IMG_DECLARE(screen_animimg_1biubiu_74)
LV_IMG_DECLARE(screen_animimg_1biubiu_75)
LV_IMG_DECLARE(screen_animimg_1biubiu_76)
LV_IMG_DECLARE(screen_animimg_1biubiu_77)
LV_IMG_DECLARE(screen_animimg_1biubiu_78)
LV_IMG_DECLARE(screen_animimg_1biubiu_79)
LV_IMG_DECLARE(screen_animimg_1biubiu_80)
LV_IMG_DECLARE(screen_animimg_1biubiu_81)
LV_IMG_DECLARE(screen_animimg_1biubiu_82)
LV_IMG_DECLARE(screen_animimg_1biubiu_83)
LV_IMG_DECLARE(screen_animimg_1biubiu_84)
LV_IMG_DECLARE(screen_animimg_1biubiu_85)
LV_IMG_DECLARE(screen_animimg_1biubiu_86)
LV_IMG_DECLARE(screen_animimg_1biubiu_87)
LV_IMG_DECLARE(screen_animimg_1biubiu_88)
LV_IMG_DECLARE(screen_animimg_1biubiu_89)
LV_IMG_DECLARE(screen_animimg_1biubiu_90)
LV_IMG_DECLARE(screen_animimg_1biubiu_91)
LV_IMG_DECLARE(screen_animimg_1biubiu_92)
LV_IMG_DECLARE(screen_animimg_1biubiu_93)
LV_IMG_DECLARE(screen_animimg_1biubiu_94)
LV_IMG_DECLARE(screen_animimg_1biubiu_95)
LV_IMG_DECLARE(screen_animimg_1biubiu_96)
LV_IMG_DECLARE(screen_animimg_1biubiu_97)
LV_IMG_DECLARE(screen_animimg_1biubiu_98)
LV_IMG_DECLARE(screen_animimg_1biubiu_99)
LV_IMG_DECLARE(_floppydiskr_20x20);
LV_IMG_DECLARE(_temp_15x15);
LV_IMG_DECLARE(_upload_10x10);
LV_IMG_DECLARE(_wifiexclamation_15x15);
LV_IMG_DECLARE(_download_10x10);
LV_IMG_DECLARE(_flow_20x20);
LV_IMG_DECLARE(_wifi_15x15);
LV_IMG_DECLARE(_networksolid_20x20);

#ifdef __cplusplus
}
#endif
#endif