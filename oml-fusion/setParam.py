import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = adsk.fusion.Design.cast(app.activeProduct)
        # create parameter 
        param_name = 'Length'
        param_unit = 'mm'
        param_ex = 1/3
        param_ex_real = adsk.core.ValueInpute.createbyReal(param_ex)
        design.userParameters.add(param_name, param_ex_real, param_unit, "")
        ui  = app.userInterface
        ui.messageBox('Parameter ' + param_name + ' has been created. Please double check UI for it.')
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))