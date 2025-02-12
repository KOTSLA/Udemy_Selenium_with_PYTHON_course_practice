
ItemsInCard = 0

if ItemsInCard != 0:
    raise Exception("Products Cart count not matching")


#error control with Try except block witch does not fail test
try:
    assert (ItemsInCard == 2)
except:
    print("Error, the items in card not 2")


try:
    with open("filelog.txt", "r") as reader:
        reader.read()
except:
    print("There is failure in try block. Such file does not exist.")

#if we want see system error text, not our custom
try:
    with open("filelog.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)
finally:                #use only in try-except block, independent to result in block it will run
    print("cleaning up resources")