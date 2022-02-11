import bpy
import pickle
import random

from bpy.types import NodeTree, Node, NodeSocket
from .custom_faker_tree import FakerTreeNode
from .config import FAKER_DATA_PICKLE_PATH


with open(FAKER_DATA_PICKLE_PATH, 'rb') as handle:
    faker_dict = pickle.load(handle)


# Custom socket type
class CustomIntSocket(NodeSocket):
    # Description string
    """Custom Integer node socket type"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'IntInputSocketType'
    # Label for nice name display
    bl_label = "Custom Node Socket"

    def update_custom_socket(self, context):
        """Ensuring Nodes are updated as socket properties change."""
        self.node.update()

    my_int_prop: bpy.props.IntProperty(default=1, update=update_custom_socket)

    # Optional function for drawing the socket input value
    def draw(self, context, layout, node, text):
        layout.prop(self, "my_int_prop", text=text)

    # Socket color
    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


# Derived from the Node base type.
class IntInputNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom input node that generates Integers to pass onto other nodes"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'IntInputNodeType'
    # Label for nice name display
    bl_label = "Integer Input"
    # Icon identifier
    bl_icon = 'LIGHT_DATA'

    def update_input_node_attribute(self, context):
        self.outputs[0].my_int_prop = self.my_int_prop

    # === Custom Properties ===
    # These work just like custom properties in ID data blocks
    # Extensive information can be found under
    # http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Properties
    my_int_prop: bpy.props.IntProperty(default=1, update=update_input_node_attribute)

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.outputs.new('IntInputSocketType', "User Input")

    #        self.outputs[0].default_value = self.my_int_prop

    # Copy funoutputsction to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        # Check if the out node is linked, if True then copy values to outgoing node
        if (self.outputs[0].is_linked) and (len(self.outputs[0].links) != 0):
            self.outputs[0].links[0].to_socket.my_int_prop = self.outputs[0].my_int_prop


# Derived from the Node base type.
class FakerPhoneNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake phone numbers"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerPhoneNodeType'
    # Label for nice name display
    bl_label = "Fake Phone No"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['phone_numbers'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerColorsNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake RGB color values"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerRGBColorsNodeType'
    # Label for nice name display
    bl_label = "Fake Color Values"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['rgb_colors'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerBarcodeNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake barcode numbers"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerBarcodeNodeType'
    # Label for nice name display
    bl_label = "Fake Barcode Values"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['barcodes'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerPersonNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake person names."""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerPersonNodeType'
    # Label for nice name display
    bl_label = "Fake Person Values"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['persons'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerLicenseNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake automotive license."""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerLicenseNodeType'
    # Label for nice name display
    bl_label = "Fake Automotive License Values"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['automotive_license_plates'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerGeoNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake geo lat long and related info."""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerGeoNodeType'
    # Label for nice name display
    bl_label = "Fake Geo Lat Long Values"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['lat_longs'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerCreditCardNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake credit card numbers"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerCreditCardNodeType'
    # Label for nice name display
    bl_label = "Fake Credit Card Values"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['credit_card_details'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerCompanyNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake company names."""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerCompanyNodeType'
    # Label for nice name display
    bl_label = "Fake Company Names"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['companies'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerEmailNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake email ids"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerEmailNodeType'
    # Label for nice name display
    bl_label = "Fake Email-Ids"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['email_ids'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


# Derived from the Node base type.
class FakerUserAgentNode(Node, FakerTreeNode):
    # === Basics ===
    # Description string
    """A custom node that generates fake user agents"""
    # Optional identifier string. If not explicitly defined, the python class name is used.
    bl_idname = 'FakerUserAgentNodeType'
    # Label for nice name display
    bl_label = "Fake User Agents"
    # Icon identifier
    bl_icon = 'LIBRARY_DATA_DIRECT'

    def init(self, context):
        """
        Initialization function, called when a new node is created.
        This is the most common place to create the sockets for a node, as shown below.
        NOTE: this is not the same as the standard __init__ function in Python, which is
              a purely internal Python method and unknown to the node system!
        """
        self.inputs.new('IntInputSocketType', "Random No Input")
        self.outputs.new('NodeSocketColor', "Status")

    # Copy function to initialize a copied node from an existing one.
    def copy(self, node):
        print("Copying from node ", node)

    # Free function to clean up on removal.
    def free(self):
        print("Removing node ", self, ", Goodbye!")

    def update(self):
        input_val = self.inputs[0].my_int_prop
        print("Faker Node input: ", input_val)
        sub_list = random.sample(faker_dict['user_agents'], input_val)
        for idx, elem in enumerate(sub_list):
            print(f"Item No {idx + 1}: {elem}")


