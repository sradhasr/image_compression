for i in range(10,100,25):
 x_comp=U[:,:i]@sigma[0:i,:i]@Vt[:i,:]
 img_1=plt.imshow(x_comp)
 img_1.set_cmap('gray')
 plt.title('rank '+str(i)+'approximation')
 plt.show()
