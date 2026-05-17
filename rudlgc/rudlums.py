from enum import IntEnum


class MessageNum(IntEnum):
    INFO = 0
    WARNING = 1
    ERROR = 2


class TextureFilter(IntEnum):
    NEAREST = 0
    LINEAR = 1
    NEAR_NEAREST = 2
    LINE_LINEAR = 3
    LINE_NEAREST = 4
    NEAR_LINEAR = 5

class Anisotropy(IntEnum):
    X1 = 0
    X2 = 2
    X4 = 4
    X6 = 6
    X8 = 8
    x16 = 16


class WindowModes(IntEnum):
    DEFAULT = 0
    RESIZABLE = 1
    BORDERLESS = 2
    FULLSCREEN = 3


class VsyncModes(IntEnum):
    BALANCED = -1
    DISABLED = 0
    ENABLED = 1


class RenderModes(IntEnum):
    OPENGL = 0
    VULKAN = 1
    METAL = 2
    DIRECTX = 3


class BuildModes(IntEnum):
    PYINSTALLER = 0
    NUITKA = 1
    

    

class KeyNum(IntEnum):
    # ======================
    # Letters (0 - 25)
    # ======================
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
    I = 8
    J = 9
    K = 10
    L = 11
    M = 12
    N = 13
    O = 14
    P = 15
    Q = 16
    R = 17
    S = 18
    T = 19
    U = 20
    V = 21
    W = 22
    X = 23
    Y = 24
    Z = 25

    # ======================
    # Numbers (top row) (30 - 39)
    # ======================
    NUM_0 = 30
    NUM_1 = 31
    NUM_2 = 32
    NUM_3 = 33
    NUM_4 = 34
    NUM_5 = 35
    NUM_6 = 36
    NUM_7 = 37
    NUM_8 = 38
    NUM_9 = 39

    # ======================
    # Numpad (KP) (40 - 49)
    # ======================
    KP_0 = 40
    KP_1 = 41
    KP_2 = 42
    KP_3 = 43
    KP_4 = 44
    KP_5 = 45
    KP_6 = 46
    KP_7 = 47
    KP_8 = 48
    KP_9 = 49

    KP_PLUS = 50
    KP_MINUS = 51
    KP_MULTIPLY = 52
    KP_DIVIDE = 53
    KP_DOT = 54
    KP_ENTER = 55

    # ======================
    # Movement (60 - 69)
    # ======================
    UP = 60
    DOWN = 61
    LEFT = 62
    RIGHT = 63

    # ======================
    # Controls (70 - 89)
    # ======================
    SPACE = 70
    ENTER = 71
    ESC = 72
    TAB = 73
    CAPS = 74
    BACKSPACE = 75
    DELETE = 76
    INSERT = 77
    HOME = 78
    END = 79
    PAGE_UP = 80
    PAGE_DOWN = 81

    # ======================
    # Modifiers (90 - 99)
    # ======================
    LSHIFT = 90
    RSHIFT = 91
    LCTRL = 92
    RCTRL = 93
    LALT = 94
    RALT = 95

    # ======================
    # Function keys (100 - 111)
    # ======================
    F1 = 100
    F2 = 101
    F3 = 102
    F4 = 103
    F5 = 104
    F6 = 105
    F7 = 106
    F8 = 107
    F9 = 108
    F10 = 109
    F11 = 110
    F12 = 111

    # ======================
    # Special / system (120+)
    # ======================
    PRINTSCREEN = 120
    SCROLLLOCK = 121
    PAUSE = 122

    # punctuation
    GRAVE = 130
    MINUS = 131
    EQUALS = 132
    LBRACKET = 133
    RBRACKET = 134
    BACKSLASH = 135
    SEMICOLON = 136
    APOSTROPHE = 137
    COMMA = 138
    PERIOD = 139
    SLASH = 140



class MouseNum(IntEnum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 3

