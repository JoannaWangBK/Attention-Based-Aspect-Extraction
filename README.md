# Attention-Based Aspect Extraction
This repository is a fork of [updated code repository](https://github.com/madrugado/Attention-Based-Aspect-Extraction) which contains an updated version of the [original author's code repository](https://github.com/ruidan/Unsupervised-Aspect-Extraction). The updated code repository included the following code improvements:
* python 3 compliant
* Keras 2 compliant
* Keras backend independent
* added optional input for seed words to train using Russian language 
* no need to specify embedding dimension with external embedding usage model

Our version of the code includes the following enhancements:
* updates to the evalauation code to improve functionailty and add additional outputs to assess model performance
* ability to run using Amazon review data

## Data
You can find the pre-processed datasets in [[Download]](https://drive.google.com/open?id=1j3qXQYe7QuWRG-pA3EzYPiGm80KRF3wB). The zip file should be decompressed and put in the main folder.

You can also download the original Amazon datasets for the speaker and headphone domain in [[Download]](https://drive.google.com/open?id=1oegIniCVLmsm_N_pzWdoOvv5yG5At6AG). For preprocessing, put the decompressed zip file in the main folder and run 
```
python preprocess.py
python word2vec.py
```
respectively in code/  The preprocessed files for the speaker domain will be saved in a folder preprocessed_data/speaker

## Train
Under code/ and type the following command for training:
```bash
python train.py \
--emb-name ../preprocessed_data/speaker/w2v_embedding \
--domain speaker -o output_dir --vocab-size 11000 --aspect-size 20
```
where *--emb*-name is the path to the pre-trained word embeddings generated in word2vec.py, --domain indicates the speaker domain, -o points to the output directory, --vocab-size is the size of the vocabulary, which for our final model is 11,000, --aspect-size is the number of clusters, which is be 20 for our final model. 

After training, two output files will be saved in code/output_dir/speaker/: 1) *aspect.log* contains extracted aspects with top 100 words for each of them. 2) *model_param* contains the saved model weights

## Evaluation
Under code/ and type the following command:
```bash
python evaluation.py \
--domain speaker -o output_dir  --vocab-size 11000 --aspect-size 20
```
Note that you should keep the values of arguments for evaluation the same as those for training (except *--emb-name*, you don't need to specify it), as we need to first rebuild the network architecture and then load the saved model weights.

This will output a file *att_weights* that contains the attention weights on all test sentences in code/output_dir/speaker.

To assign each test sentence an aspect label, you need to first manually map each inferred aspect to a gold aspect label according to its top words in in evaluation.py (line 178-180) for evaluaton using F scores.

One example of trained model for the speaker domain has been put in pre_trained_model/speaker/, and the corresponding aspect mapping has been provided in evaluation.py (line 178-180).

## Dependencies
* keras>=2.0
* tensorflow>=1.4
* numpy>=1.13

## Cite
If you use the code, please consider citing original paper:
```
@InProceedings{he-EtAl:2017:Long2,
  author    = {He, Ruidan  and  Lee, Wee Sun  and  Ng, Hwee Tou  and  Dahlmeier, Daniel},
  title     = {An Unsupervised Neural Attention Model for Aspect Extraction},
  booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = {July},
  year      = {2017},
  address   = {Vancouver, Canada},
  publisher = {Association for Computational Linguistics}
}
```





