#!/usr/bin/env python3

#from ascii_magic import AsciiArt, Front, Back, from_image

#my_art = AsciiArt.from_image(path='../img/moon.png')
#my_art.to_terminal(columns=75, monochrome=True)
#my_art.to_file(columns=75, monochrome=True , path='../out/a.txt')



import gi 

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("test.glade")



class Handler():

    def __init__(self):

        self.button = builder.get_object("button-add")
        self.button.connect('clicked', self.button_add_clicked)

        self.exit = builder.get_object("menu-file-quit")
        self.exit.connect("activate", self.menu_quit_clicked)

    def button_add_clicked(self, button_in):
        # folder chooser here
        dialog = Gtk.FileChooserDialog("Please choose a folder", None,
            #Gtk.FileChooserAction.OPEN,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            #print("uri: "+ dialog.get_uris()[0])
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

        print("Hello Glade")
        print(button_in)

    def menu_quit_clicked(self, button_in):
        print(button_in)
        Gtk.main_quit()

builder.connect_signals(Handler())


window = builder.get_object("corpus-top")

#window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
