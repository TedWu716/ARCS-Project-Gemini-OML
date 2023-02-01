import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        design = app.activeProduct
        ui  = app.userInterface
        
        rootComp = app.activeProduct.rootComponent
        
        ui.messageBox('Parameters count ' + str(design.allParameters.count))

        for i in range(rootComp.occurrences.count):
            occurence = rootComp.occurrences.item(i)

            attribute = occurence.attributes

            # Get physical properties from occurrence
            physicalProperties = occurence.physicalProperties

            # Get data from physical properties
            area = physicalProperties.area
            density = physicalProperties.density
            mass = physicalProperties.mass
            volume = physicalProperties.volume
            
            # Get accuracy from physical properties
            accuracy = physicalProperties.accuracy

            # Get center of mass from physical properties
            cog = physicalProperties.centerOfMass

            # Get principal axes from physical properties
            (retVal, xAxis0, yAxis0, zAxis0) = physicalProperties.getPrincipalAxes()   
            
            # Get the moments of inertia about the principal axes. Unit for returned values is kg/cm^2.
            (retVal,i1,i2,i3) = physicalProperties.getPrincipalMomentsOfInertia()

            # Get the radius of gyration about the principal axes. Unit for returned values is cm.
            (retVal, kx, ky, kz) = physicalProperties.getRadiusOfGyration()

            # Get the rotation from the world coordinate system of the target to the principal coordinate system.
            (retVal, rx, ry, rz) = physicalProperties.getRotationToPrincipal()

            # Get the moment of inertia about the world coordinate system.
            (retVal, xx, yy, zz, xy, yz, xz) = physicalProperties.getXYZMomentsOfInertia()


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))