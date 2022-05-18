import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


# Initializing Firebase Admin SDK
cred = credentials.Certificate("cred.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mcsur-a0dd2-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


class Challan:
    def __init__(self, vehicleRegNo, ownerName, timeStamp, camID, dateStamp):
        self.vehicleRegNo = vehicleRegNo
        self.ownerName = ownerName
        self.timeStamp = timeStamp
        self.camID = camID
        self.dateStamp = dateStamp

    def createChallan(self):
        challanNo = updateChallanNo()
        ref = db.reference("/challanList")
        ref.child(str(challanNo)).set({
            'vehicleRegNo': self.vehicleRegNo,
            'ownerName': self.ownerName,
            'timeStamp': self.timeStamp,
            'camID': self.camID,
            'dateStamp': self.dateStamp
        })


# Get Current Challan No. from Remote
def getChallanNo():
    ref = db.reference('/lastChallanNo')
    return ref.get()


# Increment Challan No. for new Challan
def updateChallanNo():
    ref = db.reference('/lastChallanNo')
    ref.set(getChallanNo()+1)
    return getChallanNo()


# Creating an object of Challan
x = Challan('KL-02-BD-5008', "Thejus Rajendran",
            "12:30PM", "CHN01", "02/04/2022")

# Calling createChallan() for adding data to remote
x.createChallan()

# def getChallanNo():
#     ref = db.reference('/lastChallanNo')
#     return ref.get()


# def updateChallanNo():
#     ref = db.reference('/lastChallanNo')
#     ref.set(getChallanNo()+1)


# print(x.createJSON())


# data1 = {"001": {
#     "regNo": "KL-03-BD-5008",
#     "time": "12:45PM"
# }}


# data2 = {"002": {
#     "regNo": "KL-03-BC-5043",
#     "time": "1:45PM"
# }}

# # Parse JSON into an object with attributes corresponding to dict keys.
# ref = db.reference('/billNo')
# ref.set(data1)

# ref = db.reference('/billNo/001')
# x = ref.get()
# print(x['regNo'], x['time'])

# ref = db.reference('/billNo')
# ref.update(data2)


# ref = db.reference('/billNo/002')
# x = ref.get()
# print(x['regNo'], x['time'])
