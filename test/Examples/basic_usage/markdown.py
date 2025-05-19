import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Saving an assembled Markdown : Saving an assembled Markdown document to a Word Processing format using file extension.\n")
            
    assembler = ga.DocumentAssembler()
    description = "GroupDocs.Assembly for .NET is a class library that enables you to generate documents in popular office and email file formats based upon template documents and data obtained from various sources including databases, XML, JSON, OData, objects of custom .NET types, external documents, and more.";
    array = [ga.DataSourceInfo("GroupDocs.Assembly for .NET", "product"), ga.DataSourceInfo(description, "description")]
    print(assembler.assemble_document(constants.input_readme_md, constants.output_readme_docx, array))
