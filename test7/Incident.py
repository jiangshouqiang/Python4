import datetime
import pickle
import gzip
import os
import sys

class Incident:
    def __init__(self,report_id,date,airport,aircraft_id,
                 aircraft_type,pilot_percent_hours_on_type,
                 pilot_total_hours,midair,narrative=""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1 ,"invalid report ID"
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_id = aircraft_id
        self.aircraft_type = aircraft_type
        self.pilot_percent_hours_on_type = pilot_percent_hours_on_type
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self,date):
        assert isinstance(date,datetime.date),"invalid date"
        self.__date = date

    def export_pickle(self,filename,compress=False):
        fh = None
        try:
            if compress:
                fh = gzip.open(filename,"wb")
            else:
                fh = open(filename,"wb")
            pickle.dump(self,fh,pickle.HIGHEST_PROTOCOL)
            return True
        except(EnvironmentError , pickle.PicklingError) as err:
            print("{0}: export error : {1} ".format(
                os.path.basename(sys.argv[0],err)
            ))
            return False
        finally:
            if fh is not None:
                fh.close()

ind = Incident("21021","da","da","da","da","da","da","da")
ind.date("20213")
print(ind.date)