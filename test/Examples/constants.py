import os
from os.path import join
import platform


#license_path = os.environ.get('CONHOLDATE_LIC_PATH')
input_path = "./Resources/SampleFiles/"
output_path = "./Resources/Output/"



def get_input_file_path(file_path):
    if platform.system() == 'Windows':
        return join(input_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, input_path, file_path)

def get_output_file_path(file_path):
    if platform.system() == 'Windows':
        return join(output_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, output_path, file_path)
    
def get_data_source_file_path(file_path):
    if platform.system() == 'Windows':
        return join(input_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, input_path, file_path)

ImagesDir = get_input_file_path("Image/")
TemplatesDir = get_input_file_path("Templates/")

input_doc = get_input_file_path("Templates/SimpleTest.doc")
input_doc_var = get_input_file_path("Templates/SimpleTest2.doc")
input_barcode = get_input_file_path("Templates/input_barcode.ppt")
input_bubble_docx = get_input_file_path("Templates/input_bubble.docx")
input_barcode_pptx = get_input_file_path("Templates/input_barcode.pptx")
input_inserting_hyperlink = get_input_file_path("Templates/Inserting hyperlink.docx")
input_common_list_msg = get_input_file_path("Templates/Common list.msg")
input_readme_md = get_input_file_path("Templates/Readme.md")
input_merging_docx = get_input_file_path("Templates/Merging table cells dynamically.docx")


output_doc = get_output_file_path("output.doc")
output_doc_var = get_output_file_path("output_var.doc")
output_barcode = get_output_file_path("output_barcode.ppt")
output_bubble_docx = get_output_file_path("output_bubble.docx")
output_barcode_otp = get_output_file_path("output_barcode.otp")
output_inserting_hyperlink = get_output_file_path("Inserting hyperlink.docx")
output_common_list_msg = get_output_file_path("Common list.msg")
output_readme_docx = get_output_file_path("Readme.docx")
output_merging_pdf = get_output_file_path("Merging table cells dynamically.pdf")


data_sources_dir = get_data_source_file_path("DataSource/")
customerJsonFile = get_data_source_file_path("DataSource/Customers.json")
managersJsonFile = get_data_source_file_path("DataSource/Managers.json")
managersXmlFile = get_data_source_file_path("DataSource/Managers.xml")
personsCsvFile = get_data_source_file_path("DataSource/Persons.csv")
testDataSourceJsonFile = get_data_source_file_path("DataSource/TestDataSource.json")
productXmlFile = get_data_source_file_path("DataSource/Product.xml")
ordersXmlFile = get_data_source_file_path("DataSource/Orders.xml")