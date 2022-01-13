
# import ee
# ee.Initialize()

# vegetation indices
def getNBR(image):
    NBR = image.expression(
        '(NIR - SWIR2) / (NIR + SWIR2)', {
            'NIR': image.select("NIR"),
            'SWIR2': image.select("SWIR2")})
    return image.addBands(NBR.rename("NBR"))

def getNDVI(image):
    NDVI = image.expression(
        '(NIR - R) / (NIR + R)', {
            'R': image.select("Red"),
            'NIR': image.select("NIR")})
    return image.addBands(NDVI.rename("NDVI"))

def getNDWI(image):
    NDWI = image.expression(
        '(NIR - SWIR1) / (NIR + SWIR1)', {
            'NIR': image.select("NIR"),
            'SWIR1': image.select("SWIR1")})
    return image.addBands(NDWI.rename("NDWI"))

def getVARI(image):
    VARI = image.expression(
        '(G - R) / (G + R - B)', {
            'B': image.select("Blue"),
            'G': image.select("Green"),
            'R': image.select("Red")})
    return image.addBands(VARI.rename("VARI"))

def getMSAVI(image):
    MSAVI = image.expression(
        '(2 * NIR + 1 - sqrt(pow((2 * NIR + 1), 2) - 8 * (NIR - R))) / 2', {
            'R': image.select("Red"),
            'NIR': image.select("NIR")})
    return image.addBands(MSAVI.rename("MSAVI"))

def getBAI(image):
    BAI = image.expression(
        '(1) / (((0.1 - R)**2) + ((0.06 - NIR)**2))', {
            'R': image.select("Red"),
            'NIR': image.select("NIR")})
    return image.addBands(BAI.rename("BAI"))

def getMIRBI(image):
    MIRBI = image.expression(
        '10 * SWIR2 + 9.8 * SWIR1 + 2', {
            'SWIR1': image.select("SWIR1"),
            'SWIR2': image.select("SWIR2")})
    return image.addBands(MIRBI.rename("MIRBI"))

def getCSI(image):
    CSI = image.expression(
        'NIR / SWIR1', {
            'NIR': image.select("NIR"),
            'SWIR1': image.select("SWIR1")})
    return image.addBands(CSI.rename("CSI"))