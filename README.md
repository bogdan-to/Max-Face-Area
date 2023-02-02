# Max-Face-Area
Python script for Rhinoceros. Finds face on brep with maximum area.

ClassMaxBrepArea.py:
  Finds face with maximum area in brep and returns area and index of that face
  arin = MaxBrepArea(brep_guid)
  area, index = arin.MaxAreaIndex()
  
MaxArea2.py:
  contains selection of breps and uses ClassMaxBrepArea to 
  print maximum area of face in brep for all selected breps
