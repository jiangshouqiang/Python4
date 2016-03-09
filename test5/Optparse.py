import optparse
def main():
    parser = optparse.OptionParser()
    parser.add_option("-w","--maxwidth",dest="maxwidth",type="int",
                      help=("the maximum number of characters that can be output [default : %default]"),
                      )
    parser.add_option("-f","--format",dest="format",
                      help=("the maximum number of characters that can be output [default : %default]"))
    parser.set_default(maxwidth=100,format=".0f")
    opt,args = parser.parse_args()
main()