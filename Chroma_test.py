import librosa as li
import librosa.feature as lf
import numpy as np
import librosa.display as ld
import scipy.io.wavfile as sc
import matplotlib.pyplot as plt
import sklearn.svm as svm
import csv
import os

tds=open('Chroma_Features_t.csv','wb')
tds_write=csv.writer(tds)

working_dir="C:\\Users\\deekshisth raya\\Desktop\\DSP_draft1\\Test_Data_Set"
geners=os.listdir(working_dir)                #lists various geners in working directory
Train_files=dict()                            #A dictionary where key is the genere and the data is a list of all files in it
Train_files.fromkeys(geners)
for x in geners:                              # To make to dictionary Training data
    data=os.listdir(working_dir+'\\'+x)
    Train_files[x]=data

fig=plt.figure(1)                              #generating a figure to polt later
feature=dict()                                 #this contains feature vecotrs in repective genres
feature.fromkeys(geners)
for gener in geners:                          # This iterates in various directories over each genre


    for music in Train_files[gener]:          #this iterates over each files in a given genre
        name=working_dir + '\\' + gener + '\\' + music
        rate,data=sc.read(name)

        print rate,data
        if (len(data.shape) == 2):  # resovling  files with 2 channels.
            data = data[:,0]


        C_DFT=lf.chroma_stft(y=data,sr=rate)



        C_DF=C_DFT.T
        label=[[gener]*C_DFT.shape[1]]
        label=np.array(label)
        print label.shape,C_DF.shape
        out=np.concatenate((label.T,C_DF),axis=1)
        print out.shape
        tds_write.writerows(out)

tds.close()

