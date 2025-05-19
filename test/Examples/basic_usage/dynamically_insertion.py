import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Insert Hyperlink Dynamically : Insert Hyperlink Dynamically to DOCX document.\n")
            
    assembler = ga.DocumentAssembler()
    array = [ga.DataSourceInfo("https://www.groupdocs.com/", "uriExpression"), ga.DataSourceInfo("GroupDocs", "displayTextExpression")]
    print(assembler.assemble_document(constants.input_inserting_hyperlink, constants.output_inserting_hyperlink, array))
