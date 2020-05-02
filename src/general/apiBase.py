class apiBase:
    #attributes may be added or removed
    #attributes = data for database
    title=""
    text=""
    lables=""
    created=""
    edited=""
    
    #attributes that are mostly present in one service
    noteColor=""
    
    #not clear yet how database connection works
    dataBaseObject
    
    def inject_in_Database (self):
        """function for the injection of given data from the service into the database"""
        #get attribute data from service and add it to the database
        
    def extract_from_Database (self):
        """function for the injection of given data from the database into the service"""
        #extract data from database and inject it into the service
        
        
#example for googleKeep
class apiKeep(apiBase):
    def inject_in_Database(self):
        #override method here
        
    def extract_from_Database(self):
        #override method here