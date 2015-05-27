import datetime

def printBigHeader( author = 'Jungle Cat Software', package = 'AWS-Toolkit', function = 'Output Formatter' ):
  lineOne = author + ' | ' + package
  lineOneLen = len(lineOne)
  lineTwoLen = len(function)

  biggestLen = lineOneLen if lineOneLen >= lineTwoLen else lineTwoLen

  # Line 1
  print('*' * (biggestLen+4))

  def printLine( line = '' ):
    print('* ', end = '')
    spaceNeeded = (biggestLen - len(line))
    lSpaceNeeded = (spaceNeeded // 2)
    print(' ' * lSpaceNeeded, end = '')
    print(line, end = '')
    rSpaceNeeded = (spaceNeeded - lSpaceNeeded)
    print(' ' * rSpaceNeeded, end = '')
    print(' *')

  # Line 2
  printLine(lineOne)

  # Line 3
  printLine(function)

  # Line 4
  print('*' * (biggestLen+4))

def printSmallHeader( function = 'Output Formatter' ):
  print('\n==' + function + '==')

def printStartDateStamp():
  print('Begin at ' + datetime.datetime.now().__str__())

def printIndented(text,indentLevel=1):
  for line in text.splitlines():
    print(('\t' * indentLevel) + line)
