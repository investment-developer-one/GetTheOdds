import time
import random


def outPutCourse( fileName ):

        print('outPutCourse')

        outputfile = open('test.csv', 'a')
        splitFileName = fileName.split('.')
        res = outputfile.write(splitFileName[0] + ',')
        outputfile.close()


def GetTime( i, multiString, filename ):

        print('GetTime')

        while i < len(multiString):
                if multiString[i].find(':')!=-1:
                        testString = multiString[i][:1]
                        print(testString)
                        print(multiString[i])
                        if testString.isdigit():
                                print(multiString[i])
                                outPutCourse(fileName)
                                outputfile = open('test.csv', 'a')
                                res = outputfile.write(multiString[i] +',')
                                outputfile.close()

                                return i
                                
                        
                i += 1
        return i

        


def GetFavAndOdds( i, multiString ):

        print('GetFavAndOdds')

        while i < len(multiString):
                if multiString[i] == "FORECAST":
                        print("Found forecast:", i)
                        outputfile = open('test.csv', 'a')
                        
                        odds = multiString[i+1]
                        oddsSplit = odds.split('/')
                        print('odds split',oddsSplit)
                                               
                        nameAndNewLine = GetName (i+2, multiString)

                        if oddsSplit[0] == 'Evs':
                                res = outputfile.write('1,1,1,')

                        else:
                                res = outputfile.write(oddsSplit[0] + ',')
                                res = outputfile.write(oddsSplit[1] + ',')

                                oddsAsPercent = int(oddsSplit[0])/int(oddsSplit[1])
                                print('odds per',oddsAsPercent)

                                res = outputfile.write( (str(oddsAsPercent)+','))
                        
                        res = outputfile.write(nameAndNewLine)
                        outputfile.close()   
                        print(multiString[i+1])
                        print(multiString[i+2])
                        break
                        return i
                        
                i += 1
        return i


def GetName(index, multiString):        

        print('GetName')

        name  = multiString[index]
        print(multiString[index])
        i = index+1
        while multiString[i].find('/')==-1:
                name += ' '
                name += multiString[i]
                
                i+=1

        name += '\n'
        return name

                
    
      
def getRunners( i, multiString ):

        print('getRunners')

        while i < len(multiString):
                if multiString[i] == 'runners':
                        testString = multiString[i-1]
                        print(testString)                        
                        outputfile = open('test.csv', 'a')
                        res = outputfile.write(testString +',')
                        outputfile.close()

                        return i
                        break
                        
                i += 1
        return i



#************************* Main ***********************/

fileName = 'wolves.TXT'
inputfile = open(fileName)
my_text = inputfile.read()
multiString = my_text.split()


index = 0

count = len(multiString)
print("len",count)

while index < len(multiString):

        index = GetTime( index, multiString, fileName )
        print("index after time",index)
        if index == -1:
            break
        index = getRunners( index, multiString )
        print("index after runners",index)
        if index == -1:
                break
        index = GetFavAndOdds( index, multiString )
        print("index after fav",index)
        if index == -1:
                break
        
        index += 1


print('END')
