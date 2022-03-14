#include "../../include/common.h"

static char file_percentage[5] = "";
static char golden_count[4] = "";
static char balanced_igt[20] = "";
static char balanced_igt_seconds[10] = "";
static char blueprints_count[5] = "";
static char move_count_str[10] = "";
static const short key_flag_array[] = {0x1A,0x4A,0x8A,0xA8,0xEC,0x124,0x13D,0x17C};

#define LINE_GAP 0x8C

int* display_images(int* dl) {
	int y_offset = FileScreenDLOffset - 720;
	for (int i = 0; i < 8; i++) {
		float divisor = (checkFlag(key_flag_array[i],0) ^ 1) + 1;
		if (divisor == 0) {
			divisor = 1;
		}
		float opacity_mult = 1.0f / divisor;
		float opacity_f = 255 * opacity_mult;
		int opacity_i = opacity_f;
		if (opacity_i > 255) {
			opacity_i = 255;
		}
		dl = drawImage(dl, 107 + i, RGBA16, 32, 32, 900 + (150 * (i % 2)), (450 + y_offset + (80 * (i / 2))),4.0f, 4.0f,opacity_i);
	}
	dl = drawImage(dl, 115, RGBA16, 32, 32, 200, y_offset + 450,4.0f, 4.0f,0xFF);
	dl = drawImage(dl, 116, RGBA16, 32, 32, 500, y_offset + 720,3.0f, 3.0f,0xFF);
	return dl;
}


int* display_text(int* dl) {
	if (Rando.unlock_kongs) {
		for (int i = 0; i < 5; i++) {
			KongUnlockedMenuArray[i] = 1;
		}
	}
	// File Percentage
	int y = FileScreenDLOffset - 320;
	dk_strFormat((char*)file_percentage, "%d%%", FilePercentage);
	dl = displayText(dl,1,0x280,y,(char*)file_percentage,0x81);
	// Move Count
	int move_count = 1;
	if (Rando.camera_unlocked) {
		move_count += 1;
	}
	if (Rando.unlock_moves) {
		move_count += 32; // All moves except sniper and camera
		move_count += (MovesBase[0].weapon_bitfield >> 2) & 1; // Sniper Scope
	} else {
		if ((!Rando.camera_unlocked) && (checkFlag(0x179,0))) {
			move_count += 1; // Fairy Camera
		}
		if (MovesBase[0].simian_slam > 1) {
			move_count += (MovesBase[0].simian_slam - 1); // Simian Slam
		}
		move_count += MovesBase[0].ammo_belt;
		int btf_value = MovesBase[0].weapon_bitfield >> 1;
		for (int i = 0; i < 2; i++) {
			move_count += (btf_value & 1);
			btf_value >>= 1;
		}
		move_count += (MovesBase[0].instrument_bitfield >> 1) & 1;
		move_count += (MovesBase[0].instrument_bitfield >> 3) & 1;
		for (int i = 0; i < 5; i++) {
			move_count += (MovesBase[i].weapon_bitfield & 1); // Base Gun
			move_count += (MovesBase[i].instrument_bitfield & 1); // Base Instrument
			btf_value = MovesBase[i].special_moves;
			for (int j = 0; j < 3; j++) {
				move_count += btf_value & 1;
				btf_value >>= 1;
			}
		}
	}
	dk_strFormat((char*)move_count_str, "%02d", move_count);
	dl = displayText(dl,1,0x140,y,(char*)move_count_str,0x81);	
	// GB Count
	y += LINE_GAP;
	dk_strFormat((char*)golden_count, "%03d", FileGBCount);
	dl = displayText(dl,1,0x280,y,(char*)golden_count,0x81);
	// Blueprint Count
	y += LINE_GAP;
	int blueprints = countFlagArray(0x1D5,40,0);
	dk_strFormat((char*)blueprints_count, "%02d", blueprints);
	dl = displayText(dl,1,0x280,y,(char*)blueprints_count,0x81);
	// Balanced IGT
	y += LINE_GAP;
	int secs = BalancedIGT % 1800;
	float secsf = secs;
	secsf /= 30;
	int hm = BalancedIGT / 1800;
	int minutes = hm % 60;
	int hours = hm / 60;
	if (secs < 300) {
		dk_strFormat((char*)balanced_igt_seconds,"0%f",secsf);
	} else {
		dk_strFormat((char*)balanced_igt_seconds,"%f",secsf);
	}
	balanced_igt_seconds[4] = 0;
	dk_strFormat((char*)balanced_igt, "%03d:%02d:%s",hours,minutes,(char*)balanced_igt_seconds);
	dl = displayText(dl,1,0x280,y,(char*)balanced_igt,0x81);
	dl = display_images(dl);
	return dl;
}