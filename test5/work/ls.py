from optparse import OptionParser

# parser = OptionParser()
# parser.add_option("-f", "--file", dest="filename",
#                   help="write report to FILE", metavar="FILE")
# parser.add_option("-q", "--quiet",
#                   action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
# parser.add_option("-n",type="int",dest="num")
#
# (options, args) = parser.parse_args(["-n42"])
# print(options.num,'W', args)
# args=["-f","ls.py"]
# (options, args) = parser.parse_args(args)
# print(options.filename, args)
usage = "usage: %prog [-f] [-q] [options] arg1 arg2 "
parser = OptionParser(usage=usage,version="%prog 1.0")
parser.add_option("-v","--verbose",
                  action="store_true",dest="verbose",default=True,
                  help="make lots of noise[default %default]")
parser.add_option("-q","--quiet",
                  action="store_false",dest="verbose",
                  help="be vewwy quiet (I'm hunting wabbits)")
parser.add_option("-f","--filename",
                  metavar="FILE",help="write output to FILE")
parser.add_option("-m","--mode",
                  default="initermediate",
                  help="interaction mode: novice ,intermediate or expert [default %default]")

(option,args) = parser.parse_args(["-q","File"])
print(option,":",args)