from maya import cmds
import maya.api.OpenMaya as om
import maya.mel as mel

blendShapeNames = cmds.listAttr('asFaceBS.w', m=True)
blendsCount = len(blendShapeNames)

for x in range(blendsCount):
  cmds.blendShape( 'asFaceBS', edit=True, w=[(x, 1)] )
  
  cmds.sculptTarget( 'asFaceBS', e=True, t=x )
  
  # set the mesh vertex position
  sel = cmds.ls(sl=True)
  selection_list = om.MSelectionList ()
  selection_list.add(sel[0])
  dag_path = selection_list.getDagPath (0)
  mfn_mesh = om.MFnMesh(dag_path)
  mfn_mesh.setPoints(points[x])
  
  cmds.sculptTarget( 'asFaceBS', e=True, t=-1 )
  
  cmds.blendShape( 'asFaceBS', edit=True, w=[(x, 0)] )
