import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import style

#style.use('fivethirtyeight')



def visualize3D(matrixWorld ,directionList, start = (1,1,1),goal = (3,3,3)) :
	size_z,size_y,size_x = matrixWorld.shape
	size_x -= 2
	size_y -= 2
	size_z -= 2
	matrixWorld[0,:,:] = matrixWorld[:,0,:] = matrixWorld[:,:,0] = False
	matrixWorld[size_z+1,:,:] = matrixWorld[:,size_y+1,:] = matrixWorld[:,:,size_x+1] = False
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1,projection='3d')
	#ax2 = fig.add_subplot(1,2,2,projection = '3d')
	# your real data here - some 3d boolean array
	'''
	a = np.array([
		[
		[False,True,False],
		[True,True,True ],
		[False,False,False]
		],
		[
		[False,False,False],
		[False,True,True ],
		[False,True,False]
		],
		[
		[False,False,False],
		[False,False,False ],
		[False,True,False]
		],
		])
	'''

	x, y, z = np.indices((size_x+2, size_y+2, size_z+2))
	drone = (x==start[0])&(y==start[1])&(z==start[2])
	goalPlace = (x==goal[0])&(y==goal[1])&(z==goal[2])
	trajectoryList = []
	trajectoryList.append(start)
	for i in directionList :
		toAppend = list(trajectoryList[-1])
		if i[1] == "+":
			toAppend[3-int(i[0])] +=1
		else :
			toAppend[3-int(i[0])] -=1
		trajectoryList.append(tuple(toAppend))
	# ax.voxels(voxels,edgecolor='k')
	#ax.voxels(drone,facecolors = 'green',alpha=0.1)
	#ax.scatter3D(1.5,1.5,1.5,)
	ax.scatter3D(0,0,0,c="k",s=75)
	
	ax.voxels(goalPlace,facecolors = 'green',edgecolor = "yellow",alpha = 0)
	# ax.set_xlabel('x-axis')
	# ax.set_ylabel('y-axis')
	# ax.set_zlabel('z-axis')

	# Hide grid lines
	ax.grid(False)

	# Hide axes ticks
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	#plt.show()
	ax.voxels(matrixWorld,facecolors = 'brown',alpha = 0.3)

	def animate(i):
		if(i<len(trajectoryList)):
			x1,y1,z1 = trajectoryList[i]
			ax.scatter3D(x1+0.5,y1+0.5,z1+0.5,c = "green",marker = '*',s=100)
			drone = (x==x1)&(y==y1)&(z==z1)
			#ax.voxels(drone,facecolors = 'green',edgecolor = 'yellow',alpha = 0.5)
			#print(i)

	ani = animation.FuncAnimation(fig,animate, interval = 1000)
	plt.show()

	#plt.show() 	


#ax2.voxels(drone2,facecolors = 'green',edgecolor = 'purple')

'''
a = np.array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True, False, False, False,  True],
        [ True, False, False, False,  True],
        [ True, False,  True, False,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True, False, False,  True,  True],
        [ True, False, False, False,  True],
        [ True,  True, False, False,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True, False,  True, False,  True],
        [ True,  True, False, False,  True],
        [ True, False, False, False,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])
_trajectoryList = [(1,1,1),(1,1,2),(1,1,3),(1,2,3),(1,3,3),(2,3,3),(3,3,3)]
visualize3D(matrixWorld = a , start = (1,1,1),goal = (3,3,3),trajectoryList = _trajectoryList) 
'''