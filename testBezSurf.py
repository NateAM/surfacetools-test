import SurfaceTools

docname = "TestBezSurf"
ftp = 1 ### Change to test different fill types (1, 2, or 3 accepted)

App.newDocument(docname)
App.setActiveDocument(docname)

mydoc = App.getDocument(docname)

import Draft
import Part

### Set Borders ###

p1 = [FreeCAD.Vector(0.0,0.0,3.0),FreeCAD.Vector(3.0,0.0,3.0),FreeCAD.Vector(7.0,0.0,-0.50),FreeCAD.Vector(10.0,0.0,0.0)]
p2 = [FreeCAD.Vector(10.0,0.0,0.0), FreeCAD.Vector(10.0,6.0,0.0), FreeCAD.Vector(3.3,9.0,0.0), FreeCAD.Vector(0.0,9.0,0.0)]
p3 = [FreeCAD.Vector(0.0,9.0,0.0),FreeCAD.Vector(0.0,6.0,-0.25),FreeCAD.Vector(0.0,4.0,3.0),FreeCAD.Vector(0.0,0.0,3.0)]


bs1 = Draft.makeBezCurve(p1,closed=False,support=None)
bs2 = Draft.makeBezCurve(p2,closed=False,support=None)
bs3 = Draft.makeBezCurve(p3,closed=False,support=None)

mydoc.recompute()

### Add Test Feature Three sides ###

test2 = mydoc.addObject('SurfaceTools::BezSurf', 'three_curves')

### Add Bezier Curves to test ###

#mydoc.test.Border = [(bs1, 'Edge1'), (bw2, 'Edge1'), (bw3, 'Edge1'), (bs4, 'Edge1')]
test2.aBezList = [(bs1, 'Edge1'), (bs2, 'Edge1'), (bs3, 'Edge1')]

### Set fill type ###
test2.filltype = ftp

mydoc.recompute()
Gui.SendMsgToActiveView("ViewFit")

