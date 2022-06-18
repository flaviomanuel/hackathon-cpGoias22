import sys
if(__name__ == "__main__"):

    # -i=file, especifies the input file
    # -o=file, especifies the output file
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    args = [args for args in sys.argv[1:] if not args.startswith("-")]
    print(opts)

