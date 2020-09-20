from PIL import Image, ImageDraw, ImageFont
import numpy
import argparse


def ImagefromTxt(Text):
	img = Image.new('RGB', (len(Text)*Size, Size), color = ('White'))

	fnt = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', Size)
	d = ImageDraw.Draw(img)
	d.text((0,0), Text , fill=("Black"), font=fnt)
	return img


def GetArrayfromImage(img):
	Img= numpy.array(img.convert("L"))
	for r,row in enumerate(Img):
		for i,index in enumerate(row):

			if index > 100:
				Img[r][i]=0
			else:
				Img[r][i]=1
	finalimg = Img.tolist()
	remove=[]
	for r,row in enumerate(finalimg):
		if row.count(1):
			continue
		remove.append(r)
	for i,rm in enumerate(remove):
		del finalimg[rm-i]
		add=[]
	while True:
		for row in finalimg:
			if row[-2] ==1:
				if args.Base:
					for i in range(len(finalimg[0])):
						add.append(1)
					for i in range(round(Size/10)):
						finalimg.append(add)
				return finalimg
		for row in range(len(finalimg)):
			finalimg[row]=finalimg[row][:-1]
	if args.Base:
		for i in range(len(final[0])):
			add.append(1)
		for i in range(round(Size/10)):
			finalimg.append(add)
	return finalimg

def rotate(img):
	return list(zip(*reversed(img)))


def PrintShadow(Text):
	file = open("Results.txt", "w")
	for i in Text:
		print(i)
		for e in i:
			file.write(str(e))
		file.write("\n")

def SaveVertice(x,y,z):
	try:
		 return Vertices.index([x,y,z])+1
	except:
		Vertices.append([x,y,z])
		return len(Vertices)


def Saveface(x,y,z,d,rein):

	if d=="X":
		Faces.append([
			SaveVertice(x,y,z),
			SaveVertice(x,y+1,z),
			SaveVertice(x,y+1,z+1),
			SaveVertice(x,y,z+1)
			])
	elif d=="Y":
		Faces.append([
			SaveVertice(x,y,z),
			SaveVertice(x+1,y,z),
			SaveVertice(x+1,y,z+1),
			SaveVertice(x,y,z+1)
			])
	elif d=="Z":
		Faces.append([
			SaveVertice(x,y,z),
			SaveVertice(x+1,y,z),
			SaveVertice(x+1,y+1,z),
			SaveVertice(x,y+1,z)
			])
def createdummy(x,y):
	Matrix=[]
	for r in range(x):
		row=[]
		for c in range(y):
			row.append(1)
		Matrix.append(row)
	return Matrix

parser= argparse.ArgumentParser()
parser.add_argument("--Resolution", type=int, default=40)
parser.add_argument("--Base", type=bool, default=False)
parser.add_argument("--TextA", type=str, default="ERROR")
parser.add_argument("--TextB", type=str)

args=parser.parse_args()

Size= args.Resolution
print("processing input data")
print("   create array from TextA")
SX=rotate(rotate(rotate(GetArrayfromImage(ImagefromTxt(args.TextA.upper())))))
print("   Done\n   create array from TextB")
try:
	SY=GetArrayfromImage(ImagefromTxt(args.TextB.upper()))
except:
	print("   No Text found! useing dummy")
	SY=createdummy(len(SX),len(SX[0]))
print("   Done")
SZ=createdummy(len(SY[0]),len(SX))
print("Done")


print("Setting up coordinates")
X=min(len(SY[0]),len(SZ))
Y=min(len(SZ[0]),len(SX))
Z=min(len(SX[0]),len(SY))
print("Done")


Faces=[]
Vertices=[]
print("create 3D mesh (this may take a while!")
print("   calculating X Faces")
for x in range(X):
	for z in range(Z):
		if SY[z][x]:
			drinnen=0
			for y in range(Y):
				if SZ[x][y] and SX[y][z]:
					if not drinnen:
						drinnen=1
						Saveface(x,y,z,"Y",drinnen)
				else:
					if drinnen:
						drinnen=0
						Saveface(x,y,z,"Y",drinnen)
			if drinnen:
				Saveface(x,Y,z,"Y",0)
print("   Done\n   calculating Y Faces")
for y in range(Y):
	for x in range(X):
		if SZ[x][y]:
			drinnen=0
			for z in range(Z):
				#print(x,y,z, "/", X,Y,Z)
				if SX[y][z] and SY[z][x]:
					if not drinnen:
						drinnen=1
						Saveface(x,y,z,"Z",drinnen)
				else:
					if drinnen:
						drinnen=0
						Saveface(x,y,z,"Z",drinnen)
			if drinnen:
				Saveface(x,y,Z,"Z",0)
print("   Done\n   calculating Z Faces")
for z in range(Z):
	for y in range(Y):
		if SX[y][z]:
			drinnen=0
			for x in range(X):
				if SY[z][x] and SZ[x][y]:
					if not drinnen:
						drinnen=1
						Saveface(x,y,z,"X",drinnen)
				else:
					if drinnen:
						drinnen=0
						Saveface(x,y,z,"X",drinnen)
			if drinnen:
				Saveface(X,y,z,"X",0)
print("   Done\n")


#print(Vertices,":",Faces)

print("Saving Object file")
file = open("Output.obj","w")

file.write("o 223D\n")

print("   writing Vertices")
for Vertex in Vertices:
	file.write("v "+ str(Vertex[0])+" "+ str(Vertex[1])+" "+ str(Vertex[2])+"\n")
print("   Done\n   writing Faces")
for Face in Faces:
	file.write("f "+ str(Face[0])+" "+ str(Face[1])+" "+ str(Face[2])+" "+ str(Face[3])+"\n")
print("   Done\nDone")