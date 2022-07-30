import os

# Method to generate cascade negetive file.
def generate_negative_file():
        with open('neg.txt', 'w') as f:
            for filename in os.listdir('neg'):
                f.write('neg/' + filename + '\n')

### OpenCV-3.4.16: https://sourceforge.net/projects/opencvlibrary/files/3.4.16/
## OpenCV Annotation Tool:-
# C:\Users\sshob\Downloads\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=pos.txt --images=p/

# Press 'c' - To confirm
# Press 'd' - To delete
# Press 'n' - To move to next image
# Press 'esc' - To exit

## Creating positive image vector file:-
# C:\Users\sshob\Downloads\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 2200 -vec pos.vec

## Training Cascade:-
# C:\Users\sshob\Downloads\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data ./cascade -vec pos.vec -bg neg.txt -numStages 17 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 535 -numNeg 1100 -w 24 -h 24