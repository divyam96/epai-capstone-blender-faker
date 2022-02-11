import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
from .nodes import *
from .custom_faker_tree import CustomFakerTree

bl_info = {
    "name": "BpyFaker",
    "author": "Divyam Malay Shah",
    "version": (1, 0, 0),
    "blender": (2, 93, 1),
    "location": "Faker Node Tree",
    "description": "Faker Node Editor",
    "category": "CustomFaker"
}

classes = []


class Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout


class FakerNodeCategory(NodeCategory):
    """Custom categories in the the Faker Node Tree editor."""

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'FakerTreeType'


# all categories in a list
node_categories = [
    # identifier, label, items list
    FakerNodeCategory('INPUTNODES', "Input Nodes", items=[
        # our basic node
        NodeItem("IntInputNodeType"),
    ]),
    FakerNodeCategory('FAKERNODES', "Faker Nodes", items=[

        NodeItem("FakerBarcodeNodeType", label="Fake Barcode"),
        NodeItem("FakerRGBColorsNodeType", label="Fake Colors No"),
        NodeItem("FakerCompanyNodeType", label="Fake Company No"),
        NodeItem("FakerCreditCardNodeType", label="Fake Credit Card No"),
        NodeItem("FakerEmailNodeType", label="Fake Email Id"),
        NodeItem("FakerGeoNodeType", label="Fake Geo lat Long"),
        NodeItem("FakerLicenseNodeType", label="Fake Auto License"),
        NodeItem("FakerPersonNodeType", label="Fake Person Name"),
        NodeItem("FakerPhoneNodeType", label="Fake Phone No"),
        NodeItem("FakerUserAgentNodeType", label="Fake User Agent")

    ])
]

classes = (
    CustomFakerTree,
    CustomIntSocket,
    IntInputNode,
    FakerPhoneNode,
    FakerBarcodeNode,
    FakerColorsNode,
    FakerCompanyNode,
    FakerCreditCardNode,
    FakerEmailNode,
    FakerGeoNode,
    FakerLicenseNode,
    FakerPersonNode,
    FakerUserAgentNode
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('CUSTOM_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('CUSTOM_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
