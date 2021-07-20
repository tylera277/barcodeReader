

class NumberIdentifier:
    def __init__(self, patternList):
        self.patternList = patternList

    def identifyNumbers(self):

        # this for loop is to just get rid of the first three
        newPatternList = []
        for j in range(3, len(self.patternList)):
            newPatternList.append(self.patternList[j])
        print('New pattern:', newPatternList)
        numberList = []
        endMiddle = 0

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
                if  newPatternList[i] == 1:
                    if newPatternList[i + 1] == 1:
                        if newPatternList[i + 2] == 1:
                            if newPatternList[i + 3] == 1:
                                if newPatternList[i + 4] == 1:
                                    numberList.append('|MIDDLE|')
                                    endMiddle = i+8
                                    #print('end:', endMiddle)
            else:
                numberList.append('?')
            #if len(numberList) == 7:
            #    break
        return numberList, endMiddle



