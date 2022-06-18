import sys
import output

if(__name__ == "__main__"):
    input_path = ''
    output_path = ''
    # -i=file, especifies the input file
    # -o=file, especifies the output file
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    for argum in opts:
        argumento = argum
        if argumento[0:3] == '-i=':
            input_path = argumento[3:]
        elif argumento[0:3] == '-o=':
            output_path = argumento[3:]
    print(input_path, output_path)
    output.merge_files(input_path, "./output/wav/video.wav", output_path)
    # python main.py -i="./audios/video.mp4" -o="./output/mp4/output.mp4"