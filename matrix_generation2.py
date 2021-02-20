import numpy as np
import time
import random 
#start_time = time.time()
#print("Start time : \t",start_time)
def generate2D2matrix():
	matrix_2D2 = np.zeros((4,4),dtype = bool)

	#Assigning boundry Walls
	matrix_2D2[0,:] = matrix_2D2[:,0] = True
	matrix_2D2[3,:] = matrix_2D2[:,3] = True

	totalCells = 2**2 #except boundries
	totalWalls = int(2*totalCells/5)
	i =0
	while i!=totalWalls:
		wallIndex = random.sample(range(2),2)
		matrix_2D2[wallIndex[0]+1][wallIndex[1]+1] = True
		i += 1
	#print("Time of generate matrix ", time.time() - start_time)
	matrix_2D2[1][1] = False
	matrix_2D2[2][2] = False
	return matrix_2D2

def generate3D3matrix():
	matrix_3D3 = np.zeros((5,5,5),dtype = bool)
	#Assigning boundry Walls
	matrix_3D3[0,:,:] = matrix_3D3[:,0,:] = matrix_3D3[:,:,0] = True
	matrix_3D3[4,:,:] = matrix_3D3[:,4,:] = matrix_3D3[:,:,4] = True
	totalCells = 3**3 #except boundries
	totalWalls = int(totalCells/2)
	i =0
	while i!=totalWalls:
		wallIndex = random.choices(range(3),k=3)
		matrix_3D3[wallIndex[0]+1][wallIndex[1]+1][wallIndex[2]+1] = True
		i += 1
	#print("Time of generate matrix ", time.time() - start_time)
	matrix_3D3[1][1][1] = False
	matrix_3D3[3][3][3] = False
	return matrix_3D3

def generate7D7matrix():
	matrix_7D7 = np.zeros((9,9,9,9,9,9,9),dtype = bool)

	#Assigning boundry Walls
	matrix_7D7[0,...] = matrix_7D7[:,0,...] = matrix_7D7[:,:,0,...] = matrix_7D7[:,:,:,0,...] = matrix_7D7[:,:,:,:,0,...] = matrix_7D7[:,:,:,:,:,0,...] =matrix_7D7[...,0] = True
	matrix_7D7[8,...] = matrix_7D7[:,8,...] = matrix_7D7[:,:,8,...] = matrix_7D7[:,:,:,8,...] = matrix_7D7[:,:,:,:,8,...] = matrix_7D7[:,:,:,:,:,8,...] =matrix_7D7[...,8] = True

	totalCells = 7**7
	totalWalls = int(totalCells/2)
	i =0
	while i!=totalWalls:
		wallIndex = random.sample(range(7),7)
		matrix_7D7[wallIndex[0]+1][wallIndex[1]+1][wallIndex[2]+1][wallIndex[3]+1][wallIndex[4]+1][wallIndex[5]+1][wallIndex[6]+1] = True
		i += 1
	#print("Time of generate matrix ", time.time() - start_time)
	matrix_7D7[1][1][1][1][1][1][1] = False
	matrix_7D7[7][7][7][7][7][7][7] = False
	return matrix_7D7

def generate8D8matrix():
	matrix_8D8 = np.zeros((10,10,10,10,10,10,10,10),dtype = bool)
	#Assigning boundry Walls
	matrix_8D8[0,...] = matrix_8D8[:,0,...] = matrix_8D8[:,:,0,...] = matrix_8D8[:,:,:,0,...] = matrix_8D8[:,:,:,:,0,...] = matrix_8D8[:,:,:,:,:,0,...] = matrix_8D8[...,0,:] = matrix_8D8[...,0] = True
	matrix_8D8[9,...] = matrix_8D8[:,9,...] = matrix_8D8[:,:,9,...] = matrix_8D8[:,:,:,9,...] = matrix_8D8[:,:,:,:,9,...] = matrix_8D8[:,:,:,:,:,9,...] = matrix_8D8[...,9,:] = matrix_8D8[...,9] = True
	
	totalCells = 8**8
	totalWalls = int(2*totalCells/5)
	i =0
	while i!=totalWalls:
		wallIndex = random.sample(range(8),8)
		matrix_8D8[wallIndex[0]+1][wallIndex[1]+1][wallIndex[2]+1][wallIndex[3]+1][wallIndex[4]+1][wallIndex[5]+1][wallIndex[6]+1][wallIndex[7]+1] = True
		i += 1
	#print("Time of generate matrix ", time.time() - start_time)
	matrix_8D8[1][1][1][1][1][1][1][1] = False
	matrix_8D8[8][8][8][8][8][8][8][8] = False
	return matrix_8D8

#generating m,n,r size three dimensional matrix
def generate3DmnrMatrix(size_x=3,size_y=3,size_z=3):
	if(size_x == 3 and size_y==3 and size_z == 3):
		return generate3D3matrix()
	if (size_x<0 or size_y<0 or size_z<0):
		raise Exception("\n\tGive Valid dimentions as input\n")
	matrix_3Dmnr = np.zeros((size_z+2,size_y+2,size_x+2),dtype = bool)
	#Assigning boundry Walls
	matrix_3Dmnr[0,:,:] = matrix_3Dmnr[:,0,:] = matrix_3Dmnr[:,:,0] = True
	matrix_3Dmnr[size_z+1,:,:] = matrix_3Dmnr[:,size_y+1,:] = matrix_3Dmnr[:,:,size_x+1] = True
	totalCells = size_x*size_y*size_z #except boundries
	totalWalls = int(totalCells/2.5) #randomness in walls
	i =0
	while i!=totalWalls:
		wallIndex_x = random.randint(1,size_x)
		wallIndex_y = random.randint(1,size_y)
		wallIndex_z = random.randint(1,size_z)
		matrix_3Dmnr[wallIndex_z][wallIndex_y][wallIndex_x] = True
		i += 1
	#print("Time of generate matrix ", time.time() - start_time)
	# matrix_3Dmnr[1][1][1] = False
	# matrix_3Dmnr[3][3][3] = False
	return matrix_3Dmnr

def generateNDNmatrix(dimension) :
	if dimension == 2 :
		return generate2D2matrix()
	if dimension == 3 :
		print("\nProvide the Size of the system-world in 3D below:\n")
		size_x = int(input("\tSize in X :\t"))
		size_y = int(input("\tSize in Y :\t"))
		size_z = int(input("\tSize in Z :\t"))
		return generate3DmnrMatrix(size_x,size_y,size_z)
	if dimension == 7 :
		return generate7D7matrix()
	if dimension == 8 :
		return generate8D8matrix()
	print("given dimension is currently unavailable\n\n")
	return None

def generateDynamicMatrix(dimension,shape):
	shapeWithBoundry = [x+2 for x in shape]
	matrixWorld = np.ones(shapeWithBoundry,dtype = bool)
	totalWalls =1
	for i in shape:
		totalWalls *= i
	totalCells= int(2*totalWalls)
	i = 0
	while i!=totalCells:
		temp = []
		for j in range(dimension):
			temp.append(random.randint(1,shape[j]))
		matrixWorld[tuple(temp)]=False
		i+=1

	return matrixWorld
#print(generateNDNmatrix(3))


#print("ddd\n",generateDynamicMatrix(5,(5,3,2,3,4)))
# a = np.array(range(60))

# print(a.reshape((5,3,4)))