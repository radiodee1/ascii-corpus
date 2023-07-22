#!/usr/bin/env python3

from ascii_magic import AsciiArt
from colorama import Back


#AsciiArt.quick_test()

my_art = AsciiArt.from_image(path='../img/moon.jpg')
my_art.to_terminal(columns=25, back=Back.BLACK)
my_art.to_file(columns=75, path='../out/a.txt')
