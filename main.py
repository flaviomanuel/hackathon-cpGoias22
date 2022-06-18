import sys
import controller
if(__name__ == "__main__"):
    input_path = ''
    output_path = ''
    # -i=file, especifies the input file
    # -o=file, especifies the output file
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    for argumento in opts:
        if argumento[0:3] == '-i=':
            input_path = argumento[3:]
            input_extension = argumento[(argumento.rfind('.')+1):]
        elif argumento[0:3] == '-o=':
            output_path = argumento[3:]
    controller.control(input_path, output_path, input_extension)
    # python main.py -i="./audios/video.mp4" -o="./output/mp4/output.mp4"