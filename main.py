import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


import mainController
import time

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class treeView:
	def __init__(self,data):
		self.children = []
		self.data = data
	def pushChildren(self,data):
		self.children.append(data)
	def getChildren(self):
		return self.children

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom




def makeViews(shape):
	#n,n-1,n-2,n-3...1
	listViewFrames = []
	nestedListButtonFrames =[]
	viewFrame0 = tk.LabelFrame(mainFrame,padx = 10,pady = 20, text=str((str(len(shape))+"D object consisting of " +str(shape[0])+ " " + (str(len(shape)-1)))+ "D objects" ) )
	viewFrame0.pack()
	tempFrames =[]
	for i in range(shape[0]):
		nestedFrame =  tk.LabelFrame(viewFrame0, text= "||",bg = "grey")
		nestedFrame.pack()
		b1 = tk.Button(nestedFrame,width =10,text=(str(len(shape)-1)+"D "),command = lambda inew=i : clickk(0,inew,shape,listViewFrames))
		b1.pack(fill = 'both')#store array of nested frames to change the colour
		tempFrames.append(nestedFrame)
	listViewFrames.append(viewFrame0)
	nestedListButtonFrames.append(tempFrames)
	prefixProduct = 1
	for i in range(len(shape)-1):#check for last index
		prefixProduct *= shape[i]
		for j in range(prefixProduct):
			viewFrame0 = tk.LabelFrame(mainFrame,padx = 10,pady = 20, text=str(str(len(shape) - i -1)+"D object consisting of" + str(shape[i+1]) +"D objects") )
			#viewFrame0.pack()
			tempFrames =[]
			frameIndex=len(listViewFrames)
			for k in range(shape[i+1]):#check for errors
				nestedFrame =  tk.LabelFrame(viewFrame0, text= "||",bg = "grey")
				nestedFrame.pack()
				b1 = tk.Button(nestedFrame,width =10, text=(str(len(shape) - i -2)+"D "),command = lambda knew=k,frameIndex_=frameIndex: clickk(frameIndex_,knew,shape,listViewFrames))#check
				b1.pack(fill = 'both')#store array of nested frames to change the colour
				tempFrames.append(nestedFrame)
			backButton = tk.Button(viewFrame0,width =5, text="Back",padx = 5 ,pady = 5,command = lambda frameIndex_ = frameIndex:backClick(frameIndex_,shape,listViewFrames))
			backButton.pack()
			listViewFrames.append(viewFrame0)
			nestedListButtonFrames.append(tempFrames)
	return [listViewFrames,nestedListButtonFrames]

	
		#array_.append(nestedFrame)


def clickk(frameIndex,buttonIndex,shape,listViewFrames):
	#print(len(listViewFrames))
	
	viewFrameinDimension = []
	viewFrameinDimension.append(1)
	for i in shape[:-1]:
		viewFrameinDimension.append(viewFrameinDimension[-1]*i)
	prefixSum = 0
	for i in range(len(viewFrameinDimension)):
		prefixSum+= viewFrameinDimension[i] 
		if frameIndex < prefixSum:
			whichIndexinDimension = frameIndex -(prefixSum - viewFrameinDimension[i])
			nextIndexFrame= prefixSum + whichIndexinDimension*shape[i] + buttonIndex
			break
	#nextIndexFrame = 1
	#print(frameIndex,buttonIndex,nextIndexFrame)
	if(nextIndexFrame < len(listViewFrames)):
		listViewFrames[frameIndex].pack_forget()
		listViewFrames[nextIndexFrame].pack()
	#viewFrame.pack_forget()
	return 

def backClick(frameIndex,shape,listViewFrames):
	
	viewFrameinDimension = []
	viewFrameinDimension.append(1)
	for i in shape[:-1]:
		viewFrameinDimension.append(viewFrameinDimension[-1]*i)
	prefixSum = 0
	for i in range(len(viewFrameinDimension)):
		prefixSum+= viewFrameinDimension[i] 
		if frameIndex < prefixSum:
			whichIndexinDimension = frameIndex -(prefixSum - viewFrameinDimension[i])
			nextIndexFrame = (prefixSum - viewFrameinDimension[i] -viewFrameinDimension[i-1])+whichIndexinDimension//shape[i-1]
			break
	#print(frameIndex,nextIndexFrame)
	#nextIndexFrame = 0
	if(nextIndexFrame >=0):
		listViewFrames[frameIndex].pack_forget()
		listViewFrames[nextIndexFrame].pack()
	return
def clickEnter():
	global mainFrame
	mainFrame.destroy()
	#mainFrame = ttk.LabelFrame(secondFrame, text="This is a mainFrame")
	mainFrame = tk.Frame(my_canvas)
	my_canvas.create_window((0,0),window = mainFrame,anchor ="nw")
	#mainFrame.pack( fill="both",expand="yes")
#	
	global secondFrame1
	secondFrame1.destroy()
	secondFrame1 = tk.Frame(my_canvas1)

	my_canvas1.create_window((0,0),window = secondFrame1,anchor ="nw")


	dimension_ = int(str(dimension.get()))
	clickEnter.dimension__ = dimension_
	#worldShape_1 = tuple(map(int,str(worldShape.get()).split(',')))
	worldShape_ = tuple(map(int,str(worldShape.get()).split(',')))
	start_ = tuple(map(int,str(start.get()).split(',')))
	goal_ = tuple(map(int,str(goal.get()).split(',')))
	algoIndex = int(comboExample.current())
	#print(worldShape_)
	print("\tDimension : ",dimension_)
	print("\tShape : ",worldShape_)
	print("\tStart : ",start_)
	print("\tGoal : ",goal_)
	viewFrameinDimension = []
	viewFrameinDimension.append(1)
	for i in worldShape_[:-1]:
		viewFrameinDimension.append(viewFrameinDimension[-1]*i)

	directionList,matrixWorld = mainController.getDirections(dimension = dimension_,worldShape = worldShape_,start = start_,goal = goal_,algoIndex = algoIndex)
	print("YE RAHA PATH:",directionList)
	
	# bm = tk.Button(mainFrame,text=" Play Animation ",activebackground = "cyan",command = lambda:True)
	# bm.pack(side = 'top',pady = 25)
	nestedListButtonFrames= outputFn(matrixWorld,worldShape_,start_,goal_,directionList)
	bm.configure(command = lambda:playAnimation(worldShape_,start_,directionList,viewFrameinDimension,nestedListButtonFrames))
	return

def outputFn(matrixWorld,shape,start,goal,directionList):
	returnLists = makeViews(shape)
	listViewFrames,nestedListButtonFrames = returnLists
	viewFrameinDimension = []
	viewFrameinDimension.append(1)
	for i in shape[:-1]:
		viewFrameinDimension.append(viewFrameinDimension[-1]*i)
	prefixSum = 0
	frameIndexStart= 0
	frameIndexGoal = 0
	for i in range(len(viewFrameinDimension)):
		nestedListButtonFrames[frameIndexStart][shape[i]-start[i]].configure(text = "start",highlightbackground = "magenta", highlightcolor= "magenta",bg = "magenta")
		frameIndexStart = (prefixSum + viewFrameinDimension[i])+(frameIndexStart-prefixSum)*shape[i] + shape[i]-start[i] #+ shape[i]-start[i]
		nestedListButtonFrames[frameIndexGoal][shape[i]-goal[i]].configure(text = "goal",bg = 'red')
		frameIndexGoal = (prefixSum + viewFrameinDimension[i])+(frameIndexGoal-prefixSum)*shape[i] + shape[i]-goal[i] #+ shape[i]-start[i]
		prefixSum+= viewFrameinDimension[i]
		if(frameIndexGoal == frameIndexStart  and start[i] == goal[i]):
			nestedListButtonFrames[frameIndexGoal][shape[i]-goal[i]].configure(bg = 'brown')
	#animation begins
	
		'''
		time.sleep(0.01)
		prefixSum = 0
		#frameIndexTemp= 0
		frameIndexTempN= 0
		for i in range(len(viewFrameinDimension)):

			#nestedListButtonFrames[frameIndexTemp][shape[i]-temp[i]].configure(bg = 'yellow')
			#frameIndexTemp = (prefixSum + viewFrameinDimension[i])+(frameIndexTemp-prefixSum)*shape[i] + shape[i]-temp[i] #+ shape[i]-start[i]
			nestedListButtonFrames[frameIndexTempN][shape[i]-tempN[i]].configure(text = "||",bg = 'grey')
			#time.sleep(0.5)
			#nestedListButtonFrames[frameIndexTempN][shape[i]-tempN[i]].configure(text = "||",bg = 'grey')
			frameIndexTempN = (prefixSum + viewFrameinDimension[i])+(frameIndexTempN-prefixSum)*shape[i] + shape[i]-tempN[i] #+ shape[i]-start[i]
			prefixSum+= viewFrameinDimension[i]
		'''
	return nestedListButtonFrames
def viewFn():
	#dimension = int(str(dimension.get()))
	if(clickEnter.dimension__== 3):
		#print("$)")
		mainController.visualIt()
	return
def animationLA(shape,start,goal,directionList):
	print(shape)
	return
def playAnimation(shape,start,directionList,viewFrameinDimension,nestedListButtonFrames):
	#print(shape)
	tempN = list(start)
	dimension = len(shape)
	#making grey
	prefixSum = 0
	#frameIndexTemp= 0
	frameIndexTempN= 0
	for i in range(len(viewFrameinDimension)):

		#nestedListButtonFrames[frameIndexTemp][shape[i]-temp[i]].configure(bg = 'yellow')
		#frameIndexTemp = (prefixSum + viewFrameinDimension[i])+(frameIndexTemp-prefixSum)*shape[i] + shape[i]-temp[i] #+ shape[i]-start[i]
		nestedListButtonFrames[frameIndexTempN][shape[i]-tempN[i]].configure(bg = 'grey')
		#time.sleep(0.5)
		#nestedListButtonFrames[frameIndexTempN][shape[i]-tempN[i]].configure(text = "||",bg = 'grey')
		frameIndexTempN = (prefixSum + viewFrameinDimension[i])+(frameIndexTempN-prefixSum)*shape[i] + shape[i]-tempN[i] #+ shape[i]-start[i]
		prefixSum+= viewFrameinDimension[i]
	#making green
	j=directionList[0]
		
	if(j[1] == '+'):
		tempN[dimension - int(j[0])] +=1
	else:
		tempN[dimension - int(j[0])] -=1
	#print(tempN)
	prefixSum = 0
	#frameIndexTemp= 0
	frameIndexTempN= 0
	for i in range(len(viewFrameinDimension)):

		#nestedListButtonFrames[frameIndexTemp][shape[i]-temp[i]].configure(bg = 'yellow')
		#frameIndexTemp = (prefixSum + viewFrameinDimension[i])+(frameIndexTemp-prefixSum)*shape[i] + shape[i]-temp[i] #+ shape[i]-start[i]
		nestedListButtonFrames[frameIndexTempN][shape[i]-tempN[i]].configure(bg = 'green')
		#time.sleep(0.5)
		#nestedListButtonFrames[frameIndexTempN][shape[i]-tempN[i]].configure(text = "||",bg = 'grey')
		frameIndexTempN = (prefixSum + viewFrameinDimension[i])+(frameIndexTempN-prefixSum)*shape[i] + shape[i]-tempN[i] #+ shape[i]-start[i]
		prefixSum+= viewFrameinDimension[i]
	textR = tk.Label(secondFrame1,text = str(tempN))
	textR.pack()
	if(len(directionList)==1):
		return
	else:
		mainFrame.after(1000,playAnimation,shape,tempN,directionList[1:],viewFrameinDimension,nestedListButtonFrames)
	return
def demoRunFn():
	global mainFrame
	mainFrame.destroy()
	#mainFrame = ttk.LabelFrame(secondFrame, text="This is a mainFrame")
	mainFrame = tk.Frame(my_canvas)
	my_canvas.create_window((3,15),window = mainFrame,anchor = "nw")
	#mainFrame.pack( fill="both",expand="yes")
#	
	global secondFrame1
	secondFrame1.destroy()
	secondFrame1 = tk.Frame(my_canvas1)

	my_canvas1.create_window((3,12),window = secondFrame1,anchor= "nw")
	directionList,matrixWorld = mainController.getDirections(dimension = 3,worldShape = (7,7,7),start = (1,1,1),goal = (5,5,5),algoIndex = 0)
	print("YE RAHA :",directionList)
	nestedListButtonFrames=outputFn(matrixWorld,(7,7,7),(1,1,1),(5,5,5),directionList)
	viewFrameinDimension = []
	viewFrameinDimension.append(1)
	shape = (7,7,7)
	for i in shape[:-1]:
		viewFrameinDimension.append(viewFrameinDimension[-1]*i)
	playAnimation((7,7,7),(1,1,1),directionList,viewFrameinDimension,nestedListButtonFrames)
	mainController.visualIt()
	return

"________________________________________________"
root = tk.Tk()
inputFrame = tk.LabelFrame(root,text = "")
inputFrame.pack(fill ='x')
demoFrame = tk.LabelFrame(inputFrame,text = "DemoFrame",padx = 10,pady=10,highlightbackground ="magenta")
demoText = tk.Label(demoFrame,justify = "left",text = "The demo run uses 3D space\n Shape : (7,7,7) ,\n Start : (1,1,1) ,\n Goal : (5,5,5) \n")
demoText.pack()
demoButton = tk.Button(demoFrame,text = "Run Demo",command = demoRunFn,activebackground = "cyan")
demoButton.pack()
demoFrame.pack(side = "left")
numberInputFrame = tk.LabelFrame(inputFrame,padx = 20,pady=20,highlightbackground ="cyan")
numberInputFrame.pack(fill ='both',side = "left")
i1 = tk.Label(numberInputFrame , text = " Dimension : ")
i1.grid(row = 0 ,column = 0)
dimension = tk.Entry(numberInputFrame)
dimension.grid(row = 0 ,column = 1)
i2 = tk.Label(numberInputFrame , text = " Shape  : ")
i2.grid(row = 1 ,column = 0)
worldShape = tk.Entry(numberInputFrame)
worldShape.grid(row = 1 ,column = 1)
i3 = tk.Label(numberInputFrame , text = " Start State  : ")
i3.grid(row = 2 ,column = 0)
start = tk.Entry(numberInputFrame)
start.grid(row = 2 ,column = 1)
i4 = tk.Label(numberInputFrame , text = " Goal State  : ")
i4.grid(row = 3 ,column = 0)
goal = tk.Entry(numberInputFrame)
goal.grid(row = 3 ,column = 1)
i5 = tk.Label(numberInputFrame , text = " Search Algorithm  : ")
i5.grid(row = 4 ,column = 0)
comboExample = ttk.Combobox(numberInputFrame,width = 20, values=["Breadth First Search" , "Uniform Cost Search" , "A* Graph Search" , "Depth First Search"])
comboExample.grid(row = 4,column = 1)
comboExample.current(0)


instructionFrame = tk.LabelFrame(inputFrame,text="")
instructionText = tk.Label(instructionFrame,justify = "left",anchor ="w",text = "INSTRUCTIONS : \n[1] Dimension must be a natural number, try any possible dimesion(Runnig time increases exponentially).\n[2] Shape Input: Use comma (',') delimeter. E.g If dimension is 4 and shape is 10 units in W-axis,3 in Z, 34 in Y and 12 in X, then input: 10,3,34,12 .\n[3]Start state is indexed from 1. E.g. left bottom of 3Dmatrix is  1,1,1. \n[4]DFS and higher dimension inputs consume significant time, so either increase your patience or get a faster processor.\n[5]If dimension is 3, 'View3D' Button will make the animation visuals.(recommended) \n[6]Randomness abstracted in generation of walls and assigning cost function \n[7]If Scrollbar is not function, try minimizing and maximizing screen again.\n[8]The robot manipulator gif shown is for illustraion purposes.\nThe dimension is equal to number of joints in manipulator, and shape equals distinct values each theta can take\n\n\t\t\tCreator : RUSHIL KAUSHAL SANGHAVI , Address : sanghavi.1@iitj.ac.in ")
instructionText.pack(fill = "both")
instructionFrame.pack(expand =1, side = "right",fill = tk.BOTH)
b5 = tk.Button(numberInputFrame,text = " Submit ",command = clickEnter,activebackground="cyan")
b5.grid(row = 5,column =1)
b6 = tk.Button(numberInputFrame,text = " View3D ",command = viewFn,activebackground="cyan")
b6.grid(row = 6,column =2,padx = 5,ipadx = 5)
bm = tk.Button(numberInputFrame,text=" Play Animation ",activebackground = "cyan",command = lambda:True)
bm.grid(row = 6,column =1)
OutputFrame = tk.LabelFrame(root, text=" Output Frame")
OutputFrame.pack(side = "right", fill="both",expand = 1)#

my_canvas = tk.Canvas(OutputFrame)
my_canvas.pack(side = tk.LEFT,expand = 1,fill = tk.BOTH)

my_scrollbar = ttk.Scrollbar(OutputFrame,orient = tk.VERTICAL,command = my_canvas.yview)
my_scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

my_canvas.configure(yscrollcommand =my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

mainFrame = tk.Frame(my_canvas)

my_canvas.create_window((0,0),window = mainFrame,anchor ="nw")

# mainFrame = tk.LabelFrame(secondFrame, text="This is a mainFrame")
# mainFrame.pack( fill="both",expand="yes")

#for right
OutputFrame1 = tk.LabelFrame(root, text="The Path :")
OutputFrame1.pack(side = "right", fill="both")#

my_canvas1 = tk.Canvas(OutputFrame1)
my_canvas1.pack(side = tk.LEFT,expand = 1,fill = tk.BOTH)

my_scrollbar1 = ttk.Scrollbar(OutputFrame1,orient = tk.VERTICAL,command = my_canvas1.yview)
my_scrollbar1.pack(side = tk.RIGHT,fill = tk.Y)

my_canvas1.configure(yscrollcommand =my_scrollbar1.set)
my_canvas1.bind('<Configure>',lambda e: my_canvas1.configure(scrollregion = my_canvas1.bbox("all")))

secondFrame1 = tk.Frame(my_canvas1)

my_canvas1.create_window((0,0),window = secondFrame1,anchor ="nw")

# lll = makeViews(tuple([5,4,5,3]))
# print(len(lll[0]))
# lll[1][0][0].configure(bg = 'green')
'''
viewFrame = tk.LabelFrame(mainFrame, text="This is a view Frame that changes")
viewFrame.pack()
array_ = []
for i in range(7):
	nestedFrame =  tk.LabelFrame(viewFrame, text=str("This is a nestedFrame" + str(i+1)))
	nestedFrame.pack()
	b1 = tk.Button(nestedFrame, text=("BUTTON"+ str(i+1)),command = clickk)
	b1.pack(fill = 'both')
	array_.append(nestedFrame)
'''
#app = FullScreenApp(root)
#root.attributes("-fullscreen", True) 
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))

'''
def stream(label):
 
  try:
    image = video.get_next_data()
  except:
    video.close()
    return
  label.after(delay, lambda: stream(label))
  frame_image = ImageTk.PhotoImage(Image.fromarray(image))
  label.config(image=frame_image)
  label.image = frame_image
'''
# label = tk.Label(root)
# label.pack(side = "left",fill = "both")
# root.after(0, update, 0)

def stream(path):
	#global path
	global panel
	global img
	indexx = int(path[-7:-4]) +1
	if(indexx ==93):
		indexx=1
	indexPath = str(indexx)
	if(len(indexPath)==1):
		indexPath = "00"+indexPath
	if(len(indexPath)==2):
		indexPath = "0"+indexPath
	path = path[:-7]+indexPath+path[-4:]
	image1 = Image.open(path)
	img = ImageTk.PhotoImage(image1)
	#print(path)
	# ppp =tk.Label(root,image = img)
	# ppp.pack(side = "left",fill = "both")
	panel.configure(image = img)
	#print("1")
	#panel.pack(side = "left",fill = "both")
	#panel.after(100,stream)
	root.after(100,stream,path)
	return

path ="Images\ezgif-frame-001.jpg"
path2 = "GrimyHotBaboon-small.gif"
#video = imageio.get_reader(path)
#delay = int(1000 / video.get_meta_data()['fps'])

panel = tk.Label(root)
panel.pack(side = "left",fill = "both")

root.after(0,stream,path)
root.state('zoomed')
root.mainloop()