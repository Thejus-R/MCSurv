import datetime
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from faker import Faker


# Initializing Firebase Admin SDK

cred = credentials.Certificate("cred.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mcsur-a0dd2-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Generating fake details


def getFakeDetails():
    fake = Faker()
    name = fake.name()
    email = name.replace(" ", "") + "@email.com"
    return name, email


# Getting current time & date
def getDateTime():
    x = datetime.datetime.now()
    date = x.strftime(r"%x")
    time = x.strftime("%I:%M %p")
    return date, time


class Challan:
    def __init__(self, vehicleRegNo, ownerName, timeStamp, camID, dateStamp):
        self.vehicleRegNo = vehicleRegNo
        self.ownerName = ownerName
        self.timeStamp = timeStamp
        self.dateStamp = dateStamp
        self.camID = camID

    def createChallan(self):
        challanNo = updateChallanNo()
        ref = db.reference("/challanList")
        ref.child(str(challanNo)).set({
            'vehicleRegNo': self.vehicleRegNo,
            'ownerName': self.ownerName,
            'timeStamp': self.timeStamp,
            'dateStamp': self.dateStamp,
            'camID': self.camID
        })


# Get Current Challan No. from Remote
def getChallanNo():
    ref = db.reference('/lastChallanNo')
    return ref.get()


# Increment Challan No. for new Challan
def updateChallanNo():
    ref = db.reference('/lastChallanNo')
    ref.set(getChallanNo() + 1)
    return getChallanNo()


def updatetoDatabase(regNo):
    td = getDateTime()
    person = getFakeDetails()
    x = Challan(regNo, person[0], td[1], "CHN01", td[0])
    x.createChallan()
