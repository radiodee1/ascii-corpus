#!/usr/bin/env python3

#from ascii_magic import AsciiArt, Front, Back, from_image

#my_art = AsciiArt.from_image(path='../img/moon.png')
#my_art.to_terminal(columns=75, monochrome=True)
#my_art.to_file(columns=75, monochrome=True , path='../out/a.txt')



import gi 

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Handler:
	def button_add_clicked(self, button):
	    print("Hello GeeksForGeeks using Glade")

builder = Gtk.Builder()
builder.add_from_file("test.glade")
builder.connect_signals(Handler())

#ournewbutton = builder.get_object("button1")
#ournewbutton.set_label("Demo using Glade!")

window = builder.get_object("corpus-top")

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
