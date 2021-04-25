def ocrPart(dirPath):
    resDirPath='./img/result/'
    print("----------OCRing----------")
    return resDirPath
def detectionPart(dirPath):
    resDirPath='./img/result/'
    print("----------detecting----------")
    return resDirPath
def multimodalFusion(DIR_OCR,DIR_DETECTION):
    print('----------Fusing----------')
    # 通过 pointList 前四危险图片，finalPoint 最后得分
    pointList=[]
    imgPathList=[]
    finalPointList=[60,20,10,30]
    return pointList,imgPathList,finalPointList