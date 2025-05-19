import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Merging table cells : Table Cell Merging in Word Processing documents.\n")
            
    assembler = ga.DocumentAssembler()
    dataSource = ga.data.XmlDataSource(constants.productXmlFile)
    DataSourceInfo = ga.DataSourceInfo(dataSource)
    array = [DataSourceInfo]
    print(assembler.assemble_document(constants.input_merging_docx, constants.output_merging_pdf, ga.LoadSaveOptions(ga.FileFormat.PDF), array))
