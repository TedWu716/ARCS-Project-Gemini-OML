import adsk.core, adsk.fusion, adsk.cam, traceback, ScalarisDataModel, SampleProject
import tempfile
import os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        dirId = ScalarisDataModel.ScalarisUniqueId()
        tempRootDir = tempfile.TemporaryDirectory()
       
        tempDir = tempRootDir+"/gemini/"+dirId.getId()
        os.mkdir(tempDir)
        ui.messageBox(tempDir + ' working directory created.')
        
        sampleProject = SampleProject.GenerateSampleProject()
        ui.messageBox('Sample project created.')
        id = sampleProject.get_Id()
        
        tempScalarisDir = tempDir+"/"+id
        
        messageBoard = ScalarisDataModel.ScalarisMessageBoard()
        
        success = sampleProject.Save(tempScalarisDir, messageBoard, SerializerType = 'OneJsonFile')
        msg = "Sample project write complete : " + success + '\n' + " number of errors: " + len(messageBoard.GetErrors()) + '\n'
        
        ui.messageBox(msg)
        
        for (dirpath, dirnames, filenames) in os.walk(tempScalarisDir):
            for file in filenames:
                if ".smt" in file:
                    copy_path = file.relace('.file.smt', '.smt')
                    os.rename(file, copy_path)
                    
        command = "Scalaris.Import " + tempScalarisDir + "/structural"
        app.executeTextCommand(command)
        ui.messageBox('Sample project import completed.')
        
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))