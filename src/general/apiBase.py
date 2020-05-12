class apiBase:
    #attributes may be added or removed
    #attributes = data for database
    title=""
    text=""
    created=""
    edited=""
     
    #not clear yet how database connection works
    dataBaseObject=''

        
    def inject_in_API (self):
        """function for the injection of given data from JSON into the service"""
        #get attribute data from JSON and inject it into the service
        return     
    
    def extract_from_API (self):
        """function for the injection of given data from the service into JSON"""
        #get attribute data from service and convert it to JSON
        return 
    
    def inject_in_Database (self):
        """function for the injection of given data from JSON into the database"""
        #get attribute data from JSON and add it to the database
        return
       
    def extract_from_Database (self):
        """function for the injection of given data from the database into the JSON"""
        #extract data from database and convert it to JSON
        return
        
        
#example for googleKeep
class apiKeep(apiBase):
    def inject_in_Database(self):
        #override method here
        return
        
    def extract_from_Database(self):
        #override method here
        return