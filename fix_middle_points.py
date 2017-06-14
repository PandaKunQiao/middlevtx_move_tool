import maya.mel as mel
import maya.cmds as cmds
import string

def deal_vtx_list(vtxlist):
    print vtxlist
    col_pos = string.find(vtxlist, ":")
    first_num = vtxlist[string.find(vtxlist, "[")+1:col_pos]
    second_num = vtxlist[col_pos+1:string.find(vtxlist, "]")]
    for index in xrange(int(first_num), int(second_num)+1):
        each_vtx = vtxlist[:(string.find(vtxlist, "["))+1] + str(index) + "]"
        each_position = cmds.pointPosition(each_vtx, w = True)
        each_position[0] = 0.0
        cmds.xform(each_vtx, t = each_position, ws = True)
    
selected_objects = cmds.ls(os = True)
print selected_objects
for each_vtx in selected_objects:
    col_pos = string.find(each_vtx, ":")
    if col_pos != -1:
        deal_vtx_list(each_vtx)
    else:
        print each_position
        each_position = cmds.pointPosition(each_vtx, w = True)
        each_position[0] = 0.0;
        cmds.xform(each_vtx, t = each_position, ws = True)