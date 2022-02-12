# EPAi4 Capstone - Integrating Faker into Blender Nodes
### Name: Divyam Malay Shah
### Email: divyam096@gmail.com

This repository contains the necessary code that can be used to create nodes in Blender that can generate fake values
for the following providers:
-  Fake Phone Numbers
-  Fake Barcodes
-  Fake Colors
-  Fake Company Names
-  Fake Credit Card Details
-  Fake Email-Ids
-  Fake Geo Details (lat-long and related info)
-  Fake Automotive Licenses 
-  Fake Person Names
-  Fake User Agents


## Setup

1. Create a dump of fake data relating to our providers. You should get a file named *faker_data_dump.pickle*.<br>
``python faker_generator.py``

2. Go to [setup.py](bpy_faker/setup.py) and update the ``FAKER_DATA_PICKLE_PATH`` variable with the absolute path of
 *faker_data_dump.pickle* generated in the previous step.
 
3. Create a .zip file by compressing the bpy_faker directory.

4. Import the package as follows: Open Blender -> Edit -> Preferences -> Add-ons -> Install -> select the bpy_faker.zip 
file.

You are good to go!

## Demo
[![Video Demo](https://img.youtube.com/vi/FoKsFUS4tsA/0.jpg)](https://www.youtube.com/watch?v=FoKsFUS4tsA)



























