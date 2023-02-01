import adsk.core, adsk.fusion, adsk.cam, csv, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        doImportExport(False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def doImportExport(isImport):
     app = adsk.core.Application.get()
     ui  = app.userInterface
     
     try:   
         fileDialog = ui.createFileDialog()
         fileDialog.isMultiSelectEnabled = False
         fileDialog.title = "Get the file to read from or the file to save the parameters to"
         fileDialog.filter = 'Text files (*.csv)'
         fileDialog.filterIndex = 0
         if isImport:
             dialogResult = fileDialog.showOpen()
         else:
             dialogResult = fileDialog.showSave()
             
         if dialogResult == adsk.core.DialogResults.DialogOK:
             filename = fileDialog.filename
         else:
             return

         # if isImport is true read the parameters from a file
         if not isImport:
             writeParametersToFile(filename)

     except:
         if ui:
             ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def writeParametersToFile(filePath):
    app = adsk.core.Application.get()
    design = app.activeProduct
                      
    with open(filePath, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, dialect=csv.excel)
        for param in design.allParameters:
            try:
                paramUnit = param.unit
            except:
                paramUnit = ""
            
            csvWriter.writerow([param.name, paramUnit, param.expression, param.comment]) 
    
    # get the name of the file without the path    
    partsOfFilePath = filePath.split("/")
    ui  = app.userInterface
    ui.messageBox('Parameters written to ' + partsOfFilePath[-1]) 