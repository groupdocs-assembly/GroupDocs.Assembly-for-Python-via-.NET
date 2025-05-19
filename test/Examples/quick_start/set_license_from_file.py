# set_license_from_file.py
# This example demonstrates how to set license from file.
# The SetLicense method attempts to set a license from several locations relative to the executable and GroupDocs.Viewer.dll.
# You can also use the additional overload to load a license from a stream, this is useful for instance when the 
# License is stored as an embedded resource. 

import groupdocs.assembly as ga
import constants
import os
  

def run():
    if os.path.exists(constants.license_path):    
        license = ga.License()
        license.set_license(constants.license_path)
        print("License set successfully.")
    else:
       print("Not find license.")


