

import ee
#ee.Initialize()

# coefs
coefficients = {
  'itcps': ee.Image.constant([0.0003, 0.0088, 0.0061, 0.0412, 0.0254, 0.0172]).multiply(10000),
  'slopes': ee.Image.constant([0.8474, 0.8483, 0.9047, 0.8462, 0.8937, 0.9071])
}

# Function to get and rename bands of interest from OLI.
def renameOli(img):
    return img.select(
        ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'pixel_qa'],
        ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2', 'pixel_qa'])

#// Function to get and rename bands of interest from ETM+.
def renameEtm(img):
    return img.select(
        ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'pixel_qa'],
        ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2', 'pixel_qa'])

def etmToOli(img):
  return img.select(['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'])\
      .multiply(coefficients['slopes'])\
      .add(coefficients['itcps'])\
      .round()\
      .toShort()\
      .addBands(img.select('pixel_qa'))

def fmask(img):
    cloudShadowBitMask = (1 << 3)
    cloudsBitMask = (1 << 5)
    qa = img.select('pixel_qa')
    mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0).And(qa.bitwiseAnd(cloudsBitMask).eq(0))
    return img.updateMask(mask)

def rescale(image):
    B1 = image.select('Blue').multiply(0.0001).rename("Blue_n")
    B2 = image.select('Green').multiply(0.0001).rename("Green_n")
    B3 = image.select('Red').multiply(0.0001).rename("Red_n")
    B4 = image.select('NIR').multiply(0.0001).rename("NIR_n")
    B5 = image.select('SWIR1').multiply(0.0001).rename("SWIR1_n")
    B6 = image.select('SWIR2').multiply(0.0001).rename("SWIR2_n")
    qa = image.select('pixel_qa')
    image = image.addBands([B1, B2, B3, B4, B5, B6, qa])
    image = image.select(['Blue_n', 'Green_n', 'Red_n', 'NIR_n', 'SWIR1_n', 'SWIR2_n', 'pixel_qa'])
    image = image.rename(['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2', 'pixel_qa'])
    return image

#// Define function to prepare OLI images.
def prepOli(img):
    orig = img
    img = renameOli(img)
    img = fmask(img)
    return ee.Image(img.copyProperties(orig, orig.propertyNames()))

#// Define function to prepare ETM+ images.
def prepEtm(img):
    orig = img
    img = renameEtm(img)
    img = fmask(img)
    img = etmToOli(img)
    return ee.Image(img.copyProperties(orig, orig.propertyNames()))
