# Training

## Background ParlAI Training
There are many many options and arguments, your best source to get an overview is the shell script [./train_script.sh](https://github.com/Roboy/ParlAI/blob/master/projects/roboy/train/roboy_train_profilememory.sh) or the according ParlAI functions.
### Training Options
- define a timeframe in which to train
- define a number of epochs to train
- PATIENCE: when the validation accuracy doesn't improve X times in a row training is considered complete.
### Pre-trained models & fine-tuning
- There are pre-trained models available through model zoo. However, they have been trained using a different implementation and are not really compatible to what is there now. Training from scratch does not hurt and one gets decent results within 10 epochs or so. 


## How To: Set up training
- go to shell script in ss18_showmaster/ParlAI/projects/roboy/train/
- set your hyper parameters
- if batches are too large you will run into CUDA memory errors (-bs up to 128 works on P100, -bs 64 for K80)
- add, commit, push changes to ParlAI git

## How To: Train
- [Boot ubuntu1604uswest1b VM instance on GCP](https://console.cloud.google.com/compute/ )
- Click SSH to open new shell in browser (alternatively, install gcloud command line tools on local machine)
- go to ParlAI and pull
- do: $ screen (you need to install [screen](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/) first)
- activate virtual environment 
```
source ~/venvParlAI36/bin/activate
```
- run shell script from ss18_showmaster/ParlAI/projects/roboy/train/
- log-file will be saved to path defined in shell script
- model will be saved to /tmp/
- Press Ctrl+a, Ctrl+d in quick sequence -> screen is now detached
- now you can close the shell while training continues
- to return to this screen, open shell and do screen -r (or screen -ls if multiple; don't forget to detach again)

#### Fine Tuning
In the shell script you can specify a model and dict file to load before training. This could look something like this:
```
python3 roboy_training.py --model-file `[path]/roboy_profilemem --dict-file [path]/roboy_profilemem.dict -nl 2 -bs 128 -lr 0.001 -dr 0.2
```
_Make sure to have the --model-file and --dict-file flags before setting the training parameters. Parser arguments will be overwritten otherwise!_

## How To: Retrieve Data and Evaluate Training
- to retrieve log files, do 
```
gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ss18_showmaster/ParlAI/data/models/convai2/profilememory ~/Desktop
```
- locally, activate your virtual environment and start the iPython AnalysisNotebook and follow the process there
- you might need to adapt names/directories
- you might need to adapt the end criteria under point 4 to match your particular log file
- to retrieve the model if log files show it is valuable, do 
```
gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:/tmp/ ~/Desktop
```
- to interactively test a model you can use 
```
python projects/convai2/baselines/profilememory/interactive.py 
```
using the appropriate falgs such as
```
python projects/convai2/baselines/profilememory/interactive.py --model-file [path]/roboy_profilemem --dict-file [path]/roboy_profilemem.dict
```
- shut down the computing engine after training, otherwise Roboy will still be charged. (depending on setup, between ~$1.50/h and ~$3/h)

# About GCloud Compute Engine
## Set up
- get [gcloud command line tools](https://cloud.google.com/sdk) locally on your machine
- put the folder somewhere where you wont delete it
- install using ./google-cloud-sdk/install.sh
- you can use the [Quickstart](https://cloud.google.com/sdk/docs/quickstart-macos) guide
- follow setup procedure there

## File Transfer
- Copy files from Instance to local machine: gcloud compute copy-files [INSTANCE_NAME]:[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]`, i.e.
```
gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ss18_showmaster/ParlAI/data/models/convai2/profilememory ~/Desktop'
```
- [Further file transfer help](https://cloud.google.com/compute/docs/instances/transfer-files)

## Configuration (21.06.2018)

### Structure:
- Showmaster git
- Pytorch venv

### GCP
- us-west1-b
- 8 vCPU
- 52 GB RAM
- 1 NVIDIA Tesla P100
- Ubuntu 16.04 LTS
- 50GB persistent storage 
- if you require more [storage](https://cloud.google.com/compute/docs/disks/add-persistent-disk)
- if you change these settings make sure you crosscheck if you need a [quota increase](https://console.cloud.google.com/iam-admin/quotas) (especially for GPU!) 

### Software
- Python 3.6
- [Nvidia drivers](https://cloud.google.com/compute/docs/gpus/add-gpus)
- Cuda 9.0 (9.1 does not work (trust me I tried))
- [Screen reconnection](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)
