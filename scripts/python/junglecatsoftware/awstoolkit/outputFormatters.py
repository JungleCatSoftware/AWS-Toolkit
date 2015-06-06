import datetime

def printBigHeader( author = 'Jungle Cat Software', package = 'AWS-Toolkit', function = 'Output Formatter' ):
  firstLine = author + ' | ' + package
  firstLineLen = len( firstLine )
  secondLine = function
  secondLineLen = len( secondLine )

  longestLineLen = firstLineLen if firstLineLen >= secondLineLen else secondLineLen
  linePadLen = longestLineLen + 2
  headerLineLen = linePadLen + 2

  print( ( '{0:*^' + str( headerLineLen ) + '}' ).format( '' ) )
  print( ( '*{0: ^' + str( linePadLen ) + '}*' ).format( firstLine ) )
  print( ( '*{0: ^' + str( linePadLen ) + '}*' ).format( secondLine ) )
  print( ( '{0:*^' + str( headerLineLen ) + '}' ).format( '' ) )

def printSmallHeader( function = 'Output Formatter' ):
  print('\n==' + function + '==')

def printStartDateStamp():
  print( 'Begin at {0:%Y-%m-d %H:%M:%S.%f}'.format( datetime.datetime.now() ) )

def printIndented(text,indentLevel=1):
  for line in text.splitlines():
    print(('\t' * indentLevel) + line)
