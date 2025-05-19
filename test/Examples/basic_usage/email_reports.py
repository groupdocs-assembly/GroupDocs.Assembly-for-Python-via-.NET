import groupdocs.assembly as ga
import constants

def run():
    print("\n--------------------------------------------------------------------------------------------------------------------")
    print("[Example Basic Usage] # Generate Email Report : Generate email report with common list.\n")
            
    assembler = ga.DocumentAssembler()
    dataSource = ga.data.JsonDataSource(constants.customerJsonFile)
    DataSourceInfo = ga.DataSourceInfo(dataSource, "customers")
    array = [DataSourceInfo, ga.DataSourceInfo(["test@test.mail", "groupdocs@groupdocs.mail"], "recipients"), ga.DataSourceInfo("sender@sender.mail", "sender"), ga.DataSourceInfo("cc@example.com", "cc"), ga.DataSourceInfo("groupdocs", "subject")]
    print(assembler.assemble_document(constants.input_common_list_msg, constants.output_common_list_msg, array))
