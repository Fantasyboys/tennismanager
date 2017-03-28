from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50, db_column='name')
    surname = models.CharField(max_length=50, db_column='surname')
    location = models.CharField(max_length=50, db_column='location', null=True)
    region = models.CharField(max_length=50, db_column='region', null=True)
    zipCode = models.IntegerField(db_column='zip_code', null=True)
    mail = models.EmailField(max_length=100, db_column='mail', null=True)
    
    def getName(self):
        return self.__name


    def getSurname(self):
        return self.__surname


    def getLocation(self):
        return self.__location

    def getRegion(self):
        return self.__region


    def getZipCode(self):
        return self.__zipCode


    def getMail(self):
        return self.__mail


    def setName(self, value):
        self.__name = value


    def setSurname(self, value):
        self.__surname = value


    def setLocation(self, value):
        self.__location = value


    def setRegion(self, value):
        self.__region = value


    def setZipCode(self, value):
        self.__zipCode = value


    def setMail(self, value):
        self.__mail = value


    def delName(self):
        del self.__name


    def delSurname(self):
        del self.__surname


    def delLocation(self):
        del self.__location


    def delRegion(self):
        del self.__region


    def delZipCode(self):
        del self.__zipCode


    def delMail(self):
        del self.__mail
    
    