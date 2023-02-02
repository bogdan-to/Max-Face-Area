import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs

#Finds face with maximum area in brep
#Class call: 
#arin = MaxBrepArea(brep_guid)
#area, index = arin.MaxAreaIndex()

class MaxBrepArea:
    
    def __init__(self, _brep):
        self.brep = _brep
     
    def MaxAreaIndex(self):
        
        if rs.ObjectType(self.brep) != 1073741824 and rs.ObjectType(self.brep) !=16:
            print ("Selected object is not polysurface.")
            return
    
        maxArea = 0
        brepFaces = rs.coercebrep(self.brep)
        for i in brepFaces.Faces:
          area = Rhino.Geometry.AreaMassProperties.Compute(i).Area
          if area > maxArea:
             maxArea = area
             index = i.ComponentIndex().Index
          else:continue
        return(maxArea, index)