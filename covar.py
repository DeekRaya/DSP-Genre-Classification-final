import sklearn.svm as svm
import numpy as np
import pandas as pd
import csv
import librosa.display as ld
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier


#fp=open('corrcoef_extra.csv','wb')
#write=csv.writer(fp)

file_name='Chroma_window.csv'
df=pd.read_csv(file_name,delimiter=',',header=None)
mapping={'classical':1,'jazz':2,'metal':3,'rock':4}
df=df.replace({0:mapping})
feature=df[:][range(1,25)]
type=df[:][0]


#dum=pd.get_dummies(type,columns=[0])

'''file_name='Chroma_window.csv'
df_t=pd.read_csv(file_name,delimiter=',',header=None)

df_t=df_t.replace({0:mapping})
feature_t=df_t[:][range(1,25)]
type_t=df_t[:][0]'''


#label=type.applymap(lambda s: mapping[s])
#print label
#print type[:][0].replace(['classical'],[1],inplace=True)

#X_t=pd.DataFrame.as_matrix(feature_t)
#Y_t=np.array(type_t)

X=pd.DataFrame.as_matrix(feature)
Y=np.array(type)
print X.shape,Y.shape
#print X_t.shape,Y_t.shape,X.shape,Y.shape
#ld.specshow(np.cov(X.T))
#M=np.corrcoef(X.T)
#write.writerows(M)
#fp.close()

#plt.show()
'''clf=svm.SVC(kernel='rbf',C=5)
score=cross_val_score(clf,X,Y)
print score'''
'''clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(8,8))
score=cross_val_score(clf,X,Y)
print score'''
M=np.corrcoef(X.T)
plt.imshow(M)
plt.colorbar()
plt.show()





