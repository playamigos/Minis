from maya import cmds
import maya.api.OpenMaya as om


blendShapeNames = cmds.listAttr('asFaceBS.w', m=True)
blendsCount = len(blendShapeNames)

points = []

for x in range(blendsCount):
  cmds.blendShape( 'asFaceBS', edit=True, w=[(x, 1)] )
  # get the mesh vertex position
  sel = cmds.ls(sl=True)
  selection_list = om.MSelectionList ()
  selection_list.add(sel[0])
  dag_path = selection_list.getDagPath (0)
  mfn_mesh = om.MFnMesh(dag_path)
  points.append(mfn_mesh.getPoints())
  
  cmds.blendShape( 'asFaceBS', edit=True, w=[(x, 0)] )
