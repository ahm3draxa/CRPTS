  # CRPTS
CRPTS: Predicting Transcription Factor Binding Sites using DNA Shape Features Based on Shared Hybrid Deep Learning Architecture>
  # Requirements
  * To install Keras with Tensorflow backend, please refer to https://keras.io/#installation.
  * Tensorflow=1.2, keras=2.0
  * Python 2.7
  	
# Setting up
   Clone the repositopry into your working space.
# Data preparation
 Firstly, using encode.sh script to preprocess DNA sequences and their corresponding shape features.
   * Usage: bash encode.sh <pbmdata>
   * 'pbmdata' denotes the path of storing experimental data, e.g. /yourpath/pbmdata.
# Run CRPTS using DNA shape and DNA sequences or CRPT using DNA sequences
   * Usage: you can excute run.sh script directly, in which you should modify the python command accordingly, e.g.: 
    ```python train_val_test_hybrid.py -datadir ./pbmdata/$eachTF/data -run 'shape' -model 'CRPTS' -batchsize 300 -k 5 -params 30 --train```
   * The command '-run' means 'shape' using four shape features, and the command '-model' can be a choice of {'CRPTS', 'CRPT'}
   * Note that you should change the ouput path in the run.sh script, the naming rule is: ```'model_' + args.model + '_' + args.run.```
* Type the following for details on other optional arguments: 
    ```python train_val_test_hybrid.py -h```
 # Contact
 * If you have any problems, please contact SiguoWang: siguo_wang@163.com
