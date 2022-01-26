from maya import cmds
import maya.api.OpenMaya as om
# set the mesh vertex position
sel = cmds.ls(sl=True)
# get the dag path
selection_list = om.MSelectionList ()
selection_list.add(sel[0])
dag_path = selection_list.getDagPath (0)
# creating Mfn Mesh
mfn_mesh = om.MFnMesh(dag_path)
mfn_mesh.setPoints(points)
