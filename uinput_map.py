from evdev import ecodes as e
js_map = {
	0x08: e.KEY_BACKSPACE,  # BACKSPACE
	0x09: e.KEY_TAB,        # TAB
	0x0D: e.KEY_ENTER,      # ENTER
	0x10: e.KEY_LEFTSHIFT,  # SHIFT
	0x11: e.KEY_LEFTCTRL,   # CTRL
	0x12: e.KEY_LEFTALT,    # ALT
	0x13: e.KEY_PAUSE,      # PAUSE
	0x14: e.KEY_CAPSLOCK,   # CAPS_LOCK
	0x1B: e.KEY_ESC,        # ESC
	0x20: e.KEY_SPACE,      # SPACE
	0x21: e.KEY_PAGEUP,     # PAGE_UP # also NUM_NORTH_EAST
	0x22: e.KEY_DOWN,       # PAGE_DOWN # also NUM_SOUTH_EAST
	0x23: e.KEY_END,        # END # also NUM_SOUTH_WEST
	0x24: e.KEY_HOME,       # HOME # also NUM_NORTH_WEST
	0x25: e.KEY_LEFT,       # LEFT # also NUM_WEST
	0x26: e.KEY_UP,         # UP # also NUM_NORTH
	0x27: e.KEY_RIGHT,      # RIGHT # also NUM_EAST
	0x28: e.KEY_DOWN,       # DOWN # also NUM_SOUTH
	0x2D: e.KEY_INSERT,     # INSERT # also NUM_INSERT
	0x2E: e.KEY_DELETE,     # DELETE # also NUM_DELETE
	0x30: e.KEY_0,          # ZERO
	0x31: e.KEY_1,          # ONE
	0x32: e.KEY_2,          # TWO
	0x33: e.KEY_3,          # THREE
	0x34: e.KEY_4,          # FOUR
	0x35: e.KEY_5,          # FIVE
	0x36: e.KEY_6,          # SIX
	0x37: e.KEY_7,          # SEVEN
	0x38: e.KEY_8,          # EIGHT
	0x39: e.KEY_9,          # NINE
	0x41: e.KEY_A,          # A
	0x42: e.KEY_B,          # B
	0x43: e.KEY_C,          # C
	0x44: e.KEY_D,          # D
	0x45: e.KEY_E,          # E
	0x46: e.KEY_F,          # F
	0x47: e.KEY_G,          # G
	0x48: e.KEY_H,          # H
	0x49: e.KEY_I,          # I
	0x4A: e.KEY_J,          # J
	0x4B: e.KEY_K,          # K
	0x4C: e.KEY_L,          # L
	0x4D: e.KEY_M,          # M
	0x4E: e.KEY_N,          # N
	0x4F: e.KEY_O,          # O
	0x50: e.KEY_P,          # P
	0x51: e.KEY_Q,          # Q
	0x52: e.KEY_R,          # R
	0x53: e.KEY_S,          # S
	0x54: e.KEY_T,          # T
	0x55: e.KEY_U,          # U
	0x56: e.KEY_V,          # V
	0x57: e.KEY_W,          # W
	0x58: e.KEY_X,          # X
	0x59: e.KEY_Y,          # Y
	0x5A: e.KEY_Z,          # Z
	0x5B: e.KEY_LEFTMETA,   # META # WIN_KEY_LEFT
	0x5C: e.KEY_RIGHTMETA,  # WIN_KEY_RIGHT
	0x60: e.KEY_KP0,        # NUM_ZERO
	0x61: e.KEY_KP1,        # NUM_ONE
	0x62: e.KEY_KP2,        # NUM_TWO
	0x63: e.KEY_KP3,        # NUM_THREE
	0x64: e.KEY_KP4,        # NUM_FOUR
	0x65: e.KEY_KP5,        # NUM_FIVE
	0x66: e.KEY_KP6,        # NUM_SIX
	0x67: e.KEY_KP7,        # NUM_SEVEN
	0x68: e.KEY_KP8,        # NUM_EIGHT
	0x69: e.KEY_KP9,        # NUM_NINE
	0x6A: e.KEY_KPASTERISK, # NUM_MULTIPLY
	0x6B: e.KEY_KPPLUS,     # NUM_PLUS
	0x6D: e.KEY_KPMINUS,    # NUM_MINUS
	0x6E: e.KEY_KPDOT,      # NUM_PERIOD
	0x6F: e.KEY_KPSLASH,    # NUM_DIVISION
	0x70: e.KEY_F1,         # F1
	0x71: e.KEY_F2,         # F2
	0x72: e.KEY_F3,         # F3
	0x73: e.KEY_F4,         # F4
	0x74: e.KEY_F5,         # F5
	0x75: e.KEY_F6,         # F6
	0x76: e.KEY_F7,         # F7
	0x77: e.KEY_F8,         # F8
	0x78: e.KEY_F9,         # F9
	0x79: e.KEY_F10,        # F10
	0x7A: e.KEY_F11,        # F11
	0x7B: e.KEY_F12,        # F12
	0x90: e.KEY_NUMLOCK,    # NUMLOCK
	0x91: e.KEY_SCROLLLOCK, # SCROLL_LOCK
	0xBA: e.KEY_SEMICOLON,  # SEMICOLON
	0xBC: e.KEY_COMMA,      # COMMA
	0xBE: e.KEY_DOT,        # PERIOD
	0xBF: e.KEY_SLASH,      # SLASH
	0xC0: e.KEY_GRAVE,      # APOSTROPHE
	0xDE: e.KEY_APOSTROPHE, # SINGLE_QUOTE
	0xDB: e.KEY_LEFTBRACE,  # OPEN_SQUARE_BRACKET
	0xDC: e.KEY_BACKSLASH,  # BACKSLASH
	0xDD: e.KEY_RIGHTBRACE, # CLOSE_SQUARE_BRACKET
}
