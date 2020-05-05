from pymongo import MongoClient 

class mongoDB():

    def __init__(self):
        self.myDB = "mongodb+srv://pi:N0tT0Kn0w@cluster0-wegmd.mongodb.net/test?retryWrites=true&w=majority"
        self.DBclient = MongoClient(self.myDB)
        self.db = self.DBclient.get_database('sensors_db')


    def getCollection(self):  
        # Be carefull by writing the exact name of the collection. 
        records = self.db.sensors_record
        
        return records


    ## To check the count of documents I have currently in my collection

    def getCountDocs(self, records):
        # We can provide a filter or not insede de {}
        count =  records.count_documents({})
        return count 


    ## Create a def on main() raasp to create a dictionary using the information provided by the sensors. 
    def exportData(self, dicctionary, records):
        records.insert_one(dicctionary)
        # Si uso records.insert_many(dictList) exporto casa diccionario dentro de la lista como un nuevo document. 
        # Es mejor, para un dia envira un diccionario de listas y no una lisya de diccionarios ej: "mq2' = 3,4,4 "
        
    ## Get all the documents of the collection at a time
    def importData(self, records):
        list(records.find())

    ## Get one document of the collection by filtering per key
    # def importDataKey(self, records):
    #     records.find_one({'key': value})

    ## To edit a document of the DB 
    # def updateDocument(self, records):
    #     ## New information
    #     updates = {
    #         'key':value
    #     }
    #     #Modify a single doc
    #     records.update_one({'key':oldvalue}, {'$set': updates})
    #     #If using records.update_many I can update all the documents at the same time

    ## Delete a object filtering by a given key value
    # def deleteDocument(self, records):
    #     records.delete_one({'key': value})


    

# def main():

#     mongo = mongoDB()

#     records = mongo.getCollection()
#     countDocs = mongo.getCountDocs(records)
#     print("Count", countDocs)

print("klok mongo")


