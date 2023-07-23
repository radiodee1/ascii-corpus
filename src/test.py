#!/usr/bin/env python3

#from ascii_magic import AsciiArt, Front, Back, from_image

#my_art = AsciiArt.from_image(path='../img/moon.png')
#my_art.to_terminal(columns=75, monochrome=True)
#my_art.to_file(columns=75, monochrome=True , path='../out/a.txt')



import gi 

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from ascii_magic import AsciiArt, Front, Back, from_image


builder = Gtk.Builder()
builder.add_from_file("test.glade")


class Handler():

    def __init__(self):

        self.source_list = []

        self.text_sources = builder.get_object("text-sources")
        self.text_preview = builder.get_object("text-preview")

        self.button_add = builder.get_object("button-add")
        self.button_add.connect('clicked', self.button_add_clicked)

        self.button_finish = builder.get_object("button-finish")
        self.button_finish.connect('clicked', self.button_finish_clicked)

        self.button_associate = builder.get_object("button-associate")
        self.button_associate.connect('clicked', self.button_associate_clicked)

        self.button_remove = builder.get_object("button-remove")
        self.button_remove.connect('clicked', self.button_remove_clicked)

        self.button_preview = builder.get_object("button-preview")
        self.button_preview.connect('clicked', self.button_preview_clicked)

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
            #print("File selected: " + dialog.get_filename())
            self.source_list.append(dialog.get_filename())
            for i in self.source_list:
                print("File selected: " + str(i))
            self.button_finish_clicked(button_in)
           #print("uri: "+ dialog.get_uris()[0])
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

        print("Hello Glade")
        print(button_in)

    def button_finish_clicked(self, button_in):
        print('clicked '+ str(button_in))
        z = ""
        for i in self.source_list:
            z += i + "\n"
        self.text_sources.get_buffer().set_text(z)

    def button_associate_clicked(self, button_in):
        print('clicked ' + str(button_in))

    def button_remove_clicked(self, button_in):
        print('clicked ' + str(button_in))
        bounds = self.text_sources.get_buffer().get_selection_bounds()
        print('bounds ' + str(bounds))
        if len(bounds) != 0:
            start, end = bounds
            print(start, end)
            line_num = Gtk.TextIter.get_line(start) # gtk_text_iter_get_line( start )
            self.source_list.pop(line_num)
            self.button_finish_clicked(button_in)
            print(line_num)

    def button_preview_clicked(self, button_in):
         # folder chooser here
        dialog = Gtk.FileChooserDialog("Please choose a folder", None,
            Gtk.FileChooserAction.OPEN,
            #Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            #self.source_list.append(dialog.get_filename())
            #for i in self.source_list:
            #    print("File selected: " + str(i))
            #self.button_finish_clicked(button_in)
           #print("uri: "+ dialog.get_uris()[0])

            my_art = AsciiArt.from_image(path= dialog.get_filename())
            #my_art.to_terminal(columns=75, monochrome=True)
            sample = my_art.to_ascii(columns=75, monochrome=True )
            self.text_preview.get_buffer().set_text(sample)


        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

        pass

    def menu_quit_clicked(self, button_in):
        print(button_in)
        Gtk.main_quit()

builder.connect_signals(Handler())


window = builder.get_object("corpus-top")

#window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
