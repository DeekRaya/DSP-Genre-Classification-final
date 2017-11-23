import librosa as li
import librosa.feature as lf
import numpy as np
import librosa.display as ld
import scipy.io.wavfile as sc
import matplotlib.pyplot as plt
import sklearn.svm as svm
import csv
import os
import util



tds=open('Chroma_Features_extra6_t.csv','wb')
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
        select=range(0,C_DFT.shape[1],6)
        for i in range(len(select)-1):
            C_DFT_temp=C_DFT[:,select[i]:select[i+1]]

            col=np.mean(C_DFT_temp,axis=1)

            bins=np.array(range(1,13,1))

            col2=np.reshape(col,(1,len(col)))
            cen=util.centorid(col,bins)
            var=util.spread(col,bins,cen)
            max=np.argmax(col)
            min=np.argmin(col)
            if(i!=len(select)-2):
                C_DFT_temp=C_DFT[:,select[i+1]:select[i+2]]
                col_next = np.mean(C_DFT_temp, axis=1)
                flux=np.abs(col_next-col)
                flux=np.sum(flux)/12.0
            else:
                print 0
            out=[gener,cen,var,max,min,flux]
            out2=np.concatenate((np.array([[gener]]),col2),axis=1)







            tds_write.writerows(out2)

tds.close()

