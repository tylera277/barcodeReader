# date: 7/18/2021
# program: has the intention of taking in a UPC-A barcode and outputting
# which numbers it comprises

import imageio
from positionOfBlackBars import PositionOfBlackBars
from numberIdentifier import NumberIdentifier
from seconddHalfNumberIdentifier import secondHalfNumberIdentifier
from randomStuff import plotter

pic = imageio.imread('flipped_barcode4.png')

print('Height:{}'.format(pic.shape[0]))
print('Width:{}'.format(pic.shape[1]))


# +the raw data on the position of the black pixels of the barcode,
# I choose a certain height, and what this is is a horizontal slice
# getting the position of the black pixels across
a = PositionOfBlackBars(pic)
raw_position = a.position()
print('Raw position:', raw_position)

# Fills in what are thought to be missing pixel values
missingFilledIn_position = a.rawDataCorrector(raw_position)
print('Missing values filled in:', missingFilledIn_position)

# A list of the difference between values of the filled_in list
calculateTheDifference = a.DifferenceCalculator(missingFilledIn_position)
print('Difference:', calculateTheDifference)

# +Tries to identify where the start guard of the barcode ends and what
# the module width is
change = a.Change(calculateTheDifference)
plot = plotter(change)
print('Change in diff.:', change)

moduleWidth1 = a.IdentifyStartGuard(calculateTheDifference, change)
# +I subtract one overall just as a little margin of safety in case
# pixel values slightly different from moduleWidth exactly.
moduleWidth = moduleWidth1 - 1
print('Module width?:', moduleWidth)

# My attempt at analyzing the 'change' list based on 4 clusters
change1 = a.clustering(change, 4, moduleWidth)

# + A list which is the number of modules in each band of black
# and white, which will be central for this program in identifying
# which number is which in the barcode.
pattern = a.patternWriter(change1, moduleWidth)
print('Pattern:', pattern)

# +This function identifies the numbers inside the pattern for left
# and up to the middle guard.
# The endOfMiddle variable is useful for doing the numbers on the right side of the guard.
numbersInPattern, endOfMiddle, newPattern = NumberIdentifier(pattern).identifyNumbers()
print('New pattern:', newPattern)
#print(numbersInPattern)

# +This just breaks away everything from the left up to the end of
# the middle guard, it just makes it easier for the moment in order to
# identify which numbers are on the right.
secondHalf = secondHalfNumberIdentifier().make2ndHalfPattern(pattern, endOfMiddle)
print('2nd half pattern:', secondHalf)

# + The function which takes in the second half pattern and identifies
# the numbers.
secondHalfPattern = secondHalfNumberIdentifier().identify2ndHalfNumbers(secondHalf)
print(numbersInPattern+secondHalfPattern)

# This has the goal of checking whether the barcode was scanned upside down,
# in which case I flip the list so it can be read by my function from
# earlier.
upsideDownCheck = a.parityDetector(newPattern, numbersInPattern)
newList, a, b = NumberIdentifier(upsideDownCheck).identifyNumbers()
print('new list:', upsideDownCheck)
#if len(newList) < 3:
#    pass
#else:
#    print(newList)

# Under here needs to be worked on.
secondHalf1 = secondHalfNumberIdentifier().make2ndHalfPattern(upsideDownCheck, a)
print(secondHalf1)
secondHalfList = secondHalfNumberIdentifier().identify2ndHalfNumbers(secondHalf1)
print(newList+secondHalfList)
