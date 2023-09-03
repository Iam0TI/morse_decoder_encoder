import script
import optparse

def main():
    
    parser= optparse.OptionParser()
    parser.add_option("-d","--decode", action="store_const", const=True, dest="decode", help="USE THE OPTION TO DECODE MORSE TO PLAIN ENGLISH")
    parser.add_option("-e","--encode", action="store_const", const=True, dest="encode", help="USE THE OPTION TO ENCODE PLAIN ENGLISH TO MORSE CODE")
    (options,arguments)= parser.parse_args()
    
    if options.encode:
            script.morse_encoder()
    elif options.decode:
            script.morse_decoder()
    elif not options.encode or options.decode:
        parser.error(" use  -h, --help   to show the help message and avaliable options")


if __name__ ==  "__main__":
    main()

