# Training

## Background ParlAI Training
There are many many options and arguments, your best source to get an overview is the shell script [./train_script.sh](https://github.com/Roboy/ParlAI/blob/master/projects/roboy/train/roboy_train_profilememory.sh) or the according ParlAI functions
### Training Options
- define a timeframe in which to train
- define a number of epochs to train
- PATIENCE: when the validation accuracy doesn't improve X times in a row training is considered finished
### Pre-trained models & fine-tuning
- There are pre-trained models available through model zoo. get them through running python projects/convai2/baselines/profilememory/interactive.py from the ParlAI folder for instance 
- For fine-tuning, include flags like
```
-- model-file ~/ss18_showmaster/ParlAI/data/models/convai2/profilememory/180703_1200/roboy_profilemem --dict-file ~/ss18_showmaster/ParlAI/data/models/convai2/profilememory/180703_1200/roboy_profilemem.dict
```
in the call.

## How To: Set up training
- go to shell script in ss18_showmaster/ParlAI/projects/roboy/train/
- set your hyper parameters
- if batches are too large you will run into CUDA memory errors (-bs up to 128 works)
- add, commit, push changes to ParlAI git
- add, commit,push latest ParlAI to ss18_showmaster 

## How To: Train
- [Boot useastdeepqa VM instance on GCP](https://console.cloud.google.com/compute/ )
- Click SSH to open new shell in browser (alternatively, install gcloud command line tools on local machine)
- go to ss18_showmaster and pull
- go to ParlAI and pull
- do: $ screen
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
- You can close the shell now (or just keep pressing Ctrl+a, Ctrl+d until all shells are closed)

## How To: Retrieve Data and Evaluate Training
- to retrieve log files, do 
```
gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ss18_showmaster/ParlAI/data/models/convai2/profilememory ~/Desktop
```
- locally, activate your virtual environment and start the iPython AnalysisNotebook and follow the process there
- you might need to adapt names/directories
- you might need to adapt the end criteria under 4 to match your log file
- to retrieve the model if log files show it is valuable, do 
```
gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:/tmp/ ~/Desktop
```
- to interactively test them you can use 
```
python projects/convai2/baselines/profilememory/interactive.py 
```
using the appropriate falgs such as
```
python projects/convai2/baselines/profilememory/interactive.py --model-file data/models/convai2/profilememory/180706_XXYY/roboy_profilemem --dict-file data/models/convai2/profilememory/180706_XXYY/roboy_profilemem.dict
```
- shut down the computing engine after training, otherwise Roboy will still be charged. (currently ~$1.50/h)

# About GCloud Compute Engine
## Set up
- get [gcloud command line tools](https://cloud.google.com/sdk)
- put the folder somewhere where you wont delete it
- install using ./google-cloud-sdk/install.sh
- [Quickstart](https://cloud.google.com/sdk/docs/quickstart-macos)
- new terminal window
- https://cloud.google.com/compute/docs/gcloud-compute/
./google-cloud-sdk/bin/gcloud init

## File Transfer
- Copy files from Instance to local machine: gcloud compute copy-files [INSTANCE_NAME]:[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]
- i.e. in a terminal do 'gcloud compute scp --recurse team_roboy@ubuntu1604uswest1b:~/ParlAI/data/models/convai2/profilememory ~/Desktop'
- [Further file transfer help](https://cloud.google.com/compute/docs/instances/transfer-files)

## Configuration (21.06.2018)

### Structure:
- Showmaster git
- Pytorch venv

### GCP
- us-west1-b
- 8 vCPU
- 52 GB memory (personachat data set needs >32GB RAM to train with torch)
- 1 NVIDIA Tesla P100 (usable in us-west1-b)
- Ubuntu 16.04 LTS
- 50GB persistent storage 
- if you require more [storage](https://cloud.google.com/compute/docs/disks/add-persistent-disk)
- if you change these settings make sure you crosscheck if you need a [quota increase](https://console.cloud.google.com/iam-admin/quotas) (especially for GPU!!) 

### Software
- Python 3.6
- [Nvidia drivers](https://cloud.google.com/compute/docs/gpus/add-gpus)
- Cuda 9.0 (9.1 does not work yet (trust me I tried))
- [Torch Lua 5.2](http://torch.ch/docs/getting-started.html) ([mind issues!](https://github.com/torch/distro/issues/239))
- [Screen reconnection](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)

### Further Requirements 
- [Spacy](https://spacy.io/usage/) (make sure to get module en as well!) 
- torchtext
- stop-words
