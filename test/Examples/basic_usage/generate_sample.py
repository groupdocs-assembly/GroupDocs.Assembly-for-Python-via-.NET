import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Generate sample : Generate sample report for document.\n")
            
    assembler = ga.DocumentAssembler()
    JsonDataSource = ga.data.JsonDataSource(constants.customerJsonFile)
    DataSourceInfo = ga.DataSourceInfo(JsonDataSource, "test")
    array = [DataSourceInfo]
    print(assembler.assemble_document(constants.input_doc, constants.output_doc, array))
