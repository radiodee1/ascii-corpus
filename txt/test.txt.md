# Counting and Logical Ability 

```
https://github.com/oobabooga/text-generation-webui.git 
```

I was using oobabooga's llm launching web site. I started at home, but quickly moved to a hosted solution. I was using runpod and a gpu that could handle 24GB of GPU-V ram. I was using LLama 2, I believe the 13B version, and I was using LoRA. My goal was to represent simple png images as ascii art, and then show them to the llm and have the llm identify them. I wanted to do fine tuning to learn a task involving the ascii art I just mentioned.

```
https://www.runpod.io/
```

Additionally, my images were all of a similar variety. They all contained collections of dots. It seemed to me that llm's could count, or seem to count, but that that ability might be derived from the symbol of the number in question, not the real number itself. An llm might not truly know that a symbol like a number, written in a text file, also had the meaning of a true number. The purpose of the images was to have the llm count the few dots in the image. Llm's may have the ability to count, but they may not. It seemed to me to be an interesting experement to see if I could get the model to count small integers from simple png files.

```
https://huggingface.co/TheBloke/Llama-2-13B-Chat-fp16
```

There is, or there appears to be a functionality in oobabooga to include images in individual queries. This method would be far superior because it uses the image in a query but does not use ascii art. The unfortunate part of this is that when you are doing training the functionality in question is not available. In other words, you can use an image during a query, but not during training. I think this is the case.

```text
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . M N M . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . T \ L . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . @ O @ . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . D K W . . . . . . . $ 4 G . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . ! + p . . . . . . . g v t . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . D K N . . . . . . . . . . . |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |

```

I am a linux user, so in python I made a gtk 3 gui that I could use for generating a training set. My training sets generally had 3,000 examples. I had the program generate png images randomly that contained a number of black splotches or dots. The number of dots varied randomly from 0 to 9. Then I had my code take a version of the png and convert it to ascii art and include it in the various training question/answer pairs. A training run took between 1 and 3 hours.

```text
[gui screenshot]
```

There were several serious challenges to this methodology. One of the main challenges has to do with the llm concept itself. Before an llm processes a piece of text it needs to be tokenized. Tokens sometimes take several symbols and combine them to make one unit. Pictures like png's or jpeg's need to represent visual data as pixels, spots or dots that have different intensities. These dots also need to be evenly spaced. Also, the tokenization task is not clearly visible to the human user. What this means is that lines of ascii art can be converted to tokens that do not really reflect the nature of the original pixels. And even further, one line in an ascii art example could be tokenized to some data that is not the same length as a previous line might be tokenized. The concept of space or distance in the horizontal direction in an image is lost during the tokenization.

Vertical distance is lost too, as the lines, once tokenized, are treated separately by the model. This vertical challenge is what is being challenged typically in the training.

There are other problems as well. The fine-tuning process does not automatically take into acount that ascii art input is large, symbol wise, during training. The window needs to be large enought to evaluate a complete ascii example with each question/answer pair. The larger this window, the longer training takes. This is also related to the fact that I'm using LoRA for my fine-tuning. The R in LoRA stands for Rank, and this rank is the window I referred to above.

If the model understood the task, it could easily approach the problem by counting the times in the overall image where the information deviates from the normal. In other words, if it knew the size of the image and the token for the background it could count the number of tokens that deviated from the background, and it would have an approximation of the answer. This could be a good start. The problem would be, in that case, that there are some splotches that traverse several lines. Still, any outcome like this would have been welcomed. This was never achieved.

It would be pretty encouraging if the model even did this, if it came up with some number, but it didn't. This does not mean that the model has a misrepresented view of small integers. It just means that it cannot understand png files in ascii art form. It's probably safe to assume that the model cannot understand anything in ascii art form. Further more, the model cannot be trained using LoRA to do this understanding.

LoRA stands for 'Low Rank Adaptation'. From my limited understanding, a Large Language Model is modified by placing a low rank matrix between every two layers in the model. By Rank, here we mean size. It may be that with LLama 2 and the standard LoRA implementation, the task I'm looking to perform cannot be achieved. For this reason we modify the task and try again. In the following text we describe a second experement that could be more successfull.

Now we fast forward to the present.

Here we will attempt, for at least one experement, to remove ascii art from the training and prompting. We will define a string of characters that has a number of countable symbols in it. We ask the LLM to count the symbols before and after the LoRA training. Hopefully the model will get it right. If the model gets it right before the training then we are done.

Results:

The same model was loaded as before. No training is being done. We have four sets of prompts and we use them all. Each of the four uses slightly different wording, but 10 possible answers, the integers between 0 and 9. The first set looks like this, and should be answered with the number 3:

```text
### Instruction:
How many O symbols are inside these brackets?
### Input:
[O,O,O]
### Output:
```

The answer should be 3. Just for completeness, here is another in the same set.

```text
### Instruction:
How many O symbols are inside these brackets?
### Input:
[O,O,O,O,O]
### Output:
```

For this one, the answer should be 5. We call this the single example small prompt. With these we achieved correct answers for 1 through 4. In other words the model got 0 wrong and it got 5 through 9 wrong. The next series would be called the double example small prompt. What we are doing here is offering the model two examples and asking it to fill in the integer for the second example only. This is a sample of the double example small prompt version.

```text
### Instruction:
How many O symbols are inside these brackets?
### Input:
[O,O]
### Output: 2 

### Instruction:
How many O symbols are inside these brackets?
### Input:
[O,O,O,O,O]
### Output:
```
The answer should be 5. With this series the model got good scores. It succeded in identifying answers between 0 and 8. It only got the symbol for 9 wrong.
The next series is single example large prompt. None of the 'large prompt' examples produced good output. The single example large prompt was not correct for any input. The double example large prompt was correct for the integers 0 and 1. No others were correct.

```text
### Instruction:
How many O symbols are inside these brackets?
### Input:
[O...............O.....O......]
### Output: 
```
The answer should be 3.
Then double example large prompt.

```text
### Instruction:
How many O symbols are inside these brackets?
### Input:
[O...............O.....O......]
### Output: 3

### Instruction:
How many O symbols are inside these brackets?
### Input:
[O.........O.....O.....O......]
### Output:
```

The example should lead the model to reply with 4. Since so few correct answers were found with the 'large prompt' examples, we consider them a failure. Possibly if we used a different separator character the results would be better. These examples are easily read by people and apparently not easily read by this computer model.
