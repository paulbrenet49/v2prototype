import fileinput

counter = 0
number_from = 0

def setVariableNull():

    global counter
    global number_from

    counter = 0
    number_from = 0

#replace the filepath by the corresponding path to the gain_live.cfg

def replace_gain(number_to):

    global counter
    global number_from

    if counter == 0:
        variable_from = "mha.gain.gains = [ " + str(0) + " " + str(0) + " ]"
        variable_to = "mha.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
        with fileinput.FileInput('gain_live.cfg',
                                 inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(variable_from,
                                   variable_to), end='')

        number_from = number_to
        #print("variable_to", variable_to)

    else :
        variable_from = "mha.gain.gains = [ " + str(number_from) + " " + str(number_from) + " ]"
        variable_to = "mha.gain.gains = [ " + str(number_to) + " " + str(number_to) + " ]"
        with fileinput.FileInput('gain_live.cfg',
                                 inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(variable_from,
                                   variable_to), end='')
        #if number_from < 0:



        number_from  = number_to
        #print("variable_to", variable_to)

    counter = counter + 1
    print("counter = ", counter)





"""

def replace_gain(number_to):

    global counter
    global number_from

    if counter == 0:
        variable_from = "mha.transducers.mhachain.altplugs.dynamiccompression.fftlen = " + str(0)
        variable_to = "mha.transducers.mhachain.altplugs.dynamiccompression.fftlen = " + str(number_to)
        with fileinput.FileInput('C:/Octave/Octave-4.4.1/openMHA-master/mha/examples/000-start/openMHA_test.cfg',
                                 inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(variable_from,
                                   variable_to), end='')

        number_from = number_to

    else :
        variable_from = "mha.transducers.mhachain.altplugs.dynamiccompression.fftlen = " + str(number_from)
        variable_to = "mha.transducers.mhachain.altplugs.dynamiccompression.fftlen = " + str(number_to)
        with fileinput.FileInput('C:/Octave/Octave-4.4.1/openMHA-master/mha/examples/000-start/openMHA_test.cfg',
                                 inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(variable_from,
                                   variable_to), end='')
        #if number_from < 0:



        number_from  = number_to

    counter = counter + 1
    print("counter = ", counter)

"""

#replace_gain(2056)

