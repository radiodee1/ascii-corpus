# ascii-corpus GUI 
Ascii images of dots for fine-tuning corpus of large language models.

- Install the necessary packages on your system. There are pip and also apt requirements. I am using Ubuntu 23.10.
- Make a folder for your output. I have a folder in my `/home/` folder called `/home/<user>/workspace/`. Do not put the output folder in the project/git folder.
- Launch the gui by navigating to the `src` directory and typing `python3 test.py`.
- STEP 1: build the csv file that specifies the output. Go to the 'compose dots' tab in the app. Click the 'compose-csv' button.
  - Enter a location and name for the 'csv file location'. You must enter a name here as well as a folder destination. Use the file folder you created above.
  - Enter a location for the developed png files. This is just a folder. Use the file folder you created above.
  - Click the 'list size' button until you have a group that is sufficiently large for your training. The highest value is 1,000 but you can run the gui several times to come up with the number you like.
  - Click the 'profile' button to change the profile. You will probably want this to read '0-9'. This is the most sensible setting.
- STEP 2: build the png files that will be transformed into the output. This process uses the csv file.
  - Make sure you are still looking at the 'compose dots' tab. To process all the png files, press 'auto-png-editor'. You will be asked to specify the csv file you generated above. Once the file has been specified, click the button again. If you want to generate one png at a time, press 'png-editor'.
  - Because there is an upper limit of 1,000 files, you may want to create additional folders at this time with more randomly generated png files in them. I typically used three folders in this setup to total 3,000 training examples.
- STEP 3: arrange the folders that will be needed for the output. These are the png file folders.
  - Go to the 'sources' tab. Click the 'add source' button and use the dialog to add your png folder. Repeat clicking the 'add source' button for all the folders you have.
  - You may want to change the association of the output text file by clicking the 'associate' button. Initially it is set for 'train', and this is good for most people. Some may switch the 'associate' to 'test' or 'validate'. Click the 'finish' button.
- STEP 4: generate the output text files.
  - Go to the 'output' tab.
  - Click either the 'write-text' or the 'write-json' button, depending on your needs. A file dialog will open.
  - Pick the folder for the output as well as a name for the resulting file.
  - You can click on the 'prompt edit txt' or the 'prompt edit json' button depending on which type of file you are using before you use the 'write' option above.

# Counting and Logic python script

- cd into the `src` directory.
- run `./one-line.py --help`

```
usage: one-line.py [-h] [--name NAME] [--verbose] [--lines LINES] [--prompt]
                   [--integers INTEGERS] [--large_string] [--foreground FOREGROUND]
                   [--background BACKGROUND] [--example EXAMPLE]

One Line

options:
  -h, --help            show this help message and exit
  --name NAME           name and path for "construct" output file. (default:
                        ./../../one-line-dots)
  --verbose             print verbose output. (default: False)
  --lines LINES         number of examples. (default: 100)
  --prompt              output prompt files. (default: False)
  --integers INTEGERS   highest integers to represent as dots. (default: 10)
  --large_string        use large string for containing dots. (default: False)
  --foreground FOREGROUND
                        set foreground character for large_string. (default: O)
  --background BACKGROUND
                        set background character for large_string. (default: .)
  --example EXAMPLE     designate an example to include in prompt output. (default:
                        -1)
```
- Individual experimentation is necessary for good results, but the following code is a good starting spot.

```
./one-line.py --prompt --lines 10 --example 3 

## or ## 

./one-line.py --prompt --lines 10 --large_string --example 3 
```

- `--prompt` tells the script to generate single examples that do not have the final integer specified. There is a blank spot for the result.
- `--lines 10` tells the script to generate 10 files.
- `--example` tells the script to include an example in the prompt. This aids the model in picking a answer.
- `--large_string` tells the script to format the output differently. 

## Not Implemented
using MNIST images for ascii fine-tuning corpus for large language models.
