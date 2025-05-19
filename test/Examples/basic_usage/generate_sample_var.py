import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Generate sample : Generate sample report for document with variable.\n")
            
    assembler = ga.DocumentAssembler()
    JsonDataSource = ga.data.JsonDataSource(constants.customerJsonFile)
    DataSourceInfo = ga.DataSourceInfo(JsonDataSource, "customers")
    array = [DataSourceInfo]
    print(assembler.assemble_document(constants.input_doc_var, constants.output_doc_var, array))
