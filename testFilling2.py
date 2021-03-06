import SurfaceTools

docname = "TestFilling2"

App.newDocument(docname)
App.setActiveDocument(docname)

mydoc = App.getDocument(docname)

import Draft
import Part

### Set Borders ###

p1 = [FreeCAD.Vector(0.0,0.0,3.0),FreeCAD.Vector(3.0,0.0,3.0),FreeCAD.Vector(7.0,0.0,-0.50),FreeCAD.Vector(10.0,0.0,0.0)]
p2 = [FreeCAD.Vector(0.0,0.0,3.0),FreeCAD.Vector(0.0,4.0,3.0),FreeCAD.Vector(0.0,6.0,-0.25),FreeCAD.Vector(0.0,9.0,0.0)]
p3 = [FreeCAD.Vector(10.0,0.0,0.0), FreeCAD.Vector(10.0,6.0,0.0), FreeCAD.Vector(3.3,9.0,0.0), FreeCAD.Vector(0.0,9.0,0.0)]

bs1 = Draft.makeBezCurve(p1,closed=False,support=None)
bs2 = Draft.makeBezCurve(p2,closed=False,support=None)
bs3 = Draft.makeBezCurve(p3,closed=False,support=None)

### Sweep Wires ###

psw1 = [FreeCAD.Vector(0.0,0.0,3.0),FreeCAD.Vector(0.0,-1.0,3.0)]
psw2 = [FreeCAD.Vector(0.0,0.0,3.0),FreeCAD.Vector(-1.0,0.0,3.0)]

sw1 = Draft.makeWire(psw1,closed=False,face=False,support=None)
sw2 = Draft.makeWire(psw2,closed=False,face=False,support=None)

### Constraint Faces ###

import Part
sweep1 = mydoc.addObject('Part::Sweep','Sweep1')
sweep1.Sections=[bs1, ]
sweep1.Spine=(sw1,["Edge1"])
sweep1.Solid=False
sweep1.Frenet=False

sweep2 = mydoc.addObject('Part::Sweep','Sweep2')
sweep2.Sections=[bs2, ]
sweep2.Spine=(sw2,["Edge1"])
sweep2.Solid=False
sweep2.Frenet=False

mydoc.recompute()

### Add Test Feature C0 Continuity ###

test1 = mydoc.addObject('SurfaceTools::Filling', 'test_C0')

### Add Border Curve Constraints ###

#mydoc.test.Border = [(bs1, 'Edge1'), (bw2, 'Edge1'), (bw3, 'Edge1'), (bs4, 'Edge1')]
test1.Border = [(sweep1, 'Edge2'), (sweep2, 'Edge2'), (bs3, 'Edge1')]

### Add Border Face Constraints ###
test1.BFaces = [(sweep1,'Face1'),(sweep2,'Face1'),(0,'Null'),(0,'Null')]
test1.orderB = [0,0,0]

### Set number of iterations ###
test1.NbIter = 5

### Add Test Feature G1 Continuity ###

test2 = mydoc.addObject('SurfaceTools::Filling', 'test_G1')

### Add Border Curve Constraints ###

#mydoc.test.Border = [(bs1, 'Edge1'), (bw2, 'Edge1'), (bw3, 'Edge1'), (bs4, 'Edge1')]
test2.Border = [(sweep1, 'Edge2'), (sweep2, 'Edge2'), (bs3, 'Edge1')]

### Add Border Face Constraints ###
test2.BFaces = [(sweep1,'Face1'),(sweep2,'Face1'),(0,'Null'),(0,'Null')]
test2.orderB = [1,1,0]

### Set number of iterations ###
test2.NbIter = 5

### Add Test Feature G2 Continuity ###

test2 = mydoc.addObject('SurfaceTools::Filling', 'test_G2')

### Add Border Curve Constraints ###

#mydoc.test.Border = [(bs1, 'Edge1'), (bw2, 'Edge1'), (bw3, 'Edge1'), (bs4, 'Edge1')]
test2.Border = [(sweep1, 'Edge2'), (sweep2, 'Edge2'), (bs3, 'Edge1')]

### Add Border Face Constraints ###
test2.BFaces = [(sweep1,'Face1'),(sweep2,'Face1'),(0,'Null'),(0,'Null')]
test2.orderB = [2,2,0]

### Set number of iterations ###
test2.NbIter = 5

mydoc.recompute()
Gui.SendMsgToActiveView("ViewFit")

