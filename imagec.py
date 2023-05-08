import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=[5,5]
A=imread(r"C:\Users\mits14\Downloads\dog.jpg")
X=np.mean(A,-1)
img=plt.imshow(X)
img.set_cmap('gray')
plt.title('orginal')
plt.show()
U,S,Vt=np.linalg.svd(X,full_matrices=True)
sigma=np.diag(S)
r=int(input('Enter the required rank r :'))
X_comp=U[:,:r]@sigma[0:r,:r]@Vt[:r,:]
img_1=plt.imshow(X_comp)
img_1.set_cmap('gray')
plt.title('Rank '+str(r)+' Approximation')
plt.show()
