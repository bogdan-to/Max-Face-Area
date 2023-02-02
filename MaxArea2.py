import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs
from ClassMaxBrepArea import*


obj = rs.GetObjects("Select plates:")




for i in obj:
    
    arin = MaxBrepArea(i)
    area, index = arin.MaxAreaIndex()
    
    print (area)
    print (index)