import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        design = app.activeProduct
        # Read the csv file.
        cnt = 0
        file = open('C://Temp//values.csv')
        for line in file:
            # Get the values from the csv file.
            pieces = line.split(',')
            
            length = pieces[0]
            width = pieces[1]
            height = pieces[2]
            
            # Set the parameters.
            lengthParam = design.userParameters.itemByName('Length')
            lengthParam.expression = length
            
            widthParam = design.userParameters.itemByName('Width')
            widthParam.expression = width

            heightParam = design.userParameters.itemByName('Height')
            heightParam.expression = height
            
            #Export the STEP file.
            exportMgr = design.exportManager
            stepOptions = exportMgr.createSTEPExportOptions('C:\\Temp\\test_​box' + str(cnt) + '.stp')
            cnt += 1
            res = exportMgr.execute(stepOptions)
        
        ui.messageBox('Finished')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))