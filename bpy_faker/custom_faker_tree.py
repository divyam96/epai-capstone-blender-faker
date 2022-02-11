import bpy
from bpy.types import NodeTree



# Derived from the NodeTree base type, similar to Menu, Operator, Panel, etc.
class CustomFakerTree(NodeTree):
    # Description string
    """A custom node tree type that will show up in the editor type list"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerTreeType'
    # Label for nice name display
    bl_label = "Faker Node Tree"
    # Icon identifier
    bl_icon = 'NODETREE'


# Mix-in class for all custom nodes in this tree type.
# Defines a poll function to enable instantiation.
class FakerTreeNode:
    """A class that will be inherited by all our custom nodes.
       This class ensures that all nodes are associated with 'FakerTreeType'.
    """
    @classmethod
    def poll(cls, ntree):
       return ntree.bl_idname == 'FakerTreeType'
