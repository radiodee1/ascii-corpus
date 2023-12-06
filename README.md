# ascii-corpus
ascii images for fine-tuning corpus of large language models.

- Install the necessary packages on your system. There are pip and also apt requirements. I am using Ubuntu 23.10.
- Make a folder for your output. I have a folder in my `/home/` folder called `/home/<user>/workspace/`. Do not put the output folder in the project/git folder.
- Launch the gui by navigating to the `src` directory and typing `python3 test.py.`
- STEP 1: build the csv file that specifies the output. Go to the 'compose dots' tab in the app. Click the 'compose-csv' button.
  - Enter a location and name for the 'csv file location'. You must enter a name here as well as a folder destination. Use the file folder you created above.
  - Enter a location for the developed png files. This is just a folder. Use the file folder you created above.
  - Click the 'list size' button until you have a group that is sufficiently large for your training. The highest value is 1,000 but you can run the gui several times to come up with the number you like.
  - Click the 'profile' button to change the profile. You will probably want this to read '0-9'. This is the most sensible setting.
- STEP 2: build the png files that will be transformed into the output. This process uses the csv file.
  - Make sure you are still looking at the 'compose dots' tab. To process all the png files, press 'auto-png-editor'. You will be asked to specify the csv file you generated above. Once the file has been specified, click the button again. If you want to generate one png at a time, press 'png-editor'.
- STEP 3: arrange the folders that will be needed for the output. These are the png file folders.
- STEP 4: generate the output text files.

## Not Implemented
using MNIST images for ascii fine-tuning corpus for large language models.
