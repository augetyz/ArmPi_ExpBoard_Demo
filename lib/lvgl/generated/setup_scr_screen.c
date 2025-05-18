/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: MIT
 * The auto-generated can only be used on NXP devices
 */

#include "lvgl.h"
#include <stdio.h>
#include "gui_guider.h"
#include "events_init.h"


static lv_obj_t* screen_datetext_1_calendar;
void screen_datetext_1_calendar_event_handler(lv_event_t* e);
void screen_datetext_1_init_calendar(lv_obj_t* parent);;
void screen_datetext_1_event(lv_event_t* e)
{
	lv_event_code_t code = lv_event_get_code(e);
	lv_obj_t* btn = lv_event_get_target(e);
	if (code == LV_EVENT_FOCUSED)
	{
		if (screen_datetext_1_calendar == NULL)
		{
			screen_datetext_1_init_calendar(guider_ui.screen_cont_1);
		}
	}
}
void screen_datetext_1_init_calendar(lv_obj_t* parent)
{
	if (screen_datetext_1_calendar == NULL)
	{
		lv_obj_add_flag(lv_layer_top(), LV_OBJ_FLAG_CLICKABLE);
		screen_datetext_1_calendar = lv_calendar_create(lv_layer_top());

		lv_obj_set_size(screen_datetext_1_calendar, 240, 240);
		lv_calendar_set_showed_date(screen_datetext_1_calendar, 2022, 05);
		lv_obj_align(screen_datetext_1_calendar, LV_ALIGN_CENTER, 20, 20);

		lv_obj_add_event_cb(screen_datetext_1_calendar, screen_datetext_1_calendar_event_handler, LV_EVENT_ALL, NULL);
		lv_calendar_header_arrow_create(screen_datetext_1_calendar);
		lv_obj_update_layout(parent);
	}
}
void screen_datetext_1_calendar_event_handler(lv_event_t* e)
{
	lv_event_code_t code = lv_event_get_code(e);
	lv_obj_t* obj = lv_event_get_current_target(e);

	if (code == LV_EVENT_VALUE_CHANGED)
	{
		lv_calendar_date_t date;
		lv_calendar_get_pressed_date(obj, &date);
		char buf[16];
		lv_snprintf(buf, sizeof(buf), "%d/%02d/%02d", date.year, date.month, date.day);
		lv_label_set_text(guider_ui.screen_datetext_1, buf);
		lv_obj_clear_flag(lv_layer_top(), LV_OBJ_FLAG_CLICKABLE);
		lv_obj_set_style_bg_opa(lv_layer_top(), LV_OPA_TRANSP, 0);
		lv_obj_del(screen_datetext_1_calendar);
		screen_datetext_1_calendar = NULL;
	}
}
static int screen_digital_clock_1_hour_value = 11;
static int screen_digital_clock_1_min_value = 25;
static int screen_digital_clock_1_sec_value = 50;
#include <time.h>
void screen_digital_clock_1_timer(lv_timer_t* timer)
{
	time_t now = time(NULL);
	struct tm* tm_info = localtime(&now);

	char date_buf[16];
	strftime(date_buf, sizeof(date_buf), "%Y/%m/%d", tm_info);
	lv_label_set_text(guider_ui.screen_datetext_1, date_buf);

	char time_buf[16];
	strftime(time_buf, sizeof(time_buf), "%H:%M:%S", tm_info);
	lv_dclock_set_text_fmt(guider_ui.screen_digital_clock_1, "%s", time_buf);
}
static const lv_img_dsc_t* screen_animimg_1_imgs[100] = {
	&screen_animimg_1biubiu_00,
	&screen_animimg_1biubiu_01,
	&screen_animimg_1biubiu_02,
	&screen_animimg_1biubiu_03,
	&screen_animimg_1biubiu_04,
	&screen_animimg_1biubiu_05,
	&screen_animimg_1biubiu_06,
	&screen_animimg_1biubiu_07,
	&screen_animimg_1biubiu_08,
	&screen_animimg_1biubiu_09,
	&screen_animimg_1biubiu_10,
	&screen_animimg_1biubiu_11,
	&screen_animimg_1biubiu_12,
	&screen_animimg_1biubiu_13,
	&screen_animimg_1biubiu_14,
	&screen_animimg_1biubiu_15,
	&screen_animimg_1biubiu_16,
	&screen_animimg_1biubiu_17,
	&screen_animimg_1biubiu_18,
	&screen_animimg_1biubiu_19,
	&screen_animimg_1biubiu_20,
	&screen_animimg_1biubiu_21,
	&screen_animimg_1biubiu_22,
	&screen_animimg_1biubiu_23,
	&screen_animimg_1biubiu_24,
	&screen_animimg_1biubiu_25,
	&screen_animimg_1biubiu_26,
	&screen_animimg_1biubiu_27,
	&screen_animimg_1biubiu_28,
	&screen_animimg_1biubiu_29,
	&screen_animimg_1biubiu_30,
	&screen_animimg_1biubiu_31,
	&screen_animimg_1biubiu_32,
	&screen_animimg_1biubiu_33,
	&screen_animimg_1biubiu_34,
	&screen_animimg_1biubiu_35,
	&screen_animimg_1biubiu_36,
	&screen_animimg_1biubiu_37,
	&screen_animimg_1biubiu_38,
	&screen_animimg_1biubiu_39,
	&screen_animimg_1biubiu_40,
	&screen_animimg_1biubiu_41,
	&screen_animimg_1biubiu_42,
	&screen_animimg_1biubiu_43,
	&screen_animimg_1biubiu_44,
	&screen_animimg_1biubiu_45,
	&screen_animimg_1biubiu_46,
	&screen_animimg_1biubiu_47,
	&screen_animimg_1biubiu_48,
	&screen_animimg_1biubiu_49,
	&screen_animimg_1biubiu_50,
	&screen_animimg_1biubiu_51,
	&screen_animimg_1biubiu_52,
	&screen_animimg_1biubiu_53,
	&screen_animimg_1biubiu_54,
	&screen_animimg_1biubiu_55,
	&screen_animimg_1biubiu_56,
	&screen_animimg_1biubiu_57,
	&screen_animimg_1biubiu_58,
	&screen_animimg_1biubiu_59,
	&screen_animimg_1biubiu_60,
	&screen_animimg_1biubiu_61,
	&screen_animimg_1biubiu_62,
	&screen_animimg_1biubiu_63,
	&screen_animimg_1biubiu_64,
	&screen_animimg_1biubiu_65,
	&screen_animimg_1biubiu_66,
	&screen_animimg_1biubiu_67,
	&screen_animimg_1biubiu_68,
	&screen_animimg_1biubiu_69,
	&screen_animimg_1biubiu_70,
	&screen_animimg_1biubiu_71,
	&screen_animimg_1biubiu_72,
	&screen_animimg_1biubiu_73,
	&screen_animimg_1biubiu_74,
	&screen_animimg_1biubiu_75,
	&screen_animimg_1biubiu_76,
	&screen_animimg_1biubiu_77,
	&screen_animimg_1biubiu_78,
	&screen_animimg_1biubiu_79,
	&screen_animimg_1biubiu_80,
	&screen_animimg_1biubiu_81,
	&screen_animimg_1biubiu_82,
	&screen_animimg_1biubiu_83,
	&screen_animimg_1biubiu_84,
	&screen_animimg_1biubiu_85,
	&screen_animimg_1biubiu_86,
	&screen_animimg_1biubiu_87,
	&screen_animimg_1biubiu_88,
	&screen_animimg_1biubiu_89,
	&screen_animimg_1biubiu_90,
	&screen_animimg_1biubiu_91,
	&screen_animimg_1biubiu_92,
	&screen_animimg_1biubiu_93,
	&screen_animimg_1biubiu_94,
	&screen_animimg_1biubiu_95,
	&screen_animimg_1biubiu_96,
	&screen_animimg_1biubiu_97,
	&screen_animimg_1biubiu_98,
	&screen_animimg_1biubiu_99
};

void setup_scr_screen(lv_ui* ui)
{

	//Write codes screen
	ui->screen = lv_obj_create(NULL);
	lv_obj_set_scrollbar_mode(ui->screen, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_main_main_default
	static lv_style_t style_screen_main_main_default;
	if (style_screen_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_main_main_default);
	else
		lv_style_init(&style_screen_main_main_default);
	lv_style_set_bg_color(&style_screen_main_main_default, lv_color_make(0xe0, 0xe8, 0xee));
	lv_style_set_bg_opa(&style_screen_main_main_default, 249);
	lv_obj_add_style(ui->screen, &style_screen_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_arc_1
	ui->screen_arc_1 = lv_arc_create(ui->screen);
	lv_obj_set_pos(ui->screen_arc_1, 3, 50);
	lv_obj_set_size(ui->screen_arc_1, 100, 100);
	lv_obj_set_scrollbar_mode(ui->screen_arc_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_arc_1_main_main_default
	static lv_style_t style_screen_arc_1_main_main_default;
	if (style_screen_arc_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_arc_1_main_main_default);
	else
		lv_style_init(&style_screen_arc_1_main_main_default);
	lv_style_set_radius(&style_screen_arc_1_main_main_default, 6);
	lv_style_set_bg_color(&style_screen_arc_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_arc_1_main_main_default, lv_color_make(0xf6, 0xf6, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_arc_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_arc_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_arc_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_arc_1_main_main_default, lv_color_make(0x09, 0x8D, 0x6B));
	lv_style_set_shadow_opa(&style_screen_arc_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_arc_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_arc_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_arc_1_main_main_default, 0);
	lv_style_set_border_width(&style_screen_arc_1_main_main_default, 0);
	lv_style_set_pad_left(&style_screen_arc_1_main_main_default, 5);
	lv_style_set_pad_right(&style_screen_arc_1_main_main_default, 5);
	lv_style_set_pad_top(&style_screen_arc_1_main_main_default, 5);
	lv_style_set_pad_bottom(&style_screen_arc_1_main_main_default, 5);
	lv_style_set_arc_color(&style_screen_arc_1_main_main_default, lv_color_make(0xE6, 0xE6, 0xE6));
	lv_style_set_arc_width(&style_screen_arc_1_main_main_default, 11);
	lv_obj_add_style(ui->screen_arc_1, &style_screen_arc_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_screen_arc_1_main_indicator_default
	static lv_style_t style_screen_arc_1_main_indicator_default;
	if (style_screen_arc_1_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_screen_arc_1_main_indicator_default);
	else
		lv_style_init(&style_screen_arc_1_main_indicator_default);
	lv_style_set_arc_color(&style_screen_arc_1_main_indicator_default, lv_color_make(0x26, 0xB0, 0x8C));
	lv_style_set_arc_width(&style_screen_arc_1_main_indicator_default, 11);
	lv_obj_add_style(ui->screen_arc_1, &style_screen_arc_1_main_indicator_default, LV_PART_INDICATOR | LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_screen_arc_1_main_knob_default
	static lv_style_t style_screen_arc_1_main_knob_default;
	if (style_screen_arc_1_main_knob_default.prop_cnt > 1)
		lv_style_reset(&style_screen_arc_1_main_knob_default);
	else
		lv_style_init(&style_screen_arc_1_main_knob_default);
	lv_style_set_bg_color(&style_screen_arc_1_main_knob_default, lv_color_make(0x26, 0xB0, 0x8C));
	lv_style_set_bg_grad_color(&style_screen_arc_1_main_knob_default, lv_color_make(0xff, 0x00, 0x27));
	lv_style_set_bg_grad_dir(&style_screen_arc_1_main_knob_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_arc_1_main_knob_default, 255);
	lv_style_set_pad_all(&style_screen_arc_1_main_knob_default, 0);
	lv_obj_add_style(ui->screen_arc_1, &style_screen_arc_1_main_knob_default, LV_PART_KNOB | LV_STATE_DEFAULT);
	lv_arc_set_mode(ui->screen_arc_1, LV_ARC_MODE_NORMAL);
	lv_arc_set_range(ui->screen_arc_1, 0, 100);
	lv_arc_set_bg_angles(ui->screen_arc_1, 0, 360);
	lv_arc_set_angles(ui->screen_arc_1, 0, 0);
	lv_arc_set_rotation(ui->screen_arc_1, 90);

	//Write codes screen_arc_2
	ui->screen_arc_2 = lv_arc_create(ui->screen);
	lv_obj_set_pos(ui->screen_arc_2, 3, 153);
	lv_obj_set_size(ui->screen_arc_2, 100, 100);
	lv_obj_set_scrollbar_mode(ui->screen_arc_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_arc_2_main_main_default
	static lv_style_t style_screen_arc_2_main_main_default;
	if (style_screen_arc_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_arc_2_main_main_default);
	else
		lv_style_init(&style_screen_arc_2_main_main_default);
	lv_style_set_radius(&style_screen_arc_2_main_main_default, 6);
	lv_style_set_bg_color(&style_screen_arc_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_arc_2_main_main_default, lv_color_make(0xFA, 0xAB, 0xAB));
	lv_style_set_bg_grad_dir(&style_screen_arc_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_arc_2_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_arc_2_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_arc_2_main_main_default, lv_color_make(0x2F, 0x92, 0xDA));
	lv_style_set_shadow_opa(&style_screen_arc_2_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_arc_2_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_arc_2_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_arc_2_main_main_default, 0);
	lv_style_set_border_width(&style_screen_arc_2_main_main_default, 0);
	lv_style_set_pad_left(&style_screen_arc_2_main_main_default, 5);
	lv_style_set_pad_right(&style_screen_arc_2_main_main_default, 5);
	lv_style_set_pad_top(&style_screen_arc_2_main_main_default, 5);
	lv_style_set_pad_bottom(&style_screen_arc_2_main_main_default, 5);
	lv_style_set_arc_color(&style_screen_arc_2_main_main_default, lv_color_make(0xe6, 0xe6, 0xe6));
	lv_style_set_arc_width(&style_screen_arc_2_main_main_default, 11);
	lv_obj_add_style(ui->screen_arc_2, &style_screen_arc_2_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_screen_arc_2_main_indicator_default
	static lv_style_t style_screen_arc_2_main_indicator_default;
	if (style_screen_arc_2_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_screen_arc_2_main_indicator_default);
	else
		lv_style_init(&style_screen_arc_2_main_indicator_default);
	lv_style_set_arc_color(&style_screen_arc_2_main_indicator_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_arc_width(&style_screen_arc_2_main_indicator_default, 11);
	lv_obj_add_style(ui->screen_arc_2, &style_screen_arc_2_main_indicator_default, LV_PART_INDICATOR | LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_screen_arc_2_main_knob_default
	static lv_style_t style_screen_arc_2_main_knob_default;
	if (style_screen_arc_2_main_knob_default.prop_cnt > 1)
		lv_style_reset(&style_screen_arc_2_main_knob_default);
	else
		lv_style_init(&style_screen_arc_2_main_knob_default);
	lv_style_set_bg_color(&style_screen_arc_2_main_knob_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_color(&style_screen_arc_2_main_knob_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_arc_2_main_knob_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_arc_2_main_knob_default, 255);
	lv_style_set_pad_all(&style_screen_arc_2_main_knob_default, 0);
	lv_obj_add_style(ui->screen_arc_2, &style_screen_arc_2_main_knob_default, LV_PART_KNOB | LV_STATE_DEFAULT);
	lv_arc_set_mode(ui->screen_arc_2, LV_ARC_MODE_NORMAL);
	lv_arc_set_range(ui->screen_arc_2, 0, 100);
	lv_arc_set_bg_angles(ui->screen_arc_2, 0, 360);
	lv_arc_set_angles(ui->screen_arc_2, 0, 0);
	lv_arc_set_rotation(ui->screen_arc_2, 90);

	//Write codes screen_cont_1
	ui->screen_cont_1 = lv_obj_create(ui->screen);
	lv_obj_set_pos(ui->screen_cont_1, 1, 2);
	lv_obj_set_size(ui->screen_cont_1, 170, 45);
	lv_obj_set_scrollbar_mode(ui->screen_cont_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_cont_1_main_main_default
	static lv_style_t style_screen_cont_1_main_main_default;
	if (style_screen_cont_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_cont_1_main_main_default);
	else
		lv_style_init(&style_screen_cont_1_main_main_default);
	lv_style_set_radius(&style_screen_cont_1_main_main_default, 8);
	lv_style_set_bg_color(&style_screen_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_screen_cont_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_cont_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_cont_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_cont_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_border_color(&style_screen_cont_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_border_width(&style_screen_cont_1_main_main_default, 2);
	lv_style_set_border_opa(&style_screen_cont_1_main_main_default, 255);
	lv_style_set_pad_left(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_cont_1_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_cont_1_main_main_default, 0);
	lv_obj_add_style(ui->screen_cont_1, &style_screen_cont_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write datetext screen_datetext_1
	ui->screen_datetext_1 = lv_label_create(ui->screen_cont_1);
	lv_label_set_text(ui->screen_datetext_1, "2022/07/28");
	lv_obj_set_style_text_align(ui->screen_datetext_1, LV_TEXT_ALIGN_CENTER, 0);
	lv_obj_set_pos(ui->screen_datetext_1, 0, 0);
	lv_obj_set_size(ui->screen_datetext_1, 72, 40);

	//write datetext event
	lv_obj_add_flag(ui->screen_datetext_1, LV_OBJ_FLAG_CLICKABLE);
	lv_obj_add_event_cb(ui->screen_datetext_1, screen_datetext_1_event, LV_EVENT_ALL, NULL);

	//Write style state: LV_STATE_DEFAULT for style_screen_datetext_1_main_main_default
	static lv_style_t style_screen_datetext_1_main_main_default;
	if (style_screen_datetext_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_datetext_1_main_main_default);
	else
		lv_style_init(&style_screen_datetext_1_main_main_default);
	lv_style_set_radius(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_datetext_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_datetext_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_datetext_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_datetext_1_main_main_default, 119);
	lv_style_set_shadow_width(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_datetext_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_datetext_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_text_color(&style_screen_datetext_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_datetext_1_main_main_default, &lv_font_consola_12);
	lv_style_set_text_letter_space(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_pad_left(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_datetext_1_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_datetext_1_main_main_default, 12);
	lv_obj_add_style(ui->screen_datetext_1, &style_screen_datetext_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	static bool screen_digital_clock_1_timer_enabled = false;

	//Write codes screen_digital_clock_1
	ui->screen_digital_clock_1 = lv_dclock_create(ui->screen_cont_1, "11:25:50");
	lv_obj_set_style_text_align(ui->screen_digital_clock_1, LV_TEXT_ALIGN_CENTER, 0);
	lv_obj_set_pos(ui->screen_digital_clock_1, 107, 0);
	lv_obj_set_size(ui->screen_digital_clock_1, 59, 40);

	//create timer
	if (!screen_digital_clock_1_timer_enabled)
	{
		lv_timer_create(screen_digital_clock_1_timer, 1000, NULL);
		screen_digital_clock_1_timer_enabled = true;
	}
	//Write style state: LV_STATE_DEFAULT for style_screen_digital_clock_1_main_main_default
	static lv_style_t style_screen_digital_clock_1_main_main_default;
	if (style_screen_digital_clock_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_digital_clock_1_main_main_default);
	else
		lv_style_init(&style_screen_digital_clock_1_main_main_default);
	lv_style_set_radius(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_digital_clock_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_digital_clock_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_digital_clock_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_digital_clock_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_digital_clock_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_digital_clock_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_text_color(&style_screen_digital_clock_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_digital_clock_1_main_main_default, &lv_font_consola_12);
	lv_style_set_text_letter_space(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_pad_left(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_digital_clock_1_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_digital_clock_1_main_main_default, 12);
	lv_style_set_pad_bottom(&style_screen_digital_clock_1_main_main_default, 0);
	lv_obj_add_style(ui->screen_digital_clock_1, &style_screen_digital_clock_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_Wifi_disconnected
	ui->screen_Wifi_disconnected = lv_img_create(ui->screen_cont_1);
	lv_obj_set_pos(ui->screen_Wifi_disconnected, 81, 10);
	lv_obj_set_size(ui->screen_Wifi_disconnected, 16, 16);
	lv_obj_set_scrollbar_mode(ui->screen_Wifi_disconnected, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_wifi_disconnected_main_main_default
	static lv_style_t style_screen_wifi_disconnected_main_main_default;
	if (style_screen_wifi_disconnected_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_wifi_disconnected_main_main_default);
	else
		lv_style_init(&style_screen_wifi_disconnected_main_main_default);
	lv_style_set_img_recolor(&style_screen_wifi_disconnected_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_wifi_disconnected_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_wifi_disconnected_main_main_default, 255);
	lv_obj_add_style(ui->screen_Wifi_disconnected, &style_screen_wifi_disconnected_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_Wifi_disconnected, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_Wifi_disconnected, &_wifiexclamation_15x15);
	lv_img_set_pivot(ui->screen_Wifi_disconnected, 50, 50);
	lv_img_set_angle(ui->screen_Wifi_disconnected, 0);

	//Write codes screen_WIfi_connected
	ui->screen_WIfi_connected = lv_img_create(ui->screen_cont_1);
	lv_obj_set_pos(ui->screen_WIfi_connected, 81, 10);
	lv_obj_set_size(ui->screen_WIfi_connected, 16, 16);
	lv_obj_set_scrollbar_mode(ui->screen_WIfi_connected, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_wifi_connected_main_main_default
	static lv_style_t style_screen_wifi_connected_main_main_default;
	if (style_screen_wifi_connected_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_wifi_connected_main_main_default);
	else
		lv_style_init(&style_screen_wifi_connected_main_main_default);
	lv_style_set_img_recolor(&style_screen_wifi_connected_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_wifi_connected_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_wifi_connected_main_main_default, 255);
	lv_obj_add_style(ui->screen_WIfi_connected, &style_screen_wifi_connected_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_WIfi_connected, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_WIfi_connected, &_wifi_15x15);
	lv_img_set_pivot(ui->screen_WIfi_connected, 50, 50);
	lv_img_set_angle(ui->screen_WIfi_connected, 0);

	//Write codes screen_label_1
	ui->screen_label_1 = lv_label_create(ui->screen);
	lv_obj_set_pos(ui->screen_label_1, 30, 85);
	lv_obj_set_size(ui->screen_label_1, 46, 31);
	lv_obj_set_scrollbar_mode(ui->screen_label_1, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_1, "99.1%\nCPU");
	lv_label_set_long_mode(ui->screen_label_1, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_1_main_main_default
	static lv_style_t style_screen_label_1_main_main_default;
	if (style_screen_label_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_1_main_main_default);
	else
		lv_style_init(&style_screen_label_1_main_main_default);
	lv_style_set_radius(&style_screen_label_1_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_1_main_main_default, 0);
	lv_style_set_shadow_width(&style_screen_label_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_1_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_1_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_label_1_main_main_default, &lv_font_consola_12);
	lv_style_set_text_letter_space(&style_screen_label_1_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_1_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_1_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_1_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_1_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_1_main_main_default, 4);
	lv_style_set_pad_bottom(&style_screen_label_1_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_1, &style_screen_label_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_label_2
	ui->screen_label_2 = lv_label_create(ui->screen);
	lv_obj_set_pos(ui->screen_label_2, 30, 189);
	lv_obj_set_size(ui->screen_label_2, 46, 29);
	lv_obj_set_scrollbar_mode(ui->screen_label_2, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_2, "15.8%\nRAM");
	lv_label_set_long_mode(ui->screen_label_2, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_2_main_main_default
	static lv_style_t style_screen_label_2_main_main_default;
	if (style_screen_label_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_2_main_main_default);
	else
		lv_style_init(&style_screen_label_2_main_main_default);
	lv_style_set_radius(&style_screen_label_2_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_2_main_main_default, 0);
	lv_style_set_shadow_width(&style_screen_label_2_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_2_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_2_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_2_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_2_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_2_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_label_2_main_main_default, &lv_font_consola_12);
	lv_style_set_text_letter_space(&style_screen_label_2_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_2_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_2_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_2_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_2_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_2_main_main_default, 4);
	lv_style_set_pad_bottom(&style_screen_label_2_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_2, &style_screen_label_2_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_cont_2
	ui->screen_cont_2 = lv_obj_create(ui->screen);
	lv_obj_set_pos(ui->screen_cont_2, 105, 50);
	lv_obj_set_size(ui->screen_cont_2, 66, 120);
	lv_obj_set_scrollbar_mode(ui->screen_cont_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_cont_2_main_main_default
	static lv_style_t style_screen_cont_2_main_main_default;
	if (style_screen_cont_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_cont_2_main_main_default);
	else
		lv_style_init(&style_screen_cont_2_main_main_default);
	lv_style_set_radius(&style_screen_cont_2_main_main_default, 5);
	lv_style_set_bg_color(&style_screen_cont_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_cont_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_screen_cont_2_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_cont_2_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_cont_2_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_cont_2_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_border_color(&style_screen_cont_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_border_width(&style_screen_cont_2_main_main_default, 2);
	lv_style_set_border_opa(&style_screen_cont_2_main_main_default, 255);
	lv_style_set_pad_left(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_cont_2_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_cont_2_main_main_default, 0);
	lv_obj_add_style(ui->screen_cont_2, &style_screen_cont_2_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_img_1
	ui->screen_img_1 = lv_img_create(ui->screen_cont_2);
	lv_obj_set_pos(ui->screen_img_1, 21, 11);
	lv_obj_set_size(ui->screen_img_1, 20, 20);
	lv_obj_set_scrollbar_mode(ui->screen_img_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_img_1_main_main_default
	static lv_style_t style_screen_img_1_main_main_default;
	if (style_screen_img_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_img_1_main_main_default);
	else
		lv_style_init(&style_screen_img_1_main_main_default);
	lv_style_set_img_recolor(&style_screen_img_1_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_img_1_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_img_1_main_main_default, 255);
	lv_obj_add_style(ui->screen_img_1, &style_screen_img_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_img_1, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_img_1, &_flow_20x20);
	lv_img_set_pivot(ui->screen_img_1, 50, 50);
	lv_img_set_angle(ui->screen_img_1, 0);

	//Write codes screen_img_4
	ui->screen_img_4 = lv_img_create(ui->screen_cont_2);
	lv_obj_set_pos(ui->screen_img_4, 0, 94);
	lv_obj_set_size(ui->screen_img_4, 15, 15);
	lv_obj_set_scrollbar_mode(ui->screen_img_4, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_img_4_main_main_default
	static lv_style_t style_screen_img_4_main_main_default;
	if (style_screen_img_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_img_4_main_main_default);
	else
		lv_style_init(&style_screen_img_4_main_main_default);
	lv_style_set_img_recolor(&style_screen_img_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_img_4_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_img_4_main_main_default, 255);
	lv_obj_add_style(ui->screen_img_4, &style_screen_img_4_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_img_4, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_img_4, &_temp_15x15);
	lv_img_set_pivot(ui->screen_img_4, 50, 50);
	lv_img_set_angle(ui->screen_img_4, 0);

	//Write codes screen_img_2
	ui->screen_img_2 = lv_img_create(ui->screen);
	lv_obj_set_pos(ui->screen_img_2, 110, 95);
	lv_obj_set_size(ui->screen_img_2, 10, 10);
	lv_obj_set_scrollbar_mode(ui->screen_img_2, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_img_2_main_main_default
	static lv_style_t style_screen_img_2_main_main_default;
	if (style_screen_img_2_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_img_2_main_main_default);
	else
		lv_style_init(&style_screen_img_2_main_main_default);
	lv_style_set_img_recolor(&style_screen_img_2_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_img_2_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_img_2_main_main_default, 255);
	lv_obj_add_style(ui->screen_img_2, &style_screen_img_2_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_img_2, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_img_2, &_upload_10x10);
	lv_img_set_pivot(ui->screen_img_2, 50, 50);
	lv_img_set_angle(ui->screen_img_2, 0);

	//Write codes screen_img_3
	ui->screen_img_3 = lv_img_create(ui->screen);
	lv_obj_set_pos(ui->screen_img_3, 110, 120);
	lv_obj_set_size(ui->screen_img_3, 10, 10);
	lv_obj_set_scrollbar_mode(ui->screen_img_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_img_3_main_main_default
	static lv_style_t style_screen_img_3_main_main_default;
	if (style_screen_img_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_img_3_main_main_default);
	else
		lv_style_init(&style_screen_img_3_main_main_default);
	lv_style_set_img_recolor(&style_screen_img_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_img_3_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_img_3_main_main_default, 255);
	lv_obj_add_style(ui->screen_img_3, &style_screen_img_3_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_img_3, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_img_3, &_download_10x10);
	lv_img_set_pivot(ui->screen_img_3, 50, 50);
	lv_img_set_angle(ui->screen_img_3, 0);

	//Write codes screen_label_3
	ui->screen_label_3 = lv_label_create(ui->screen);
	lv_obj_set_pos(ui->screen_label_3, 120, 87);
	lv_obj_set_size(ui->screen_label_3, 52, 26);
	lv_obj_set_scrollbar_mode(ui->screen_label_3, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_3, "1.0 KB/s");
	lv_label_set_long_mode(ui->screen_label_3, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_3_main_main_default
	static lv_style_t style_screen_label_3_main_main_default;
	if (style_screen_label_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_3_main_main_default);
	else
		lv_style_init(&style_screen_label_3_main_main_default);
	lv_style_set_radius(&style_screen_label_3_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_3_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_label_3_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_3_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_3_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_3_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_3_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_3_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_label_3_main_main_default, &lv_font_consola_10);
	lv_style_set_text_letter_space(&style_screen_label_3_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_3_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_3_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_3_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_3_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_3_main_main_default, 7);
	lv_style_set_pad_bottom(&style_screen_label_3_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_3, &style_screen_label_3_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_animimg_1
	ui->screen_animimg_1 = lv_animimg_create(ui->screen);
	lv_obj_set_pos(ui->screen_animimg_1, 107, 172);
	lv_obj_set_size(ui->screen_animimg_1, 61, 81);
	lv_obj_set_scrollbar_mode(ui->screen_animimg_1, LV_SCROLLBAR_MODE_OFF);
	lv_animimg_set_src(ui->screen_animimg_1, (const void**)screen_animimg_1_imgs, 100);
	lv_animimg_set_duration(ui->screen_animimg_1, 6000);
	lv_animimg_set_repeat_count(ui->screen_animimg_1, 1410065408);
	lv_animimg_start(ui->screen_animimg_1);

	//Write codes screen_label_4
	ui->screen_label_4 = lv_label_create(ui->screen);
	lv_obj_set_pos(ui->screen_label_4, 120, 112);
	lv_obj_set_size(ui->screen_label_4, 52, 26);
	lv_obj_set_scrollbar_mode(ui->screen_label_4, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_4, "100.0 MB/s");
	lv_label_set_long_mode(ui->screen_label_4, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_4_main_main_default
	static lv_style_t style_screen_label_4_main_main_default;
	if (style_screen_label_4_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_4_main_main_default);
	else
		lv_style_init(&style_screen_label_4_main_main_default);
	lv_style_set_radius(&style_screen_label_4_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_4_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_4_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_4_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_4_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_label_4_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_4_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_4_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_4_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_4_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_4_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_4_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_label_4_main_main_default, &lv_font_consola_10);
	lv_style_set_text_letter_space(&style_screen_label_4_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_4_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_4_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_4_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_4_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_4_main_main_default, 8);
	lv_style_set_pad_bottom(&style_screen_label_4_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_4, &style_screen_label_4_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_label_5
	ui->screen_label_5 = lv_label_create(ui->screen);
	lv_obj_set_pos(ui->screen_label_5, 120, 140);
	lv_obj_set_size(ui->screen_label_5, 52, 26);
	lv_obj_set_scrollbar_mode(ui->screen_label_5, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_5, "0.0 C");
	lv_label_set_long_mode(ui->screen_label_5, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_5_main_main_default
	static lv_style_t style_screen_label_5_main_main_default;
	if (style_screen_label_5_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_5_main_main_default);
	else
		lv_style_init(&style_screen_label_5_main_main_default);
	lv_style_set_radius(&style_screen_label_5_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_5_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_5_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_5_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_5_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_label_5_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_5_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_5_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_5_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_5_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_5_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_5_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_label_5_main_main_default, &lv_font_consola_10);
	lv_style_set_text_letter_space(&style_screen_label_5_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_5_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_5_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_5_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_5_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_5_main_main_default, 8);
	lv_style_set_pad_bottom(&style_screen_label_5_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_5, &style_screen_label_5_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_cont_3
	ui->screen_cont_3 = lv_obj_create(ui->screen);
	lv_obj_set_pos(ui->screen_cont_3, 3, 256);
	lv_obj_set_size(ui->screen_cont_3, 166, 62);
	lv_obj_set_scrollbar_mode(ui->screen_cont_3, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_cont_3_main_main_default
	static lv_style_t style_screen_cont_3_main_main_default;
	if (style_screen_cont_3_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_cont_3_main_main_default);
	else
		lv_style_init(&style_screen_cont_3_main_main_default);
	lv_style_set_radius(&style_screen_cont_3_main_main_default, 5);
	lv_style_set_bg_color(&style_screen_cont_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_cont_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_dir(&style_screen_cont_3_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_cont_3_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_cont_3_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_cont_3_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_border_color(&style_screen_cont_3_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_border_width(&style_screen_cont_3_main_main_default, 2);
	lv_style_set_border_opa(&style_screen_cont_3_main_main_default, 255);
	lv_style_set_pad_left(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_cont_3_main_main_default, 0);
	lv_style_set_pad_bottom(&style_screen_cont_3_main_main_default, 0);
	lv_obj_add_style(ui->screen_cont_3, &style_screen_cont_3_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_img_5
	ui->screen_img_5 = lv_img_create(ui->screen_cont_3);
	lv_obj_set_pos(ui->screen_img_5, 0, 38);
	lv_obj_set_size(ui->screen_img_5, 20, 20);
	lv_obj_set_scrollbar_mode(ui->screen_img_5, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_img_5_main_main_default
	static lv_style_t style_screen_img_5_main_main_default;
	if (style_screen_img_5_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_img_5_main_main_default);
	else
		lv_style_init(&style_screen_img_5_main_main_default);
	lv_style_set_img_recolor(&style_screen_img_5_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_img_5_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_img_5_main_main_default, 255);
	lv_obj_add_style(ui->screen_img_5, &style_screen_img_5_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_img_5, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_img_5, &_floppydiskr_20x20);
	lv_img_set_pivot(ui->screen_img_5, 50, 50);
	lv_img_set_angle(ui->screen_img_5, 0);

	//Write codes screen_bar_1
	ui->screen_bar_1 = lv_bar_create(ui->screen_cont_3);
	lv_obj_set_pos(ui->screen_bar_1, 23, 42);
	lv_obj_set_size(ui->screen_bar_1, 90, 12);
	lv_obj_set_scrollbar_mode(ui->screen_bar_1, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_bar_1_main_main_default
	static lv_style_t style_screen_bar_1_main_main_default;
	if (style_screen_bar_1_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_bar_1_main_main_default);
	else
		lv_style_init(&style_screen_bar_1_main_main_default);
	lv_style_set_radius(&style_screen_bar_1_main_main_default, 10);
	lv_style_set_bg_color(&style_screen_bar_1_main_main_default, lv_color_make(0xce, 0xce, 0xce));
	lv_style_set_bg_grad_color(&style_screen_bar_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_bar_1_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_bar_1_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_bar_1_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_bar_1_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_bar_1_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_bar_1_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_bar_1_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_bar_1_main_main_default, 0);
	lv_obj_add_style(ui->screen_bar_1, &style_screen_bar_1_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write style state: LV_STATE_DEFAULT for style_screen_bar_1_main_indicator_default
	static lv_style_t style_screen_bar_1_main_indicator_default;
	if (style_screen_bar_1_main_indicator_default.prop_cnt > 1)
		lv_style_reset(&style_screen_bar_1_main_indicator_default);
	else
		lv_style_init(&style_screen_bar_1_main_indicator_default);
	lv_style_set_radius(&style_screen_bar_1_main_indicator_default, 10);
	lv_style_set_bg_color(&style_screen_bar_1_main_indicator_default, lv_color_make(0xff, 0x9b, 0xaa));
	lv_style_set_bg_grad_color(&style_screen_bar_1_main_indicator_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_bar_1_main_indicator_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_bar_1_main_indicator_default, 255);
	lv_obj_add_style(ui->screen_bar_1, &style_screen_bar_1_main_indicator_default, LV_PART_INDICATOR | LV_STATE_DEFAULT);
	lv_obj_set_style_anim_time(ui->screen_bar_1, 1000, 0);
	lv_bar_set_mode(ui->screen_bar_1, LV_BAR_MODE_NORMAL);
	lv_bar_set_value(ui->screen_bar_1, 50, LV_ANIM_OFF);

	//Write codes screen_img_6
	ui->screen_img_6 = lv_img_create(ui->screen_cont_3);
	lv_obj_set_pos(ui->screen_img_6, 0, 9);
	lv_obj_set_size(ui->screen_img_6, 20, 20);
	lv_obj_set_scrollbar_mode(ui->screen_img_6, LV_SCROLLBAR_MODE_OFF);

	//Write style state: LV_STATE_DEFAULT for style_screen_img_6_main_main_default
	static lv_style_t style_screen_img_6_main_main_default;
	if (style_screen_img_6_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_img_6_main_main_default);
	else
		lv_style_init(&style_screen_img_6_main_main_default);
	lv_style_set_img_recolor(&style_screen_img_6_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_img_recolor_opa(&style_screen_img_6_main_main_default, 0);
	lv_style_set_img_opa(&style_screen_img_6_main_main_default, 255);
	lv_obj_add_style(ui->screen_img_6, &style_screen_img_6_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
	lv_obj_add_flag(ui->screen_img_6, LV_OBJ_FLAG_CLICKABLE);
	lv_img_set_src(ui->screen_img_6, &_networksolid_20x20);
	lv_img_set_pivot(ui->screen_img_6, 50, 50);
	lv_img_set_angle(ui->screen_img_6, 0);

	//Write codes screen_label_7
	ui->screen_label_7 = lv_label_create(ui->screen_cont_3);
	lv_obj_set_pos(ui->screen_label_7, 24, 9);
	lv_obj_set_size(ui->screen_label_7, 136, 18);
	lv_obj_set_scrollbar_mode(ui->screen_label_7, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_7, "IP Address");
	lv_label_set_long_mode(ui->screen_label_7, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_7_main_main_default
	static lv_style_t style_screen_label_7_main_main_default;
	if (style_screen_label_7_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_7_main_main_default);
	else
		lv_style_init(&style_screen_label_7_main_main_default);
	lv_style_set_radius(&style_screen_label_7_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_7_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_7_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_7_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_7_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_label_7_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_7_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_7_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_7_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_7_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_7_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_7_main_main_default, lv_color_make(0xFF, 0x9B, 0xAA));
	lv_style_set_text_font(&style_screen_label_7_main_main_default, &lv_font_consola_16);
	lv_style_set_text_letter_space(&style_screen_label_7_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_7_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_7_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_7_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_7_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_7_main_main_default, 2);
	lv_style_set_pad_bottom(&style_screen_label_7_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_7, &style_screen_label_7_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);

	//Write codes screen_label_6
	ui->screen_label_6 = lv_label_create(ui->screen);
	lv_obj_set_pos(ui->screen_label_6, 118, 298);
	lv_obj_set_size(ui->screen_label_6, 50, 15);
	lv_obj_set_scrollbar_mode(ui->screen_label_6, LV_SCROLLBAR_MODE_OFF);
	lv_label_set_text(ui->screen_label_6, "16/64 GB");
	lv_label_set_long_mode(ui->screen_label_6, LV_LABEL_LONG_WRAP);

	//Write style state: LV_STATE_DEFAULT for style_screen_label_6_main_main_default
	static lv_style_t style_screen_label_6_main_main_default;
	if (style_screen_label_6_main_main_default.prop_cnt > 1)
		lv_style_reset(&style_screen_label_6_main_main_default);
	else
		lv_style_init(&style_screen_label_6_main_main_default);
	lv_style_set_radius(&style_screen_label_6_main_main_default, 0);
	lv_style_set_bg_color(&style_screen_label_6_main_main_default, lv_color_make(0xff, 0xff, 0xff));
	lv_style_set_bg_grad_color(&style_screen_label_6_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_bg_grad_dir(&style_screen_label_6_main_main_default, LV_GRAD_DIR_NONE);
	lv_style_set_bg_opa(&style_screen_label_6_main_main_default, 255);
	lv_style_set_shadow_width(&style_screen_label_6_main_main_default, 0);
	lv_style_set_shadow_color(&style_screen_label_6_main_main_default, lv_color_make(0x21, 0x95, 0xf6));
	lv_style_set_shadow_opa(&style_screen_label_6_main_main_default, 255);
	lv_style_set_shadow_spread(&style_screen_label_6_main_main_default, 0);
	lv_style_set_shadow_ofs_x(&style_screen_label_6_main_main_default, 0);
	lv_style_set_shadow_ofs_y(&style_screen_label_6_main_main_default, 0);
	lv_style_set_text_color(&style_screen_label_6_main_main_default, lv_color_make(0x00, 0x00, 0x00));
	lv_style_set_text_font(&style_screen_label_6_main_main_default, &lv_font_consola_10);
	lv_style_set_text_letter_space(&style_screen_label_6_main_main_default, 0);
	lv_style_set_text_line_space(&style_screen_label_6_main_main_default, 0);
	lv_style_set_text_align(&style_screen_label_6_main_main_default, LV_TEXT_ALIGN_CENTER);
	lv_style_set_pad_left(&style_screen_label_6_main_main_default, 0);
	lv_style_set_pad_right(&style_screen_label_6_main_main_default, 0);
	lv_style_set_pad_top(&style_screen_label_6_main_main_default, 3);
	lv_style_set_pad_bottom(&style_screen_label_6_main_main_default, 0);
	lv_obj_add_style(ui->screen_label_6, &style_screen_label_6_main_main_default, LV_PART_MAIN | LV_STATE_DEFAULT);
}