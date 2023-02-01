import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        # insert parameter name of interest
        param_name = 'Length'
        returnParam = design.userParameters.itemByName(param_name)
        ui  = app.userInterface
        ui.messageBox(returnParam.comment)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))