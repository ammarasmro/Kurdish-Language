# Kurdish Speech Recognizer

This part of the repo aims to train a speech recognition model for the Kurdish language.

## Data
The data at hand are recorded phone conversations obtained from LDC.

## Preprocessing
The wav files originally in the dataset were in the sphere format so they had to be converted into wav files. A tool called sph2pipe was used for this task.

Next the wave files needed to be in the PCM format to be fed into the model, so the soundfile library was used to process those files.

## Model
The model used can be found in the sample_models.py file.
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
the_input (InputLayer)       (None, None, 13)          0         
_________________________________________________________________
conv1d (Conv1D)              (None, None, 200)         28800     
_________________________________________________________________
bn_conv_1d (BatchNormalizati (None, None, 200)         800       
_________________________________________________________________
bidirectional_3 (Bidirection (None, None, 400)         481200    
_________________________________________________________________
bn_birnn (BatchNormalization (None, None, 400)         1600      
_________________________________________________________________
bidirectional_4 (Bidirection (None, None, 400)         721200    
_________________________________________________________________
bn_birnn2 (BatchNormalizatio (None, None, 400)         1600      
_________________________________________________________________
time_distributed_2 (TimeDist (None, None, 33)          13233     
_________________________________________________________________
softmax (Activation)         (None, None, 33)          0         
=================================================================
```
## Results
The training took a long time as I didn't have access to a GPU so I couldn't fine tune the model. The model overfitted on the training dataset with training loss: 16.9116, and validation loss: 49.3050, after 20 epochs.

Original text | Predicted text
--- | ---
sêşem sih û yekê sibata du hezar û bazdanê bazdan | sêşem si û yekê sibata du hezar û pazanên bazdan
du sed û sî û yek nod |  du sed û sî û yeklûye
sê sed û nozdeh û çar hezar û heft sed û şêst û yek |  sed û  es û çar rezar û heft sed û şêş sê
do tam bîst saet duyan de | do tamnê seet duyande



> Disclaimer: alot of the base code was borrowed from the Natural Language Processing Nanodegree as implementing a DNN Speech Recognizer was the last project of that degree. You can view my submission here [My Repo](https://github.com/ammarasmro/DNN-speech-recognizer)
