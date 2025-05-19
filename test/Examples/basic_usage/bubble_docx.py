import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Generate sample : Generate sample report for bubble chart docx.\n")
            
    assembler = ga.DocumentAssembler()
    dataSource = ga.data.JsonDataSource(constants.customerJsonFile)
    DataSourceInfo = ga.DataSourceInfo(dataSource, "customers")
    array = [DataSourceInfo]
    print(assembler.assemble_document(constants.input_bubble_docx, constants.output_bubble_docx, array))
