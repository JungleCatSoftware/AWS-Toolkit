import datetime

def printBigHeader( author = 'Jungle Cat Software', package = 'AWS-Toolkit', function = 'Output Formatter' ):
  firstLine = author + ' | ' + package
  firstLineLen = len( firstLine )
  secondLine = function
  secondLineLen = len( secondLine )
  
  longestLineLen = firstLineLen if firstLineLen >= secondLineLen else secondLineLen
  linePadLen = longestLineLen + 2
  headerLineLen = linePadLen + 2

  print('*' * headerLineLen)
  formatStr = '*{{0: ^{}}}*'.format(linePadLen)
  print(formatStr.format(firstLine))
  print(formatStr.format(secondLine))
  print('*' * headerLineLen)

def printSmallHeader( function = 'Output Formatter' ):
  print('\n=={}=='.format(function))

def printStartDateStamp():
  print( 'Begin at {0:%Y-%m-d %H:%M:%S.%f}'.format( datetime.datetime.now() ) )

def printIndented( text, indentLevel = 1 ):
  for line in text.splitlines():
    print( ( '\t' * indentLevel ) + line )

if __name__ == "__main__":
    printBigHeader()
    printSmallHeader()
    printIndented("this is my text")
