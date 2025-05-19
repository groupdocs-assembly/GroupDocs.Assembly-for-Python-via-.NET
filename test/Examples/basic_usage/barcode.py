import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Generate sample : Generate sample report for document with variable.\n")
            
    assembler = ga.DocumentAssembler()
    dataSource = ga.data.XmlDataSource(constants.productXmlFile)
    DataSourceInfo = ga.DataSourceInfo(dataSource)
    array = [DataSourceInfo]
    print(assembler.assemble_document(constants.input_barcode, constants.output_barcode, array))
