import time
import string
from math import pi, sin, cos
from direct.showbase import DirectObject 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from panda3d.core import Point3
from panda3d.core import Vec3,TextNode
from pandac.PandaModules import CollisionTraverser, CollisionHandlerEvent
from pandac.PandaModules import CollisionNode, CollisionSphere
from direct.gui.OnscreenText import OnscreenText
#from direct.gui.OnscreenText import OnscreenText
carx=38
cary= -363
car_speed =3
x=0
y= -120
d=0
dis = 20
camx = 18
camy = -410
a=2
k=0
car_def = -6
points = 10
time = 0
Num = 15
cor_ans = 0
count = 20
h=0
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(0,0), align=TextNode.ARight, scale = .7)

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
	global carx,cary,d,cor_ans,count
 
	self.disableMouse()
        self.Truck=[0]*6	
	self.crate=[0]*10
	self.posc=[0]*30
	self.radX=[0]*60
	self.radY=[0]*60
	self.radZ=[0]*60
	self.sX=[0]*10
	self.sY=[0]*10
	self.sZ=[0]*10
	self.flag=[0]*10
	self.ans=[0]*10
	self.inst1 = addInstructions(0.89, "Correct Answer: "+str(cor_ans))
        self.inst2 = addInstructions(0.95, "Time: "+str(time))
        self.inst3 = addInstructions(0.84, "Waste Reamaining "+str(count/2))

	#self.title = addTitle("Recycle Game By : Sandeep Sharma")
	p = 0
	file = open("ans.txt")
	
	for line in file:
		
    		
		#for p in range(30):
			
			
 			#print line
			line = line.split()
			self.ans[p] = str(line[0])
			
			p=p+1
		#	self.posc[p]= int(line)
		#print self.posc[p]		
		#break
	file.close()	
	p = 0
	file = open("sample.txt")
	
	for line in file:
		
    		
		#for p in range(30):
			
			line = line[0:len(line)-1]
 			#print line
			self.posc[p] = int(line)
			
			p=p+1
		#	self.posc[p]= int(line)
		#print self.posc[p]		
		#break
	file.close()
	p=0
	
	file = open("scale.txt")

        for line in file:


                #for p in range(30):

                        line = line.split()

                        #print line
                        self.sX[p] = float(line[0])
			self.sY[p] = float(line[1])
			self.sZ[p] = float(line[2])
			#print self.radY[p]
                        p=p+1
		
	p = 0
	
	
	file = open("rad.txt")

        for line in file:


                #for p in range(30):

                        line = line.split()

                        #print line
                        self.radX[p] = float(line[0])
			self.radY[p] = float(line[1])
			self.radZ[p] = float(line[2])
			#print self.radY[p]
                        p=p+1
			
                #       self.posc[p]= int(line)
                #print self.posc[p]             
                #break
        file.close()

	self.CornField=self.loader.loadModel("cornfield")
        self.CornField.reparentTo(self.render)
        self.CornField.setScale(1000,1000,0)
        self.CornField.setPos(0,0,-8)
	
	self.WM=self.loader.loadModel("WM/Windmill")
        self.WM.reparentTo(self.render)
        self.WM.setScale(2,2,2)
        self.WM.setPos(354,131,0)
	self.WM.setHpr(180,0,0)
		
	self.F1=self.loader.loadModel("Forest/Forest")
        self.F1.reparentTo(self.render)
        self.F1.setScale(0.8,0.5,0.5)
        self.F1.setPos(-338,-164,0)
	self.F1.setHpr(90,0,0)
	
	self.F2=self.loader.loadModel("Forest/Forest")
        self.F2.reparentTo(self.render)
        self.F2.setScale(0.8,0.5,0.5)
        self.F2.setPos(366,-189,0)
	self.F2.setHpr(90,0,0)

	
	self.castle=self.loader.loadModel("castle")
        self.castle.reparentTo(self.render)
        self.castle.setScale(0.6,0.8,0.5)
        self.castle.setPos(-97,-200,0)
	self.castle.setHpr(90,0,0)
	#print self.castle	

	self.church=self.loader.loadModel("church/Church")
        self.church.reparentTo(self.render)
        self.church.setScale(2.5,2.5,1)
        self.church.setPos(90,-200,0)
	self.church.setHpr(180,0,0)

	self.Temple=self.loader.loadModel("Temple/TempleFort")
        self.Temple.reparentTo(self.render)
        self.Temple.setScale(0.06,0.1,0.18)
        self.Temple.setPos(210,-109,0)

	self.house=self.loader.loadModel("BuildingCluster3")
        self.house.reparentTo(self.render)
        self.house.setScale(1.5,1.5,1)
        self.house.setPos(208,86,0)
	
	self.CityHall=self.loader.loadModel("cityhall/CityHall")
        self.CityHall.reparentTo(self.render)
        self.CityHall.setScale(1.5,1.5,1.5)
        self.CityHall.setPos(-188,-84,0)
 	self.CityHall.setHpr(90,0,0)
	
	self.statue=self.loader.loadModel("statue/statue")
        self.statue.reparentTo(self.render)
        self.statue.setScale(4.5,4.5,3.5)
        self.statue.setPos(-191,105,0)
	self.statue.setHpr(-90,0,0)

	self.FarmHouse=self.loader.loadModel("farmhouse/FarmHouse")
        self.FarmHouse.reparentTo(self.render)
        self.FarmHouse.setScale(2.8,3.5,2.5)
        self.FarmHouse.setPos(-66,209,0)

	self.Fence1=self.loader.loadModel("fence/fence")
        self.Fence1.reparentTo(self.render)
        self.Fence1.setScale(70,1,2)
        self.Fence1.setPos(0,-418,0)
	
	self.Fence2=self.loader.loadModel("fence/fence")
        self.Fence2.reparentTo(self.render)
        self.Fence2.setScale(70,1,2)
        self.Fence2.setPos(0,418,0)
	
	self.Fence3=self.loader.loadModel("fence/fence")
        self.Fence3.reparentTo(self.render)
        self.Fence3.setScale(70,1,2)
        self.Fence3.setPos(-418,0,0)
	self.Fence3.setHpr(90,0,0)

	self.Fence4=self.loader.loadModel("fence/fence")
        self.Fence4.reparentTo(self.render)
        self.Fence4.setScale(70,1,2)
        self.Fence4.setPos(418,0,0)
	self.Fence4.setHpr(90,0,0)
		
	self.CityTerrain=self.loader.loadModel("CityTerrain/CityTerrain")
	self.CityTerrain.reparentTo(self.render)
	self.CityTerrain.setScale(0.5,0.5,0.5)
	self.CityTerrain.setPos(0,0,0)

	self.BeachTerrain=self.loader.loadModel("BeachTerrain/BeachTerrain")
        self.BeachTerrain.reparentTo(self.render)
        self.BeachTerrain.setScale(0.5,0.5,0.5)
        self.BeachTerrain.setPos(200,750,0)
	self.BeachTerrain.setHpr(90,0,0)
	
	self.school=self.loader.loadModel("school/school")
        self.school.reparentTo(self.render)
        self.school.setScale(0.056,0.07,0.05)
        self.school.setPos(-162,-348,0)
        self.school.setHpr(90,0,0)
	
	self.car = Actor("bvw-f2004--jeep/jeep",{"walk": "bvw-f2004--jeep/jeep-start"})
        self.car.setScale(0.5, 0.5, 0.5)
        self.car.reparentTo(self.render)
      	self.car.setPos(carx,cary,-2)
	self.car.setHpr(180,0,0)
	#print self.car      
	for l in range(10):
		self.crate[l] = self.loader.loadModel("model"+str(l+1)+"/crate"+str(l+1)+".egg")
        	self.crate[l].setScale(self.sX[l], self.sY[l], self.sZ[l])
        	self.crate[l].reparentTo(self.render)
        	self.crate[l].setPos(self.posc[3*l],self.posc[3*l + 1],2)
        	self.crate[l].setHpr(0,0,0)
		#self.car.loop("walk")

	#self.car.reparentTo(self.render)
        #self.car.setScale(2,2,2)
        #self.car.setPos(carx,cary,-2)
        #self.car.setHpr(0,0,0)
	

	self.museum = self.loader.loadModel("Museum/Museum")
        self.museum.reparentTo(self.render)
        self.museum.setScale(1,2,1.5)
        self.museum.setPos(100,200,0)
        self.museum.setHpr(180,0,0)
	
	self.PalmTree = self.loader.loadModel("PalmTree/palmtree")
        self.PalmTree.reparentTo(self.render)
        self.PalmTree.setScale(2,2,3.5)
        self.PalmTree.setPos(175,200,0)
        self.PalmTree.setHpr(0,0,0)

	
	self.stadium = self.loader.loadModel("Stadium/stadium")
        self.stadium.reparentTo(self.render)
        self.stadium.setScale(0.5,0.5,0.5)
        self.stadium.setPos(13,0,0)
        self.stadium.setHpr(0,0,0)

	self.Junkyard = self.loader.loadModel("Junkyard")
        self.Junkyard.reparentTo(self.render)
        self.Junkyard.setScale(0.2,0.4,0.3)
        self.Junkyard.setPos(150,-650/2 - 25,0)
        self.Junkyard.setHpr(90,0,0)
	
	self.BB1 = self.loader.loadModel("BuildingCluster1")
        self.BB1.reparentTo(self.render)
        self.BB1.setScale(0.5,0.5,1)
        self.BB1.setPos(-100 - 10,650/2 + 20,0)
        self.BB1.setHpr(270,0,0)
	     
        self.BB2 = self.loader.loadModel("BB2/BuildingCluster2")
        self.BB2.reparentTo(self.render)
        self.BB2.setScale(0.5,0.5,1)
        self.BB2.setPos(-60 - 10,650/2 + 20,0)
	self.BB2.setHpr(270,0,0)

	self.BB3 = self.loader.loadModel("BB3/BuildingCluster3")
        self.BB3.reparentTo(self.render)
        self.BB3.setScale(0.5,0.5,1)
        self.BB3.setPos(-140 - 10,650/2 + 20,0)
        self.BB3.setHpr(270,0,0)

	self.BB4 = self.loader.loadModel("BB4/BuildingCluster4")
        self.BB4.reparentTo(self.render)
        self.BB4.setScale(0.5,0.5,1)
        self.BB4.setPos(-25 - 10,650/2 + 20,0)
	self.BB4.setHpr(270,0,0)

	self.BB5 = self.loader.loadModel("BB5/BuildingCluster5")
        self.BB5.reparentTo(self.render)
        self.BB5.setScale(0.5,0.5,1)
        self.BB5.setPos(-190 - 10,650/2 + 20,0)
	self.BB5.setHpr(270,0,0)

	self.BS = self.loader.loadModel("BS/blue_sky_sphere")
        self.BS.reparentTo(self.render)
        self.BS.setScale(1,1,1)
        self.BS.setPos(-180,0,0)
	
	self.flagMain = self.loader.loadModel("Flag/flag")
        self.flagMain.setScale(0.3,0.3,0.3)
        self.flagMain.reparentTo(self.render)
	self.flagMain.setPos(carx-20,cary,10)
	print self.flagMain

	for i in range (6):
		self.Truck[i] = self.loader.loadModel("bvw-f2004--fireengine/fireengine")
        	self.Truck[i].reparentTo(self.render)
        	self.Truck[i].setScale(2,2,2)
        	##self.Truck[i].setPos(180,0,0)

	#Create the four lerp intervals needed to walk back and forth
	self.setTruck()
		
	#self.City = self.loader.loadModel("City/course2")
        #self.City.reparentTo(self.render)
        #self.City.setScale(2.5,2.5,2.5)
        #self.City.setPos(500,0,0)

	self.accept('arrow_down',self.moved,[0])
        self.accept('arrow_up',self.move,[0])
        self.accept("arrow_left",self.change_dc,[0])
        self.accept("arrow_right",self.change_da,[0])
	
	
	self.accept('arrow_down-up',self.moved,[2])
	self.accept('arrow_up-up',self.move,[2])
	#self.accept("arrow_left-up",self.change_dc,[2])
        #self.accept("arrow_right-up",self.change_da,[2])

	self.accept('arrow_down-repeat',self.moved,[1])
	self.accept('arrow_up-repeat',self.move,[1])
	self.accept("arrow_left-repeat",self.change_dc,[1])
	self.accept("arrow_right-repeat",self.change_da,[1])
	
	base.cTrav = CollisionTraverser()
	
	self.collHandEvent = CollisionHandlerEvent()
        self.collHandEvent.addInPattern('into-%in')
        self.collHandEvent.addOutPattern('outof-%in')
	self.collCount = 0
	sColl = self.initCollisionSphere(self.car,1,1,1, True)
	base.cTrav.addCollider(sColl[0], self.collHandEvent)


	self.accept('into-' + sColl[1] , self.collide)
        #self.accept('outof-' + sColl[1], self.collide4)
	i=0
	for child in render.getChildren():	
		if child != self.CornField and child != camera and child != self.CityTerrain and child!= self.BeachTerrain and child != self.BS and child != self.Fence1 and child != self.Fence2 and child != self.Fence3 and child != self.Fence4:
			#print child
			tColl = self.initCollisionSphere(child,self.radX[i],self.radY[i],self.radZ[i], True)
			base.cTrav.addCollider(tColl[0], self.collHandEvent)
 			#print i
			i=i+1
			
        # Accept the events sent by the collisions.
        		self.accept('into-' + tColl[1] , self.collide)
	for l in range(10):
                self.flag[l] = self.loader.loadModel("Flag/flag")
                self.flag[l].setScale(0.3,0.3,0.3)
                self.flag[l].reparentTo(self.render)

                self.flag[l].setPos(self.posc[3*l],self.posc[3*l + 1],10)


#       	self.accept( 'into-' + sColl[1], self.collide)
	 #self.accept('outof-' + tColl[1], self.collide2)
#	print carx,cary
#	cs = CollisionSphere(0, 0, 0, 10)
#	fromObject = self.car.attachNewNode(CollisionNode('cnode'))
#	fromObject.node().addSolid(cs)
#	fromObject.show()
#	pusher = CollisionHandlerPusher()
#	pusher.addCollider(fromObject, self.car)
#	base.cTrav = CollisionTraverser()
#	base.cTrav.addCollider(fromObject, pusher)
	
	self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
	
    def collide(self,collEntry):
	global carx,cary,car_def,a,Num,count
	#print "Collide"

	#print collEntry.getFromNodePath().getParent() 
	#for objectc in collEntry:
	for l in range(10):
		#print collEntry.getFromNodePath().getParent()
		if collEntry.getIntoNodePath().getParent() == self.crate[l] :
			collEntry.getIntoNodePath().getParent().remove()
			#print "Baba"
			Num = l
			count = count - 1
			self.flag[l].hide()
			self.Game_Point()
	if str(collEntry.getIntoNodePath().getParent()) ==  "render/flag.egg" and count == 0 and str(collEntry.getFromNodePath().getParent()) == "render/jeepNman_loop_baked":
		#print "here"
		self.GameOver()

   	if str(collEntry.getIntoNodePath().getParent()) == "render/jeepNman_loop_baked"  or str(collEntry.getFromNodePath().getParent()) == "render/jeepNman_loop_baked":
		
		if a==0:

			if self.car.getH() == 45:

                		carx =  carx + car_def
                		cary =  cary - car_def
        		if self.car.getH() == 90:
                		carx = carx + car_def
 
	        	if self.car.getH() == 135:
        	        	carx = carx + car_def
                		cary = cary + car_def
        		if self.car.getH() == 180:
                		cary=cary + car_def
 
		        if self.car.getH() == 225:
        		        carx = carx - car_def
                		cary = cary + car_def
 
        		if self.car.getH() == 270:
                		carx = carx - car_def
 
	        	if self.car.getH() == 315:
        	        	carx =carx - car_def
                		cary= cary - car_def
 
        		if self.car.getH() == 0:
                		cary = cary - car_def
 		if a==1:
			car_def= -1*car_def
			if self.car.getH() == 45:

                        	carx =  carx + car_def
                        	cary =  cary - car_def
                	if self.car.getH() == 90:
                        	carx = carx + car_def

              		if self.car.getH() == 135:
                        	carx = carx + car_def
                        	cary = cary + car_def
                	if self.car.getH() == 180:
                        	cary=cary + car_def

                	if self.car.getH() == 225:
                        	carx = carx - car_def
                        	cary = cary + car_def

                	if self.car.getH() == 270:
                        	carx = carx - car_def

                	if self.car.getH() == 315:
                        	carx =carx - car_def
                      		cary= cary - car_def

                	if self.car.getH() == 0:
                        	cary = cary - car_def

			car_def= -1*car_def
	
#    def collide2(self,collEntry):
#	
#    def collide3(self,collEntry):
#	global carx , cary
#	carx=carx-2
#	cary=cary-2
#    def collide4(self,collEntry):
#	print 4

    def initCollisionSphere(self, obj,setX,setY,setZ, show=False):
        # Get the size of the object for the collision sphere.
        bounds = obj.getChild(0).getBounds()
        center = bounds.getCenter()
        radius = bounds.getRadius() * 0.6
 
        # Create a collision sphere and name it something understandable.
        collSphereStr = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
        self.collCount += 1
	self.accept('arrow_down',self.moved,[0])
        self.accept('arrow_up',self.move,[0])
        cNode = CollisionNode(collSphereStr)
#	cNode.setScale(3,3,3)
        cNode.addSolid(CollisionSphere(center, radius))
 
        cNodepath = obj.attachNewNode(cNode)
	cNodepath.setScale(setX,setY,setZ)
	#cNodepath.show()
        
 
        # Return a tuple with the collision node and its corrsponding string so
        # that the bitmask can be set.
        return (cNodepath, collSphereStr)	

    def moved(self,i):
	global carx,cary,camx,camy,dis,a
	#print "moved"
	a=1
	if i ==0:
		#print "Hello"
		self.car.loop("walk") 
	if i==2:
		self.car.stop("walk")
	#print "hello",self.car.getH()	
	#print base.camera.getH()
	if carx> -410 and carx<410 and cary>-410 and cary<410:
		if self.car.getH() == 45:

			carx =	carx - car_speed
    			cary =  cary + car_speed
			camx =  carx - dis
			camy = cary  + dis
		if self.car.getH() == 90:
			carx = carx - car_speed
			camx = carx - dis
		if self.car.getH() == 135:
			carx = carx - car_speed
			cary = cary - car_speed
			camx = carx - dis
			camy = cary -dis
		if self.car.getH() == 180:
			cary=cary - car_speed
			camy = cary - dis
		if self.car.getH() == 225:
			carx = carx + car_speed
			cary = cary - car_speed
			camx=carx + dis
			camy=cary - dis
		if self.car.getH() == 270:
			carx = carx + car_speed
			camx =carx + dis
		if self.car.getH() == 315:
			carx =carx +car_speed
			cary= cary +car_speed
			camx=carx + dis
			camy =cary +dis
		if self.car.getH() == 0:
			cary = cary + car_speed
			camy = cary + dis
	
        
	else:
            if carx <= -410:
                carx = carx-1
            if carx >= 410:
                carx = carx+1               
            if cary <= -410:
                cary = cary-1
            if cary >= 410:       
                cary = cary+1        
    def move(self,i):
	global carx,cary,camx,camy,dis,a
	a=0
#	print "move"
#	print carx,cary
	if i ==0:
                
                self.car.loop("walk")
        if i==2:
                self.car.stop("walk")

        #print "hello",self.car.getH()
        #print base.camera.getH()
	if carx>-410 and carx<410 and cary>-410 and cary<410:
        	if self.car.getH() == 45:

                	carx =  carx + car_speed
                	cary =  cary - car_speed
               		camx =  carx + dis
                	camy = cary  - dis
        	if self.car.getH() == 90:
                	carx = carx + car_speed
               	        camx = carx + dis
        	if self.car.getH() == 135:
                	carx = carx + car_speed
                	cary = cary + car_speed
                	camx = carx + dis
               	        camy = cary +dis
        	if self.car.getH() == 180:
                	cary=cary + car_speed
                	camy = cary + dis
        	if self.car.getH() == 225:
                	carx = carx - car_speed
                	cary = cary + car_speed
                	camx=carx - dis
                	camy=cary + dis
        	if self.car.getH() == 270:
                	carx = carx - car_speed
                	camx =carx - dis
        	if self.car.getH() == 315:
                	carx =carx - car_speed
                	cary= cary - car_speed
                	camx=carx - dis
                	camy =cary - dis
        	if self.car.getH() == 0:
                	cary = cary - car_speed
               	 	camy = cary - car_speed	    
	else:
            if carx<=-410:
                carx = carx+1
            if carx>=410:
                carx= carx-1               
            if cary<=-410:
                cary = cary+1
            if cary>=410:       
                cary=cary -1        
#	self.car.loop("walk")

    def change_dc(self,i):
	global d
	#if i ==0:
        #        print "Hello"
        #        self.car.loop("walk")
        #if i==2:
        #        self.car.stop("walk")

	d=d + 45
	d=d % 360
	

	   		
 
    def change_da(self,i):
        global d
	#if i ==0:
        #        print "Hello"
        #        self.car.loop("walk")
        #if i==2:
        #        self.car.stop("walk")

	d = d - 45
        d=d%360
	
        #for j in range(9):
        #	d=d - 5
	#
        #	d=d % 360
	#	self.car.setHpr(d , 0 , 0)
	#	time.sleep(0.1)
	#messenger.send('arrow_up-repeat')	

    def spinCameraTask(self, task):
	global time,carx,cary,d,dis,camx,camy,count,cor_ans
	time = int(task.time)
	#r = d * (pi / 180.0)
	#print carx,cary
	if self.car.getH() == 45:

                camx =  carx - dis
                camy = cary  + dis
        if self.car.getH() == 90:
                camx = carx - 1.41*dis
		camy = cary
        if self.car.getH() == 135:
                camx = carx - dis
                camy = cary -dis
        if self.car.getH() == 180:
                camy = cary - 1.41*dis
		camx =carx
        if self.car.getH() == 225:
                camx=carx + dis
                camy=cary - dis
        if self.car.getH() == 270:
                camx =carx + 1.41*dis
		camy=cary
        if self.car.getH() == 315:
                camx=carx + dis
                camy =cary +dis
        if self.car.getH() == 0:
                camy = cary + 1.41*dis
		camx=carx
	if h==0:
		self.inst1.destroy()
		self.inst2.destroy()
		self.inst3.destroy()
		self.inst1 = addInstructions(0.89, "Correct Answer: "+str(cor_ans))
		self.inst2 = addInstructions(0.95, "Time: "+str(time))
		self.inst3 = addInstructions(0.84, "Waste Reamaining "+str(count/2))

	self.car.setPos(carx,cary,0)
	self.car.setHpr(d , 0 , 0)
	base.camera.setPos(camx ,camy,5)
	base.camera.setHpr(d + 180, 0 , 0)
	
	#base.camera.setPos(0,0,1700)
	#base.camera.setHpr(0, -90 , 0)

	return Task.cont	
#	base.camera.setPos(0,-40,3)
#	return Task.cont
    def setTruck(self):
	pandaPosInterval01= self.Truck[0].posInterval(11,Point3(18,138,0), startPos=Point3(21,390,0))
        pandaPosInterval02= self.Truck[0].posInterval(5,Point3(140,132,0), startPos=Point3(18,138,0))
        pandaPosInterval03= self.Truck[0].posInterval(10,Point3(140,-123,0), startPos=Point3(140,132,0))
        pandaPosInterval04= self.Truck[0].posInterval(5,Point3(-7,-126,0), startPos=Point3(140,-123,0))
        pandaPosInterval05= self.Truck[0].posInterval(11,Point3(-10,-399,0), startPos=Point3(-7,-126,0))
        #pandaPosInterval6=self.Truck[0].posInterval(1,Point3(21,390,0),startPos=Point3(-10,-399,0)
        pandaHprInterval00= self.Truck[0].hprInterval(1,Point3(180,0,0), startHpr=Point3(0,0,0))
	pandaHprInterval01= self.Truck[0].hprInterval(3,Point3(-90,0,0), startHpr=Point3(180,0,0))
        pandaHprInterval02= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(-90,0,0))
        pandaHprInterval03= self.Truck[0].hprInterval(3,Point3(90,0,0), startHpr=Point3(180,0,0))
        pandaHprInterval04= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(90,0,0))
        #pandaHprInterval5= self.Truck[0].hprInterif collEntry.getIntoNodePath().getParent() == self.crate[l]:val(3,Point3(180,0,0), startHpr=Point3(0,0,0))


#Create and play the sequence that coordinates the intervals
        pandaPace0 = Sequence(pandaHprInterval00,pandaPosInterval01, pandaHprInterval01,
        pandaPosInterval02, pandaHprInterval02,pandaPosInterval03,pandaHprInterval03,pandaPosInterval04,pandaHprInterval04,pandaPosInterval05, name = "pandaPace0")
        pandaPace0.loop()        
 
	pandaPosInterval11= self.Truck[1].posInterval(11,Point3(-126,14,0), startPos=Point3(-411,14,0))
        pandaPosInterval12= self.Truck[1].posInterval(5,Point3(-117,145,0), startPos=Point3(-126,14,0))
        pandaPosInterval13= self.Truck[1].posInterval(10,Point3(148,130,0), startPos=Point3(-117,145,0))
        pandaPosInterval14= self.Truck[1].posInterval(5,Point3(145,-5,0), startPos=Point3(148,130,0))
        pandaPosInterval15= self.Truck[1].posInterval(11,Point3(394,-8,0), startPos=Point3(145,-5,0))
        #pandaPosInterval6=self.Truck[0].posInterval(1,Point3(21,390,0),startPos=Point3(-10,-399,0)
	pandaHprInterval10= self.Truck[1].hprInterval(1,Point3(-90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval11= self.Truck[1].hprInterval(3,Point3(0,0,0), startHpr=Point3(-90,0,0))
        pandaHprInterval12= self.Truck[1].hprInterval(3,Point3(-90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval13= self.Truck[1].hprInterval(3,Point3(180,0,0), startHpr=Point3(-90,0,0))
        pandaHprInterval14= self.Truck[1].hprInterval(3,Point3(-90,0,0), startHpr=Point3(180,0,0))
        #pandaHprInterval5= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(0,0,0))


#Create and play the sequence that coordinates the intervals
        pandaPace1 = Sequence(pandaHprInterval10,pandaPosInterval11, pandaHprInterval11,
        pandaPosInterval12, pandaHprInterval12,pandaPosInterval13,pandaHprInterval13,pandaPosInterval14,pandaHprInterval14,pandaPosInterval15, name = "pandaPace1")
        pandaPace1.loop()
	
	pandaPosInterval21= self.Truck[2].posInterval(11,Point3(-9,-144,0), startPos=Point3(-6,-358,0))
        pandaPosInterval22= self.Truck[2].posInterval(5,Point3(-129,-137,0), startPos=Point3(-9,-144,0))
        pandaPosInterval23= self.Truck[2].posInterval(10,Point3(-129,142,0), startPos=Point3(-129,-137,0))
        pandaPosInterval24= self.Truck[2].posInterval(5,Point3(5,145,0), startPos=Point3(-129,142,0))
        pandaPosInterval25= self.Truck[2].posInterval(11,Point3(20,395,0), startPos=Point3(5,145,0))
        #pandaPosInterval6=self.Truck[0].posInterval(1,Point3(21,390,0),startPos=Point3(-10,-399,0)
	pandaHprInterval20= self.Truck[2].hprInterval(1,Point3(0,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval21= self.Truck[2].hprInterval(3,Point3(90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval22= self.Truck[2].hprInterval(3,Point3(0,0,0), startHpr=Point3(90,0,0))
        pandaHprInterval23= self.Truck[2].hprInterval(3,Point3(-90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval24= self.Truck[2].hprInterval(3,Point3(0,0,0), startHpr=Point3(-90,0,0))
        #pandaHprInterval5= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(0,0,0))


#Create and play the sequence that coordinates the intervals
        pandaPace2 = Sequence(pandaHprInterval20,pandaPosInterval21, pandaHprInterval21,
        pandaPosInterval22, pandaHprInterval22,pandaPosInterval23,pandaHprInterval23,pandaPosInterval24,pandaHprInterval24,pandaPosInterval25, name = "pandaPace2")
        pandaPace2.loop()
	
	pandaPosInterval31= self.Truck[3].posInterval(11,Point3(150,-18,0), startPos=Point3(408,-18,0))
        pandaPosInterval32= self.Truck[3].posInterval(5,Point3(147,-135,0), startPos=Point3(150,-18,0))
        pandaPosInterval33= self.Truck[3].posInterval(10,Point3(-120,-138,0), startPos=Point3(147,-135,0))
        pandaPosInterval34= self.Truck[3].posInterval(5,Point3(-123,-6,0), startPos=Point3(-120,-138,0))
        pandaPosInterval35= self.Truck[3].posInterval(11,Point3(-396,10,0), startPos=Point3(-123,-6,0))
        #pandaPosInterval6=self.Truck[0].posInterval(1,Point3(21,390,0),startPos=Point3(-10,-399,0)
	pandaHprInterval30= self.Truck[3].hprInterval(1,Point3(90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval31= self.Truck[3].hprInterval(3,Point3(180,0,0), startHpr=Point3(90,0,0))
        pandaHprInterval32= self.Truck[3].hprInterval(3,Point3(90,0,0), startHpr=Point3(180,0,0))
        pandaHprInterval33= self.Truck[3].hprInterval(3,Point3(0,0,0), startHpr=Point3(90,0,0))
        pandaHprInterval34= self.Truck[3].hprInterval(3,Point3(90,0,0), startHpr=Point3(0,0,0))
        #pandaHprInterva5= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(0,0,0))


#Create and play the sequence that coordinates the intervals
        pandaPace4 = Sequence(pandaHprInterval30,pandaPosInterval31, pandaHprInterval31,
        pandaPosInterval32, pandaHprInterval32,pandaPosInterval33,pandaHprInterval33,pandaPosInterval34,pandaHprInterval34,pandaPosInterval35, name = "pandaPace4")
        pandaPace4.loop()
	
	pandaPosInterval41= self.Truck[4].posInterval(12,Point3(298,-282,0), startPos=Point3(-276,-282,0))
        pandaPosInterval42= self.Truck[4].posInterval(12,Point3(286,280,0), startPos=Point3(298,-282,0))
        pandaPosInterval43= self.Truck[4].posInterval(12,Point3(-268,280,0), startPos=Point3(286,280,0))
        pandaPosInterval44= self.Truck[4].posInterval(12,Point3(-276,-282,0), startPos=Point3(-268,280,0))
        
        #pandaHprInterval30= self.Truck[3].hprInterval(1,Point3(90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval41= self.Truck[4].hprInterval(3,Point3(-90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval42= self.Truck[4].hprInterval(3,Point3(0,0,0), startHpr=Point3(-90,0,0))
        pandaHprInterval43= self.Truck[4].hprInterval(3,Point3(90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval44= self.Truck[4].hprInterval(3,Point3(180,0,0), startHpr=Point3(90,0,0))
        #pandaHprInterva5= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(0,0,0))


#Create and play the sequence that coordinates the intervals
        pandaPace5 = Sequence(pandaHprInterval41,pandaPosInterval41, pandaHprInterval42,
        pandaPosInterval42, pandaHprInterval43,pandaPosInterval43,pandaHprInterval44,pandaPosInterval44, name = "pandaPace5")
        pandaPace5.loop()
	
	pandaPosInterval51= self.Truck[5].posInterval(12,Point3(-268,280,0), startPos=Point3(286,280,0))
        pandaPosInterval52= self.Truck[5].posInterval(12,Point3(-276,-282,0), startPos=Point3(-268,280,0))
        pandaPosInterval53= self.Truck[5].posInterval(12,Point3(298,-282,0), startPos=Point3(-276,-282,0))
        pandaPosInterval54= self.Truck[5].posInterval(12,Point3(286,280,0), startPos=Point3(298,-282,0))
        #pandaPosInterval55= self.Truck[5].posInterval(13,Point3(-396,10,0), startPos=Point3(-123,-6,0))
        #pandaPosInterval6=self.Truck[0].posInterval(1,Point3(21,390,0),startPos=Point3(-10,-399,0)
        #pandaHprInterval50= self.Truck[5].hprInterval(1,Point3(90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval51= self.Truck[5].hprInterval(3,Point3(90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval52= self.Truck[5].hprInterval(3,Point3(180,0,0), startHpr=Point3(90,0,0))
        pandaHprInterval53= self.Truck[5].hprInterval(3,Point3(-90,0,0), startHpr=Point3(0,0,0))
        pandaHprInterval54= self.Truck[5].hprInterval(3,Point3(0,0,0), startHpr=Point3(-90,0,0))
        #pandaHprInterva5= self.Truck[0].hprInterval(3,Point3(180,0,0), startHpr=Point3(0,0,0))


#Create and play the sequence that coordinates the intervals
        pandaPace6 = Sequence(pandaHprInterval51,pandaPosInterval51, pandaHprInterval52,
        pandaPosInterval52, pandaHprInterval53,pandaPosInterval53,pandaHprInterval54,pandaPosInterval54, name = "pandaPace6")
        pandaPace6.loop()
	
    def Game_Point(self):
	
		
	self.ignore("arrow_down")	
	self.ignore("arrow_up")
	self.ignore("arrow_down-repeat")
	self.ignore("arrow_up-repeat")
	#self.text1 = addInstructions(0.5,"Is this Recyclable")
	self.text1 = TextNode('t1')
	self.text1.setText("is This  Recyclable")
	self.text1.setTextColor(0,0,0,1)
	self.textNodePath1 = aspect2d.attachNewNode(self.text1)
	self.textNodePath1.setScale(0.07)
	self.textNodePath1.setPos(-0.1,-0.1,0.1) 	
	#text1.setTextColor(1,1,1)
	self.text1.setFrameColor(1, 0, 0, 1)
	self.text1.setFrameAsMargin(0.2, 0.2, 0.1, 0.1)	

	self.text2 = TextNode('t2')
        self.text2.setText("Y/N")
        self.text2.setTextColor(0,0,0,1)
	self.textNodePath2 = aspect2d.attachNewNode(self.text2)
        self.textNodePath2.setScale(0.07)
        self.textNodePath2.setPos(0,0,0) 
	#textNodePath2.setTextColor(1,1,1) 
        self.text2.setFrameColor(1, 0, 0, 1)
        self.text2.setFrameAsMargin(0.2, 0.2, 0.1, 0.1)
	self.accept('y',self.answer,[0])
        self.accept('n',self.answer,[1])
  
    def answer(self,n):
	global Num,cor_ans
	#print self.ans[Num]
	self.accept('arrow_down',self.moved,[0])
        self.accept('arrow_up',self.move,[0])
	self.accept('arrow_down-repeat',self.moved,[1])
	self.accept('arrow_up-repeat',self.move,[1])
	aspect2d.getChildren().detach()
	if n == 0:
		if self.ans[Num] == 'Y':
			cor_ans = cor_ans + 1
	if n == 1:
		if self.ans[Num] == 'N':
			#print "Correct"
			cor_ans = cor_ans + 1
	self.ignore('y')
	self.ignore('n')

	#print "Hello"
    def GameOver(self):
	
	global cor_ans,time,h
	h=1
	#print time
	for x in self.render.getChildren():
		x.detachNode()
	self.inst1.destroy()
	self.inst2.destroy()
	self.inst3.destroy()
	
	self.text3 = TextNode('t1')
	self.text3.setText("Game Over ")
	self.text3.setTextColor(1,0,0,1)
	self.textNodePath3 = aspect2d.attachNewNode(self.text3)
	self.textNodePath3.setScale(0.1)
	self.textNodePath3.setPos(-0.1,-0.1,0.2) 	
	#text1.setTextColor(1,1,1)
	#self.text3.setFrameColor(1, 0, 0, 1)
	#self.text3.setFrameAsMargin(0.2, 0.2, 0.1, 0.1)	
	self.text5 = TextNode('t1')
	self.text5.setText("Time Taken: "+ str(time))
	self.text5.setTextColor(1,0,0,1)
	self.textNodePath5 = aspect2d.attachNewNode(self.text5)
	self.textNodePath5.setScale(0.1)
	self.textNodePath5.setPos(-0.1,-0.1,0)
	
	self.text6 = TextNode('t1')
	self.text6.setText("correct answer: " + str(cor_ans))
	self.text6.setTextColor(1,0,0,1)
	self.textNodePath6 = aspect2d.attachNewNode(self.text6)
	self.textNodePath6.setScale(0.1)
	self.textNodePath6.setPos(-0.1,-0.1,-0.2)

	self.text4 = TextNode('t2')
        self.text4.setText("Score: " + str(5000/time + (cor_ans * 10)))
        self.text4.setTextColor(1,0,0,1)
	self.textNodePath4 = aspect2d.attachNewNode(self.text4)
        self.textNodePath4.setScale(0.1)
        self.textNodePath4.setPos(-0.1,-0.1,-0.4) 
	#textNodePath2.setTextColor(1,1,1) 
        #self.text4.setFrameColor(1, 0, 0, 1)
        #self.text4.setFrameAsMargin(0.2, 0.2, 0.1, 0.1)
	
	#print "Game Over"
app = MyApp()
app.run()
