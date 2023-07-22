#!/usr/bin/env python3

from ascii_magic import AsciiArt, Front, Back, from_image
#from colorama import Back, Front


#AsciiArt.quick_test()

my_art = AsciiArt.from_image(path='../img/moon.png')
my_art.to_terminal(columns=75, monochrome=True)
my_art.to_file(columns=75, monochrome=True , path='../out/a.txt')
