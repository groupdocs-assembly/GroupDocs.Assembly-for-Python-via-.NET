import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Conversion : Saving assembled Presentation document to template OTP presentation document.\n")
            
    assembler = ga.DocumentAssembler()
    dataSource = ga.data.XmlDataSource(constants.productXmlFile)
    DataSourceInfo = ga.DataSourceInfo(dataSource)
    array = [DataSourceInfo]
    print(assembler.assemble_document(constants.input_barcode_pptx, constants.output_barcode_otp, array))
