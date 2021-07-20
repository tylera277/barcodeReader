class secondHalfNumberIdentifier:
    """
    + I figured it would be easier to house all of the tools for
    analysing the right-hand side of the middle guard under a new class,
    instead of using the same function twice as I'm not that intelligent
    on figuring how to smoothly do that.
    """

    def __init__(self):
        pass

    def make2ndHalfPattern(self, list, endOfMiddle):
        newList = []
        for i in range(endOfMiddle, len(list), 1):
            newList.append(list[i])

        return newList

    def identify2ndHalfNumbers(self, secondHalfPattern):

        numberList = []
        newPatternList = secondHalfPattern

        for i in range(0, len(newPatternList) - 4, 4):

            # if even iterator, meaning its white stripes
            # even section is for the left side of the middle guard
            if len(numberList) <= 12:

                # this is for zero
                if newPatternList[i] == 3:
                    if newPatternList[i + 1] == 2:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 1:
                                numberList.append('zero')
                # one
                if newPatternList[i] == 2:
                    if newPatternList[i + 1] == 2:
                        if newPatternList[i + 2] == 2:
                            if newPatternList[i + 3] == 1:
                                numberList.append('one')
                # two
                if newPatternList[i] == 2:
                    if newPatternList[i + 1] == 1:
                        if newPatternList[i + 2] == 2:
                            if newPatternList[i + 3] == 2:
                                numberList.append('two')
                # three
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 4:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 1:
                                numberList.append('three')
                # four
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 1:
                        if newPatternList[i + 2] == 3:
                            if newPatternList[i + 3] == 2:
                                numberList.append('four')
                # five
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 2:
                        if newPatternList[i + 2] == 3:
                            if newPatternList[i + 3] == 1:
                                numberList.append('five')
                # six
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 1:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 4:
                                numberList.append('six')
                # seven
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 3:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 2:
                                numberList.append('seven')
                # eight
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 2:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 3:
                                numberList.append('eight')
                # nine
                if newPatternList[i] == 3:
                    if newPatternList[i + 1] == 1:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 2:
                                numberList.append('nine')
                if newPatternList[i] == 1:
                    if newPatternList[i + 1] == 1:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 1:
                                if newPatternList[i + 4] == 1:
                                    numberList.append('|MIDDLE|')
                                    endMiddle = i + 8
                                    print('end:', endMiddle)
        return numberList