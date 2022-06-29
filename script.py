from distutils.log import error
import os

from cv2 import exp
import tesseract
import processBBox
import database

import shutil

# remove old directory
try:
    shutil.rmtree(r'MCSurv')
except os.error:
    print("error")


# generate command
image_name = "biker-without-helmet"

cmd = "python detect.py --weights best.pt --source " + image_name + \
    ".jpg --data data.yaml --save-txt --save-crop --save-conf --project MCSurv --conf-thres 0.50"

os.system(cmd)
if(processBBox.processBoundingBox(image_name)):
    RegNo = tesseract.processLPlate(image_name)
    database.updatetoDatabase(RegNo)
else:
    print("Motorcyclist without helmet is not found!")
# model = torch.hub.load('./', 'custom', path='./best.pt', source='local')
# img = 'biker-without-helmet.jpg'

# result = model(img)
# result.show()
