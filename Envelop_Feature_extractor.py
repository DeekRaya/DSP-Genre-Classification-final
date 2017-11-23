'''This Program  extracts various spectral envolop based features of each frame and writes them to a CSV file
Spectral features used here are :
1.Zero crossing rate - a estimate of pitch.
2.Spectral Centroid - to estimate the envelop
3.Spectral roll off - to estimate the shape of envelop
4.Spectral flux
These features are used and the classification using these features will be independent of other frames.The classifier's decision will
be baesed on the frame itself and is independent of other frames..'''

import numpy as np
import librosa as lb
import librosa.feature as ft
import scipy.io.wavfile as sc
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
import os
import spec_feature

#we shall use librosa to compute stft of each frame for a given music file..
#which shall be later used for computing spectral centroid
#spectral roll off.


#this will iterate through the directory and
working_dir="C:\\Users\\deekshisth raya\\Desktop\\DSP_draft1\\Training_Data_Set"
geners=os.listdir(working_dir)                #lists various geners in working directory
Train_files=dict()                            #A dictionary where key is the genere and the data is a list of all files in it
Train_files.fromkeys(geners)
for x in geners:                              # To make to dictionary Training data
    data=os.listdir(working_dir+'\\'+x)
    Train_files[x]=data

fig=plt.figure(1)                              #generating a figure to polt later
feature=dict()                                 #this contains feature vecotrs in repective genres
feature.fromkeys(geners)

mark=dict()
mark.fromkeys(geners)
mark[geners[1]]='x'
mark[geners[2]]='o'
mark[geners[3]]='+'
mark[geners[0]]='s'
#ax=fig.add_subplot(111,projection='3d')
for gener in geners:                          # This iterates in various directories over each genre
    z=np.array([[0]])                         #initializing nx1 vector having zero crossing rate of alll files in each genere
    cen=np.array([[0]])                       #initializing nx1 vector having centroid of all the files in each genre
    roll=np.array([[0]])                      #initializing nx1 vecotor having roll off of the files in each genre
    flux=np.array([[0]])

    for music in Train_files[gener]:          #this iterates over each files in a given genre
        name=working_dir + '\\' + gener + '\\' + music
        rate,data=sc.read(name)              #reading each file.rate store the sampling rate, data store a 1XN time series.

        if(len(data.shape)==2):               # resovling  files with 2 channels.
            data=data[:,0]


        z_t,cen_t,roll_t,flux_t=spec_feature.spec_features(data,2048,rate)

        z=np.concatenate((z,z_t),axis=1)
        cen=np.concatenate((cen,cen_t),axis=1)
        roll= np.concatenate((roll,roll_t), axis=1)
        flux=np.concatenate((flux,flux_t), axis=1)
    plt.scatter(z,cen,marker=mark[gener])
    #print z.shape,cen.shape,flux.shape
    #Axes3D.scatter(ax,z,cen,flux)



plt.show()