from decimal import *

class CineDrone_ActionCaptureCameraDesign:

    imageSensorSizeMM = 11
    LCDDisplayScreenK = 920
    ImageQuality = '2704x2028'
    NumberOfPhotoModesVideo = 7
    NumberOfPhotoModesStill = 3
    ProductEnhancements_CameraHousing = decimal(11)
    ProductEnhancements_EditingSharing = decimal(12)
    ProductEnhancements_IncludedAccessories = decimal(11)
    ExtraPerformanceFeatures = 3
    NumberOfACCameraModels = 3
    ProductRDExpenditures = decimal(3000)

    '''Grayed out'''
    CumulativeRDExpenditures = decimal(3000)
    PerformanceQualityRating = 4.5
    
    '''Projected AC Camera Projected Costs'''
    ImageSensorCosts = decimal(10_730)
    ImageSensorUnitCosts = decimal(10.00)
    LCDDisplayScreenCosts = decimal(10_730)
    LCDDisplayScreenCostsUnit = decimal(10.00)
    ImageQualityCosts = decmial(8_584)
    ImageQualityCostsUnit = decimal(8.00)
    PhotoModesCosts = decimal(6_975)
    PhotoModesCostsUnit = decimal(6.50)
    CameraHousingCosts = decimal(11_803)
    CameraHousingCostsUnit = decimal(11.00)
    EditingSharingCapabilitiesCosts = decimal(12_876)
    EditingSharingCapabilitiesCostsUnit = decimal(12.00)
    IncludedAccessoriesCosts = decimal(11_803)
    IncludedAccessoriesCostsUnit = decimal(11.00)
    ExtraPerformanceFeaturesCosts = decimal(9_657)
    ExtraPerformanceFeaturesCostsUnit = decimal(9.00)
    TotalCostOfComponentsFeaturesCosts = ImageSensorCosts + LCDDisplayScreenCosts + \
                                         ImageQualityCosts + PhotoModesCosts + CameraHousingCosts + \
                                         EditingSharingCapabilitiesCosts + IncludedAccessoriesCosts + \
                                         ExtraPerformanceFeaturesCosts 
    
    TotalCostOfComponentsFeaturesCosts = decimal(77.50)

    AssemblyLaborCosts = decimal(36_403)
    AssemblyLaborCostsUnit = decimal(33.93)
    ProductRDExpendituresCosts = decimal(3_000)
    ProductRDExpendituresCostsUnit = decimal(2.80)
    AllowanceforWarrantyRepairsCosts = decimal(3_620)
    AllowanceforWarrantyRepairsCostsUnit = decimal(3.37)
    MaintenanceOfPlantEquipmentCost = decimal(12_650)
    MaintenanceOfPlantEquipmentCostUnit = decimal(11.79)
    DepreciationOfPlantEquipmentCost = decimal(7_650)
    DepreciationOfPlantEquipmentCostUnit = decimal(7.13)
    TotalCameraProductionAssemblyCost = TotalCostOfComponentsFeaturesCosts + AssemblyLaborCosts + \
                                        ProductRDExpendituresCosts + AllowanceforWarrantyRepairsCosts + \
                                        MaintenanceOfPlantEquipmentCost + DepreciationOfPlantEquipmentCost 
    
    ''' Projected Unit Assembly '''	
    '''AC Camera Unit Assembly (000s)'''
    ACCameraUniAssemblyCost_Regular = decimal (894.00)
    ACCameraUniAssemblyCost_Overtime = decimal (179.00)
    ACCameraUniAssemblyCost_Total = ACCameraUniAssemblyCost_Regular + ACCameraUniAssemblyCost_Overtime 

    
