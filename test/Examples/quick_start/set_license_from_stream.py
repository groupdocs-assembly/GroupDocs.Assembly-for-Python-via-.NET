# set_license_from_stream.py
# This example demonstrates how to set a license from a stream.

import groupdocs.assembly as ga
import constants
import os
from os.path import join

def run():
    if os.path.exists(constants.license_path):
        with open(constants.license_path, "rb") as stream:
            ga.License().set_license(stream)

        print("License set successfully.")
    else:
        print("\nWe do not ship any license with this example. " +
              "\nVisit the GroupDocs site to obtain either a temporary or permanent license. " +
              "\nLearn more about licensing at https://purchase.groupdocs.com/faqs/licensing. " +
              "\nLearn how to request a temporary license at https://purchase.groupdocs.com/temporary-license.")

if __name__ == "__main__":
    run()
