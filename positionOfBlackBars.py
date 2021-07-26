

class PositionOfBlackBars:
    """
    +Input an array of a picture, and get out the position of the pixels
     black marks of the barcode stripes
    """

    def __init__(self, pic):
        self.pic = pic

    def position(self):
        """
        Takes in the raw picture and outputs, at a certain height, the
        location of the black pixels which are to represent the vertical
        bars of the barcode.
        """

        i = 0
        pos = []
        while i < self.pic.shape[1]:
            if (self.pic[250, i, 2]) <= 175:

                pos.append(i)
            i += 1

        return pos

    def rawDataCorrector(self, list):
        """
        Takes the black pixel array and fills in numbers if there are
        gaps that exist and which are not large enough to constitute a
        feature of the barcode but instead some kind of data reading/
        recording failure.
        """

        newList = []
        # +if between 2 and 3 pixels are missing from raw data set,
        # place the value in.
        for i in range(0, len(list)-1, 1):
            start = list[0]
            diff = (list[i + 1] - list[i])
            if diff > 1 and diff <= 3:
                for j in range(diff):
                    newList.append(list[i] + j)
            else:
                newList.append(list[i])



        return newList

    def DifferenceCalculator(self, filledInList):
        """
        Outputs a list of the difference between each number, either one
        or some larger number.
        """

        difference = []
        for k in range(0, len(filledInList)-1):
            diff = filledInList[k+1] - filledInList[k]
            difference.append(diff)

        return difference

    def Change(self, Difference):
        """
        Outputs a list which has the change between values of the difference
        list, outputting the sum of the 1's and outputting the other numbers.
        """

        changeInChange = []
        momentarySum = 0

        for i in range(0, len(Difference)):
            if Difference[i] == 1:
                momentarySum += 1

            elif Difference[i] != 1:
                changeInChange.append(momentarySum)
                changeInChange.append(Difference[i])
                momentarySum = 0
        # +this append is needed in order to get the last value on the
        # right side of the barcode
        changeInChange.append(momentarySum)



        return changeInChange


    def IdentifyStartGuard(self, difference, change):
        """
        +Tries to identify the unique signature that is the start guard,
        basically the first three data points of the difference list.
        + I cant figure out how to do this intelligently and adaptively
        at the moment.
        """

        # identify end of start guard

        moduleWidth = change[1]
        #i = 0
        #sum = 0
        #counter = 0
        #while i < len(difference):
       #     if difference[i] != 1:
        #        counter += 1
        #    if counter == 2:
        #        break
        #    i += 1

        return moduleWidth

    def patternWriter(self, list, moduleWidth):
        """
        + Takes the list of the changes in the difference list and divides it
        by the module length
        :param list:
        :return:  a list which will have the width in terms of modules of
        of the black and white stripes of the barcode.
        """

        pattern = []

        for i in range(len(list)):
            pattern.append(int(list[i]/moduleWidth))

        return pattern

    def clustering(self, change, numOfClusters, moduleWidth):
        """
        An attempt at implementing a shitty clustering
        "algorithm" with the ultimate aim of assigning the data into
        four clusters and
        assigning those in each cluster a multiple of the module width,
        hopefully making the number identifier of the patterns list
        more effective and better at handling variations in specific
        pixel readings.
        """

        MostFrequent = max(set(change), key=change.count)

        # Testing something
        if MostFrequent > moduleWidth:
            MostFrequent1 = MostFrequent
        elif MostFrequent < moduleWidth:
            MostFrequent1 = moduleWidth
        else:
            MostFrequent1 = MostFrequent

        print('Most frequent:', MostFrequent1)

        centroidPos = []
        for i in range(1, numOfClusters+1):
            centroidPos.append(i*MostFrequent1)

        cluster1 = []
        cluster2 = []
        cluster3 = []
        cluster4 = []

        k = 0
        while k < 1:

            for l in range(len(change)):
                dist0 = abs(change[l] - centroidPos[0])**2.0
                dist1 = abs(change[l] - centroidPos[1])**2.0
                dist2 = abs(change[l] - centroidPos[2])**2.0
                dist3 = abs(change[l] - centroidPos[3])**2.0

                if min(dist0, dist1, dist2, dist3) == dist0:
                    cluster1.append(change[l])
                if min(dist0, dist1, dist2, dist3) == dist1:
                    cluster2.append(change[l])
                if min(dist0, dist1, dist2, dist3) == dist2:
                    cluster3.append(change[l])
                if min(dist0, dist1, dist2, dist3) == dist3:
                    cluster4.append(change[l])
            k+= 1
        cluster1.sort()

        print('cluster1:', cluster1)
        print('cluster2:', cluster2)
        print('cluster3:', cluster3)
        print('cluster4:', cluster4)

        for o in range(len(change)):
            if change[o] in cluster1:
                change[o] = MostFrequent1
            if change[o] in cluster2:
                change[o] = MostFrequent1 * 2
            if change[o] in cluster3:
                change[o] = MostFrequent1 * 3
            if change[o] in cluster4:
                change[o] = MostFrequent1 * 4

        print('new change:', change)

        return change

    def parityDetector(self, list, firstList):
        """

        """
        newList = []
        for i in range(0, 1, 1):

            # +this if checks the parity of the list, if its even, that means the
            # list is flipped upside down.
            if (list[i+1] + list[i+3]) % 2 == 0:
                print('flipped')
                for j in range(len(list)-1, -1, -1):
                    newList.append(list[j])

            else:
                print('Not flipped')
                newList.append('NONE')
        return newList

