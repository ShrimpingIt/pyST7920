from bitFont import BitFont
font = BitFont(
	fontHeight = 17,
	pixBytes = bytearray(b'\x00\x10\xc0o\x00@\x80\x04\x00\x07\x00\x00\x00$\x008\x00\x808\x00\x1f\x80#\x00\xc4\x01\xf8\x00\x1c\x01`\x06 \x11@$\xc0\xff\x00\x91\x00\xc4\x00\x0c\x03$\x01\xc8\x07\xe0\x12\x80$\xc00\x00p\x00\x16\x012\x02\xa4\x020\x06\x00\x13\x90\x00\xe0\x00\x00>\x00\x83\x01\x01\x04\x02\x08\x18\x0c\xc0\x07\x80\x08\x00\n\x00\x7f\x00(\x00\x88\x00@\x00\x80\x00\xe0\x0f\x00\x02\x00\x04\x00@\x02\x80\x03 \x00@\x00\x80\x00\x00\x01\x00\x02\x00`\x00\xc0\x00\x80\x01\xc0\x00@\x00`\x000\x00\x80\x0f\x80 \x80\x80\x00\x01\x01\x04\x01\xf0\x01 \x08 \x10\xe0?\x00@\x00\x80\x00\x86\x01\x82\x02\x84\x04\x88\x08\x10\x11\xc0!\x801\x80\x80\x00\x11\x01"\x02D\x04p\x07\x00\x06\x00\n\x00\x13\x00!\x00\xff\x01\x80\x00<\x02H\x08\x90\x10 !@B\x80x\x00\xfe\x00"\x02D\x04\x88\x08\x10\x11@\x1c@\x00\x80\x00\x00\xc1\x01b\x004\x00\x18\x00\xe0\x0e "@D\x80\x88\x00\x11\x01\xdc\x018\x03\x88\x08\x10\x11 "@D\x00\x7f\x00\x8c\x01\x18\x030\x12`\x1c\x00\x02\x00\n\x00"\x00\x82\x00H\x00\x90\x00 \x01@\x02\x80\x04\x80 \x00"\x00(\x00 \x00\x0c\x00\x04\x00\x08\x00\x10\x1b \x01\x80\x01\x00>\x00\x82\x00r\x02\x14\x05(\n\xe0\x17\x80?\x80\x04\x80\x08\x00\x11\x00$\x00\xf0\x07\x08\x08\xf0\x1f "@D\x80\x88\x00\xee\x00\xfc\x01\x04\x04\x08\x08\x10\x10  \x801\x80\x80\x00\xff\x01\x02\x02\x04\x04\x08\x08\xe0\x0f\xe0?@D\x80\x88\x00\x11\x01"\x02\x04\x04\xf8\x0f\x10\x01 \x02@\x04\x80\x08\x00\x01\x00\xfc\x01\x04\x04\x08\x08\x10\x11 \x12\x80|\x80\xff\x00\x10\x00 \x00@\x00\x80\x00\xf0\x1f  @@\x80\xff\x00\x01\x01\x02\x02\x00\x03\x00\x08\x00\x10  \xc0?\x80\x00\x00\xff\x01 \x00\xa0\x00 \x02 \x08  \xc0\x7f\x00\x80\x00\x00\x01\x00\x02\x00\x04\x00\x08\xf0\x1f\xc0\x00\x00\x06\x00\x0c\x00\x06\x00\xfe\x03\xfc\x07\x18\x00\xc0\x00\x00\x06\x000\x80\xff\x00\xfe\x00\x02\x02\x04\x04\x08\x08\x10\x10\xc0\x1f\xc0\x7f\x80\x08\x00\x11\x00"\x00D\x00p\x00\xe0\x0f $@H\x80\xa0\x00\x81\x03\xfc\t\xfc\x07\x88\x00\x10\x01 \x06@\x14\x00\xc7\x00\xc6\x00\x12\x02$\x04\x88\x08\x10\x11@\x1c@\x00\x80\x00\x00\x01\x00\xfe\x03\x04\x00\x08\x00\x10\x00\xe0\x1f\x00@\x00\x80\x00\x00\x01\x00\x02\xfc\x038\x00\x80\x03\x008\x00p\x00\x1c\x00\x07\x00\xfe\x03\x00\x03\x80\x01\x00\x03\x00\x18\xc0\x7f\x80\xc1\x00l\x00 \x00@\x00`\x030\x18\xe0\x01\x00\x04\x00\xf0\x00\x10\x00\x1e\x00\x04\x07\x08\t\x10\x11 !@A\x80\x81\x80\xff\x03\x01\x04\x02\x08\x18\x00\xc0\x00\x00\x02\x00\x18\x00\xc0\x80\x00\x02\x01\x04\xfe\x0f\x08\x00\x08\x00\x08\x00\x10\x00@\x00\x00\x01\x00\x00\x04\x00\x08\x00\x10\x00 \x00@\x00\x80\x00\x00\x81\x03\x00\t\x00 \x03 \t@\x12\x80"\x00%\x00\xfc\x00\xff\x01\x10\x01\x10\x04 \x08@\x10\x00\x1f\x00>\x00\x82\x00\x04\x01\x08\x02\x10\x04@\x04\x80\x0f\x80 \x00A\x00\x82\x00\x88\x00\xfe\x03\xe0\x03 \t@\x12\x80$\x00I\x00\\\x00\x08\x00\x10\x00\xf8\x07H\x00\x90\x00\x00g\x001\x01\xa2\x02D\x05p\n\x10\x08\xf8\x0f\x80\x00\x80\x00\x00\x01\x00\x02\x00\xf8\x01\x00\x02\x10\x04\xec\x0f\x00\x10\x00 \x00\xc0\x00\x00\x02\x00\x04\x08\x08\xf6\x0f\xf8\x0f\x00\x02\x00\n\x00"\x00\x82\x00\x00\x01\x02\x02\xfc\x07\x00\x08\x00\x10\x80?\x00\x01\x00|\x00\x04\x00\xf0\x03\xf0\x07@\x00@\x00\x80\x00\x00\x01\x00\xfc\x00\xf8\x00\x08\x02\x10\x04 \x08@\x10\x00\x1f\x00\xff\x01D\x00\x04\x01\x08\x02\x10\x04\xc0\x07\x80\x0f\x80 \x00A\x00\x82\x00\x88\x00\xf8\x0f\xf0\x07@\x00@\x00\x80\x00\x00\x01\x00\x0c\x00\x98\x00H\x02\x90\x04 \t@\x12\x00\x19\x00\x01\x00\x02\x00\xff\x00\x08\x02\x10\x04\x00\x04\xc0\x0f\x00 \x00@\x00\x80\x00\x80\x00\xf8\x03p\x00\x00\x03\x00\x18\x00\x0c\x00\x07\x00~\x00\x00\x01\xf0\x01\x00\x04\xe0\x07\xc0\x18\x00\n\x00\x08\x00(\x00\x8c\x01\xf8\x00\x00\x12\x00$\x00H\x00\x88\x00\xff\x00\xc2\x00D\x01H\x02P\x04`\x08@\x10`2 \x9b@\x00\xc1\xff\x07\x01\x04\xb2\t\x98\x0c \x00 \x00@\x00\x00\x01\x00\x02\x00\x02'),
	endCols = [3, 8, 14, 20, 26, 32, 34, 37, 40, 45, 50, 52, 57, 59, 64, 70, 75, 81, 87, 93, 99, 105, 111, 117, 123, 125, 127, 131, 136, 140, 146, 152, 158, 164, 170, 176, 182, 188, 194, 200, 205, 211, 217, 223, 229, 235, 241, 247, 253, 259, 265, 272, 278, 284, 290, 296, 301, 307, 310, 315, 318, 324, 331, 333, 339, 345, 351, 357, 363, 368, 374, 380, 385, 390, 395, 400, 405, 411, 417, 423, 429, 435, 441, 447, 453, 458, 463, 468, 474, 480, 483, 484, 487, 493]
)