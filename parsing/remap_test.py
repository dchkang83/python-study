def remap(x, oMin, oMax, nMin, nMax):

    #range check
    if oMin == oMax:
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min(oMin, oMax)
    oldMax = max(oMin, oMax)
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False
    newMin = min(nMin, nMax)
    newMax = max(nMin, nMax)
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

if __name__ == '__main__':
    result = remap(25.0, 0.0, 100.0, 1.0, -1.0)
    print(result)

    # test cases
    print(remap(25.0, 0.0, 100.0, 1.0, -1.0), "==", 0.5)
    print(remap(25.0, 100.0, -100.0, -1.0, 1.0), "==", -0.25)
    print(remap(-125.0, -100.0, -200.0, 1.0, -1.0), "==", 0.5)
    print(remap(-125.0, -200.0, -100.0, -1.0, 1.0), "==", 0.5)
    #even when value is out of bound
    print(remap(-20.0, 0.0, 100.0, 0.0, 1.0), "==", -0.2)

