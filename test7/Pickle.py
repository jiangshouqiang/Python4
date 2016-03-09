import pickle
import gzip
import os
import sys
GZIP_MAGIC=b"\x1F\x8B"
class Test1(dict):

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
    def import_pickle(self,filename):
        fh = None
        try:
            fh = open(filename,"rb")
            magic = fh.read(len(GZIP_MAGIC))
            if magic == GZIP_MAGIC:
                fh.close()
                fh = gzip.open(filename,'rb')
            else:
                fh.seek(0)
            self.clear()
            self.update(pickle.load(fh))
            return True
        except(EnvironmentError ,pickle.UnpicklingError) as err:
            print("{0}:import error:{1}".format(
                os.path.basename(sys.argv[0]),err
            ))
            return False
        finally:
            if fh is not None:
                fh.close()


pickle_test = Test1()
print(pickle_test.export_pickle("file.txt",True))
print(pickle_test.import_pickle("file.txt"))
print(pickle_test)