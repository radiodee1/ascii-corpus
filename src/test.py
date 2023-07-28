#!/usr/bin/env python3

#from ascii_magic import AsciiArt, Front, Back, from_image

#my_art = AsciiArt.from_image(path='../img/moon.png')
#my_art.to_terminal(columns=75, monochrome=True)
#my_art.to_file(columns=75, monochrome=True , path='../out/a.txt')



import gi 

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from ascii_magic import AsciiArt, Front, Back, from_image
import glob
import os
import random
import json 

builder = Gtk.Builder()
builder.add_from_file("test.glade")



prompt_1 = { 
'label' : "three-lines",

'text': """

### Image: 
{}
### Question:
{}
### Answer:
{}
"""
}

prompt_2 = {
'label' : "two-lines",

'text' : """

### Question:
{}
### Answer:
{}
"""
}


json_prompt_1 = {
        'label' : 'json-three-lines',
        'text' : {
            'image': '{}',
            'question': '{}',
            'answer': '{}'
            }
        }

json_prompt_2 = {
        'label': 'json-two-lines',
        'text' : {
            'question': "{}",
            'answer': "{}"
            }
        }

class Handler():

    def __init__(self):

        self.source_list = []
        self.preview_url = ""
        self.insert_spaces = True
        #self.corpus = ""
        self.corpus_count = 0

        self.width = 40
        
        self.prompt_list = [prompt_1, prompt_2] ## not used yet...
        self.prompt_list_number = 0 
        self.prompt = self.prompt_list[self.prompt_list_number]['text']

        self.json_prompt_list = [ json_prompt_1, json_prompt_2 ]
        self.json_prompt_list_number = 0 
        self.json_prompt = self.json_prompt_list[self.json_prompt_list_number]['text']

        self.associate_list = ['train', 'test', 'validate']
        self.associate_list_number = 0
        self.associate = self.associate_list[self.associate_list_number]

        self.associate_count = { x:0 for x in self.associate_list }
        self.corpus = { x:"" for x in self.associate_list }
        self.corpus_json = {x: [] for x in self.associate_list}


        self.dots_csv_location = ""
        self.dots_png_location = ""
        self.dots_sizes = [5, 50, 100, 1000]
        self.dots_types = ["0-9", "0-4", "5-9"]
        self.dots_sizes_number = 0 
        self.dots_types_number = 0 

        self.mechanical_generate_file = ""
        self.mechanical_generate_file_number = 0
        self.mechanical_lines = []
        self.mechanical_numbers = []

        self.global_question = "How many dots are there?"
        self.global_answer = "There are"

        self.text_sources = builder.get_object("text-sources")
        self.text_preview = builder.get_object("text-preview")
        self.label_status = builder.get_object("label-status")
        self.label_mix = builder.get_object("label-mix")
        self.label_csv_1 = builder.get_object("label-csv-1")
        self.label_csv_2 = builder.get_object("label-csv-2")

        self.button_add = builder.get_object("button-add")
        self.button_add.connect('clicked', self.button_add_clicked)

        self.button_finish = builder.get_object("button-finish")
        self.button_finish.connect('clicked', self.button_finish_clicked)

        self.button_associate = builder.get_object("button-associate")
        self.button_associate.connect('clicked', self.button_associate_clicked)
        self.button_associate.set_label('associate : ' + self.associate)

        self.button_remove = builder.get_object("button-remove")
        self.button_remove.connect('clicked', self.button_remove_clicked)

        self.button_preview = builder.get_object("button-preview")
        self.button_preview.connect('clicked', self.button_preview_clicked)

        self.button_show = builder.get_object("button-show")
        self.button_show.connect('clicked', self.button_show_clicked)

        self.button_write = builder.get_object("button-write")
        self.button_write.connect('clicked', self.button_write_clicked)

        self.button_write_json = builder.get_object("button-write-json")
        self.button_write_json.connect('clicked', self.button_write_json_clicked)

        self.button_spaces = builder.get_object("button-spaces")
        self.button_spaces.connect('clicked', self.button_spaces_clicked)

        self.button_prompt_edit = builder.get_object("button-prompt-edit")
        self.button_prompt_edit.connect('clicked', self.button_prompt_edit_clicked)

        self.button_compose_go = builder.get_object("button-compose-go")
        self.button_compose_go.connect('clicked', self.button_compose_go_clicked)

        self.button_compose_csv = builder.get_object("button-compose-csv")
        self.button_compose_csv.connect('clicked', self.button_compose_csv_clicked)

        self.dots_csv_cancel = builder.get_object("button-compose-csv-cancel")
        self.dots_csv_cancel.connect('clicked', self.dots_csv_cancel_clicked)

        self.dots_csv_save = builder.get_object("button-compose-csv-save")
        self.dots_csv_save.connect('clicked', self.dots_csv_save_clicked)

        self.dots_csv_location_button = builder.get_object("csv-location")
        self.dots_csv_location_button.connect('clicked', self.dots_csv_location_button_clicked)

        self.dots_csv_png_button = builder.get_object("csv-png")
        self.dots_csv_png_button.connect('clicked', self.dots_csv_png_button_clicked)

        self.dots_csv_size_button = builder.get_object("csv-size")
        self.dots_csv_size_button.connect('clicked', self.dots_csv_size_button_clicked)

        self.dots_csv_type_button = builder.get_object("csv-type")
        self.dots_csv_type_button.connect('clicked', self.dots_csv_type_button_clicked)

        self.exit = builder.get_object("menu-file-quit")
        self.exit.connect("activate", self.menu_quit_clicked)

        self.compose_dots = builder.get_object('csv-top')

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
            self.source_list.append(self.associate + ":" + dialog.get_filename())
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
        self.associate_list_number += 1 
        if self.associate_list_number >= len(self.associate_list):
            self.associate_list_number = 0 
        self.associate = self.associate_list[self.associate_list_number]
        self.button_associate.set_label('associate : ' + self.associate)
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
        dialog = Gtk.FileChooserDialog("Please choose a file", None,
            Gtk.FileChooserAction.OPEN,
            #Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked "+ str(button_in))
            print("File selected: " + dialog.get_filename())
            my_art = AsciiArt.from_image(path= dialog.get_filename())
            #my_art.to_terminal(columns=75, monochrome=True)
            sample = my_art.to_ascii(columns=self.width, monochrome=True )

            sample = self.prep_sample_for_tokenizer(sample)
            
            sample_out = self.substitute_in_prompt(sample, 'How many dots are there', 'there are two')

            self.text_preview.get_buffer().set_text(sample_out)
            self.preview_url = dialog.get_filename()

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()
        pass

    def button_show_clicked(self, button_in):
        if self.preview_url != "":
            print("Open clicked " + str(button_in))
            
            my_art = AsciiArt.from_image(path=self.preview_url)
            #my_art.to_terminal(columns=75, monochrome=True)
            sample = my_art.to_ascii(columns=self.width, monochrome=True )

            sample = self.prep_sample_for_tokenizer(sample)
            
            sample_out = self.substitute_in_prompt(sample, self.global_question, 'there are two')
            self.text_preview.get_buffer().set_text(sample_out)
        pass

    def button_write_clicked(self, button_in):
        self.corpus_count = 0
        start, end = self.text_sources.get_buffer().get_bounds()
        self.glob_from_text_list(self.text_sources.get_buffer().get_text(start, end, True))
        self.label_status_set()
        print(button_in)
        pass

    def button_write_json_clicked(self, button_in):
        self.corpus_count = 0 
        start, end = self.text_sources.get_buffer().get_bounds()
        self.glob_from_text_list(self.text_sources.get_buffer().get_text(start, end, True), use_json=True)
        self.label_status_set()
        print(button_in)

    def button_spaces_clicked(self, button_in):
        self.insert_spaces = not self.insert_spaces
        self.label_status_set()
        print(button_in)

    def button_prompt_edit_clicked(self, button_in):
        self.prompt_list_number += 1 
        if self.prompt_list_number >= len(self.prompt_list):
            self.prompt_list_number = 0         
        self.prompt = self.prompt_list[self.prompt_list_number]['text'] 
        self.label_status_set()
        print(button_in)

    def button_compose_go_clicked(self, button_in):
        if self.mechanical_generate_file.strip() == "" and len(self.mechanical_lines) == 0:
         # folder chooser here
            dialog = Gtk.FileChooserDialog("Please choose a file", None,
                Gtk.FileChooserAction.OPEN,
                #Gtk.FileChooserAction.SELECT_FOLDER,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                self.mechanical_generate_file = dialog.get_filename()

            elif response == Gtk.ResponseType.CANCEL:
                print("Cancel clicked")
            dialog.destroy()
            self.mechanical_generate_file_number = 0 
            return

        if self.mechanical_generate_file_number == 0 and len(self.mechanical_lines) == 0:
            f = open(self.mechanical_generate_file, 'r')
            #self.mechanical_lines = f.readlines()
            lines = f.readlines()
            for i in lines:
                if len(i.split(',')) < 2:
                    f.close()
                    return
                self.mechanical_lines.append(i.split(',')[0])
                self.mechanical_numbers.append(int(i.split(',')[1]))
            f.close()

        #self.mechanical_generate_file_number += 1 
        num = 0
        png_name = ""

        if self.mechanical_generate_file_number >= len(self.mechanical_lines) :
            return

        png_name = self.mechanical_lines[self.mechanical_generate_file_number] 
        num = self.mechanical_numbers[self.mechanical_generate_file_number] 
        self.mechanical_numbers[self.mechanical_generate_file_number] = 1 
        
        while num == 1 and self.mechanical_generate_file_number < len(self.mechanical_lines):
            png_name = self.mechanical_lines[self.mechanical_generate_file_number] 
            num = self.mechanical_numbers[self.mechanical_generate_file_number] 
            #self.mechanical_numbers[self.mechanical_generate_file_number] = 1 
            #count += 1 
            self.mechanical_generate_file_number += 1 
            
        if self.mechanical_generate_file_number >= len(self.mechanical_lines):
            return

        if len(png_name.strip()) == 0:
            self.mechanical_generate_file_number += 1 
            return 
         
        name = png_name
        if png_name.strip().endswith(".png"):
            os.system("python3 compose.py " + name)

        #self.mechanical_generate_file_number += 1  ## sneaky??
        print(button_in)
        print(self.mechanical_generate_file_number, 'number from csv file.')
        pass

    def button_compose_csv_clicked(self, button_in):
        #self.compose_dots.show_all()
        self.compose_dots = builder.get_object('csv-top')
        self.compose_dots.show_all()
        self.label_csv_2_set()
        self.label_csv_1_set()
        print(button_in)
        pass

    ### submenu csv dots start here ###
    def dots_csv_cancel_clicked(self, button_in):
        self.compose_dots.hide()
        print(button_in)

    def dots_csv_save_clicked(self, button_in):
        print(button_in)
        self.prep_csv_for_dots()
        self.compose_dots.hide()

    def dots_csv_location_button_clicked(self, button_in):
        name = "../../"

        dialog = Gtk.FileChooserDialog("Please choose a name", None,
            Gtk.FileChooserAction.SAVE,
            #Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            #print("Open clicked "+ str(button_in))
            print("File selected: " + dialog.get_filename())
            name = dialog.get_filename() #+ "."
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

        self.dots_csv_location = name
        self.label_csv_1_set()
        print(button_in)

    def dots_csv_png_button_clicked(self, button_in):
        dialog = Gtk.FileChooserDialog("Please choose a folder", None,
            #Gtk.FileChooserAction.OPEN,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            #print("File selected: " + dialog.get_filename())
            #self.source_list.append(self.associate + ":" + dialog.get_filename())
            self.dots_png_location = dialog.get_filename()
            for i in self.source_list:
                print("File selected: " + str(i))
            self.button_finish_clicked(button_in)
           #print("uri: "+ dialog.get_uris()[0])
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        self.label_csv_2_set()
        dialog.destroy()
        print(button_in)

    def dots_csv_size_button_clicked(self, button_in):
        self.dots_sizes_number += 1 
        if self.dots_sizes_number >= len(self.dots_sizes):
            self.dots_sizes_number = 0 
        print(button_in)
        self.label_csv_1_set()
        pass

    def dots_csv_type_button_clicked(self, button_in):
        self.dots_types_number += 1 
        if self.dots_types_number >= len(self.dots_types):
            self.dots_types_number = 0 
        print(button_in)
        self.label_csv_2_set()

    def label_csv_2_set(self):
        content = ""
        content += self.dots_types[self.dots_types_number] + ' | '
        content += self.dots_png_location.split("/")[-1]
        self.label_csv_2.set_text(content)
        pass

    def label_csv_1_set(self):
        content = ""
        #content += str(self.mechanical_generate_file_number) + "/"
        content += str(self.dots_sizes[self.dots_sizes_number]) + ' | '
        content += self.dots_csv_location.split("/")[-1]
        self.label_csv_1.set_text(content)
        pass
    ### submenu csv dots end here ###


    def menu_quit_clicked(self, button_in):
        print(button_in)
        if self.mechanical_generate_file_number < len(self.mechanical_lines) - 1 and self.mechanical_generate_file_number >= 0:
            self.mechanical_numbers[self.mechanical_generate_file_number - 1] = 1 
            f = open(self.mechanical_generate_file + '.incomplete.csv', 'w')
            for i in range(len(self.mechanical_lines)):
                f.write(self.mechanical_lines[i] + ',' + str(self.mechanical_numbers[i]) + '\n')
                pass
            f.close()
        print(self.associate_count)
        Gtk.main_quit()

    def substitute_in_prompt(self, image, question, answer):
        if question == None or len(question) == 0:
            return self.prompt.format(str(image), str(answer))
        return self.prompt.format(str(image), str(question), str(answer))

    def substitute_in_prompt_json(self, image, question, answer):
        if question == None or len(question) == 0:
            x = self.json_prompt.copy()
            x['image'] = image
            x['answer'] = answer
            #print(x)
            return x 
        x = self.json_prompt.copy()
        x['image'] = image
        x['question'] = question
        x['answer'] = answer
        #print(x)
        return x 

    def label_status_set(self):
        label = ""
        label += 'prompt:' + self.prompt_list[self.prompt_list_number]['label']
        label += ' | '
        label += 'spacing:' + str(self.insert_spaces)
        #label += ' | '
        #label += 'count:' + str(self.corpus_count)
        self.label_status.set_text(label)
        self.label_mix_set()
        pass

    def label_mix_set(self):
        label = ""
        label += 'count:' + str(self.associate_count)
        self.label_mix.set_text(label)

    def glob_from_text_list(self, t, use_json=False):
        if use_json:
            self.corpus_json = {x:[] for x in self.associate_list}
        else:
            self.corpus = { x:"" for x in self.associate_list }


        name = "../../"

        dialog = Gtk.FileChooserDialog("Please choose a name", None,
            Gtk.FileChooserAction.SAVE,
            #Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            #print("Open clicked "+ str(button_in))
            print("File selected: " + dialog.get_filename())
            name = dialog.get_filename() + "."
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

        for i in t.split('\n'):
            #print("=" + i + "=")
            if len(i.split(":")) > 1:
                assoc = i.split(':')[0]
                #print("+" + assoc + "+")
                folder = i.split(':')[1]
                #print(i, assoc, folder)
                for j in self.associate_list:
                    if j == assoc:
                        #filetype = '.txt'
                        #if use_json:
                        #    filetype = '.json'
                        #self.corpus[assoc] = ""
                        #f = open( name + assoc + filetype, 'w')
                        li = []
                        li += glob.glob(folder + '/*.png')
                        li += glob.glob(folder + '/*.jpg')
                        li += glob.glob(folder + '/*.jpeg')
                        print(li)
                        for k in li:
                            print(k)
                            local_answer = "two."
                            if len(k.split('.')) > 2:
                                local_answer = k.split('.')[-2]
                                local_answer = ' '.join(local_answer.split('_')) + '.'
                            my_art = AsciiArt.from_image(path=k)
                            sample = my_art.to_ascii(columns=self.width, monochrome=True )
                            sample = self.prep_sample_for_tokenizer(sample)
                            
                            if use_json:
                                sample_out = self.substitute_in_prompt_json( sample, self.global_question, self.global_answer + ' ' + local_answer )
                                self.corpus_json[assoc].append(sample_out)
                            else:
                                sample_out = self.substitute_in_prompt(sample, self.global_question, self.global_answer + ' ' + local_answer)
                                self.corpus[assoc] += sample_out

                            self.corpus_count += 1
                        self.associate_count[assoc] = self.corpus_count

                        if not use_json:
                            filetype = '.txt'
                            f = open( name + assoc + filetype, 'w')
                        
                            f.write(self.corpus[assoc])
                            f.close()

                        else:
                            filetype = ".json"
                            print(self.corpus_json)
                            f = open( name + assoc + filetype, 'w' )
                            f.write(json.dumps(self.corpus_json[assoc]))
                            f.close()

        self.corpus_json = { x:[] for x in self.associate_list }
        self.corpus = { x:"" for x in self.associate_list }
        self.label_mix_set()

    def prep_sample_for_tokenizer(self, sample):
        sample_out = ""
        for i in sample.split("\n"):
            for j in i:
                if j == " ":
                    j = '.'
                if j in ['"', "'"]:
                    j = '.'
                if self.insert_spaces:
                    sample_out += j + ' '
                else:
                    sample_out += j 
            sample_out += '\n'
        return sample_out

    def prep_csv_for_dots(self):
        if self.dots_csv_location.strip() == "" or self.dots_png_location.strip() == "":
            return
        lines = []
        list_done = 0 
        options = []
        shuffle_list = []
        while list_done < self.dots_sizes[self.dots_sizes_number]:
            if len(shuffle_list) == 0:
                type_in = self.dots_types[self.dots_types_number]
                start = int(type_in.split('-')[0])
                end = int(type_in.split('-')[1]) + 1

                options = [x for x in range(start, end)]
                shuffle_list = random.sample(options, len(options))
                print(shuffle_list)
                pass
            if len(shuffle_list) > 0:
                label = shuffle_list.pop(0)
                label_string = self.dots_png_location + "/file_dots_" + str(list_done) + "." + str(label) + ".png"
                lines.append(label_string)
            list_done += 1 
        #print(lines)
        if not self.dots_csv_location.endswith('.csv'):
            self.dots_csv_location += '.csv'
        f = open(self.dots_csv_location, 'w')
        for i in lines:
            f.write(i + ',0\n')
        f.close()
        pass
        

builder.connect_signals(Handler())


window = builder.get_object("corpus-top")

#window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
