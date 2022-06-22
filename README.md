# Capstone_mutimodal: DASC7600 Capstone project

This is the pytroch implementation for the paper:
>RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR. [Paper in arXiv](https://arxiv.org/abs/2111.11665).
 
The code is adapted from this [repo](https://github.com/marshuang80/penet). (Code for PENet)




## Usage

### Environmemt Setup

The pacakges required are list below and the version is the lastest.
* Pytorch
* Numpy
* Pandas
* sklearn
* scipy


## For Windows User

* The path in train.sh and test.sh have to be windows-style. 
* The path in `read_pkl.py`,`./scripts/create_pe_hdf5_update.py` and  `generate_ehr.py` have to be windows-style.
* Go to `datasets/ct_pe_dataset_3d.py` and find `_load_volume()` to see the comment in that function.

### Data Preparation

CT data and EHR records can be downloaded [here](https://stanfordaimi.azurewebsites.net/datasets/3a7548a4-8f65-4ab7-85fa-3d68c9efc1bd.)   


If you choose to use only part of the CT data,      


1. put the .npy files into the directory `data/raw`
2. put the .csv files into `data/`
3. *Generate .pkl file for the part of data we choose:*    modify the list part_of_study in `read_pkl.py`: fill the list with 'idx' of the data you choose and run `python read_pkl.py`, then a file named `series_list.pkl` will appear in `data/processed`
4. *Generate hdf5 file for the part of data we choose:*    run `python ./scripts/create_pe_hdf5_update.py` to generate data.hdf5 file under the directory `data/processed` (
5. *Generate combined EHR record for the part of data we choose:*    modify the list part_of_study in `generate_ehr.py`:fill the list with 'idx' of the data you choose and run `python generate_ehr.py`, then a file named part_of_ehr.csv will appear in `data/processed`

Just to check there are three files in `data/processed` after doing the steps above:
* series_list.pkl
* data.hdf5 
* part_of_ehr.csv 



### Pretrained model

Our model has two parts: PENet and Elasticnet. Download the best checkpoint of PENet and put it into `./data/ckpt`. 

### Train and test

To train the fusion model, run `sh train.sh`. After the training is finished, the trained model is stored at `./train_logs`. 
To test the model, modify the `ckpt_path` in test.sh and run `sh test.sh`




If you choose to use all the CT data, 

> Just put the corresponding .hdf5, series_list.pkl and part_of_ehr.csv into `data/processed`.




