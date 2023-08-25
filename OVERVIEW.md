

# 2023 08 07
TheBloke/Llama-2-7B-fp16

lora_05

160 mins

---

# 2023 08 08 

TheBloke/Llama-2-13B-chat-GPTQ:gptq-8bit-128g-actorder_False

LoRA training with GPTQ models requires loading with --monkey-patch .

---

# 2023 08 09

TheBloke/Llama-2-13B-fp16

Try this model with --load-in-8bit and see how long training is supposed to take.

5h12m

Note: this crashed around 4 hours

---

# 2023 08 12 - Saturday

TheBloke/Llama-2-13B-fp16

runpod.io - A40 - 48GB VRAM - approx $0.79/hr 

Try this model with '--load-in-8bit' and larger rank and smaller corpus. See how long training is supposed to take.
Auto-save the model checkpoint every so many steps. This should yeild many checkpoints if there are no crashes, and if
there are crashes then there would be a saved checkpoint from before the crash.
Use new images from the corpus generating gui. The new images should be bigger.

use:

- epochs: 1 
- auto-save: 75 steps
- input-token cutoff: 750
- lora-rank: 128 units
- lora-alpha: 256 units
- corpus length: 3,000 examples
- training time: 1h51mins

note:

The training is completed and the new LoRA is applied. After this process the model cannot easily 
answer other questions. It is, in essance, broken. It does answer the essential counting question better. 
It seems to know that the answer for the question is between 0 and 9. Also, numbers below 5 
have a higher probability of being answered correctly. It did answer in the form 'There are x.' where x is the number that the model is 
proposing is the answer. I think if the lora-rank were higher and the training was repeated 
the model might work even better at this task.

folder contents:
- lora_20.zip     training results for LoRA. 
- prompt.zip      pre-generated prompts for the first 10 cardinal integers.
- test.txt        this file.
- train.zip       pre-generated training files for alpaca training.

---

# 2023 08 15 - Tuesday

TheBloke/Llama-2-13B-fp16 

runpod.io - A6000 - 48GB VRAM - approx $0.79/hr 

use:

- epochs: 1
- auto-save: 75 steps
- input-token cutoff: 750
- lora-rank: 256 units (last test x2)
- lora-alpha: 512 units (last test x2)
- corpus length: 3,000 examples
- training time 1h32mins

note:

The training completed and the LoRA is applied. After words the model answers questions well, but is pre-occupied
with math questions. It answers questions like 'what is 3 + 2?' accurately. It doesn't get the right number of
dots in the ascii-art frames, but it always answers with integers between zero and nine. I dont know what
training would change the output.

---

# 2023 08 18 - Friday

TheBloke/Llama-2-13B-fp16 

runpod.io - A6000 - 48GB VRAM - approx $0.79/hr 

use:

- epochs: 1
- auto-save: 75 steps
- input-token cutoff: 750
- lora-rank: 256 units 
- lora-alpha: 512 units
- visualization using: tensorboard
- corpus length: 3,000 examples
- training time approx 1h32mins

note:

I should have $6.44 left in my account.
Try new/modified dataset. Make sure to activate tensorboard data collection.

1. download model in oobabooga. load model with --load-in-8bit option.
2. move prompts from local computer using runpodctl. Put them in the right folder.
3. move training data from local computer using runpodctl. Put them in the right folder.
4. Call LoRA 'lora_xx'.
5. set all controls as noted above.
6. start training.
7. After training, test model with prompts. Does it work better?
8. After training, prune checklists from lora folder.
9. zip remaining lora folder.
10. move lora_xx zip to local computer using runpodctl.
11. test lora_xx zip folder with tensorboard.

I have $4.76 left. I could not download the checkpoints, they were too large. (approx 5.1 GB) Testing 
the model (loaded with the LoRA) showed dreck output. There was always a display of an empty
ascii-art frame. It should be noted that the frame had the right height and width. This actually
was an improvement. No label number was displayed. 

The loss on the tensorboard display showed alot of room for improvement. The chart did not begin 
to level off.

---

# 2023 08 20 - Sunday

TheBloke/Llama-2-13B-fp16 

runpod.io - A6000 - 48GB VRAM - approx $0.79/hr 

use:

- epochs: 1
- auto-save: 75 steps
- input-token cutoff: 750
- lora-rank: 512 units (last test x2) 
- lora-alpha: 1024 units (last test x2)
- visualization using: tensorboard
- corpus length: 3,000 examples
- training time approx 2h00mins

note:

I should have $4.76 left in my account. Add $10.00 to account.
Try expanded LoRA rank. Make sure to activate tensorboard data collection.

1. download model in oobabooga. load model with --load-in-8bit option.
2. move prompts from local computer using runpodctl. Put them in the right folder.
3. move training data from local computer using runpodctl. Put them in the right folder.
4. Call LoRA 'lora_xx'.
5. set all controls as noted above.
6. start training.
7. After training, test model with prompts. Does it work better?
8. After training, prune checklists from lora folder.
9. zip remaining lora folder.
10. move lora_xx zip to local computer using runpodctl.
11. test lora_xx zip folder with tensorboard.

Do training twice. Examine tensorboard graph of loss. Graph shows loss leveling off 
at second epoch but output from testing does not improve massively. runpodctl does not
work well for large downloads and the lora_xx zip download is 1.5 GB. Setup Google Cloud
service so that lora rank can be expanded further. Next time try lora rank of 1024.

/workspace/text-generation-webui/loras

---

# 2023 08 26 - Saturday

TheBloke/Llama-2-13B-fp16 

runpod.io - A6000 - 48GB VRAM - approx $0.79/hr 

use:

- epochs: 1
- auto-save: 75 steps
- input-token cutoff: 750
- lora-rank: 768 units 
- lora-alpha: 1536 units 
- visualization using: tensorboard
- corpus length: 3,000 examples
- training time approx 2h00mins
- runpod.io local folder path: /workspace/text-generation-webui/loras

note:

I should have $4.76 left in my account. Add $10.00 to account.
Try expanded LoRA rank. Make sure to activate tensorboard data collection.

1. download model in oobabooga. load model with --load-in-8bit option.
2. move prompts from local computer using runpodctl. Put them in the right folder.
3. move training data from local computer using runpodctl. Put them in the right folder.
4. Connect running instance to Google Cloud. Note local and remote folder name. Input api json file.
5. Call LoRA 'lora_xx'.
6. set all controls as noted above.
7. start training.
8. After training, test model with prompts. Does it work better?
9. Examine output in Google Cloud. Download LoRAs. 
10. After training, prune checklists from lora folder. Look in Google Cloud.
11. zip remaining lora folder.
12. move lora_xx zip to local computer using runpodctl.
13. test lora_xx zip folder with tensorboard.

Do training twice. Examine tensorboard graph of loss. Graph shows loss leveling off 
at second epoch but output from testing does not improve massively. runpodctl does not
work well for large downloads and the lora_xx zip download is 1.5 GB. Setup Google Cloud
service so that lora rank can be expanded further. Next time try lora rank of 768.

/workspace/text-generation-webui/loras
