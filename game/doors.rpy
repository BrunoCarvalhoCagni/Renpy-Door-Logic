

screen highlight_doors:
    imagemap:
        idle "map_doors.png"
        hover "map_doors.png"
        hotspot (740, 386, 125, 431) action Jump("dialog_door_1") hovered Show("make_door_frames", _xpos= 740, _ypos = 386, _width = 125, _height= 431, _message="Door 1") unhovered Hide("make_door_frames")
        hotspot (863, 385, 125, 436) action Jump("dialog_door_2") hovered Show("make_door_frames", _xpos= 863, _ypos = 385, _width = 125, _height= 436, _message="Door 2") unhovered Hide("make_door_frames")
        hotspot (1000, 410, 128, 411) action Jump("dialog_door_3") hovered Show("make_door_frames", _xpos= 1000, _ypos = 410, _width = 128, _height= 411, _message="Door 3") unhovered Hide("make_door_frames")
        hotspot (1137, 424, 98, 390) action Jump("dialog_door_4") hovered Show("make_door_frames", _xpos= 1137, _ypos = 424, _width = 98, _height= 390, _message="Door 4") unhovered Hide("make_door_frames")


screen make_door_frames(_xpos, _ypos, _width, _height, _message):
    frame:
        area(_xpos, _ypos, _width, _height)
        text _message


