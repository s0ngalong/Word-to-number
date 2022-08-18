#a dictionary definition that supports up to vigintillion
DBBaseDict = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
        #'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'ninteen':19}
DBExtDic = {'ten':DBBaseDict['one']+DBBaseDict['zero'],
        'eleven':DBBaseDict['one']*2,
        'twelve':DBBaseDict['one']+DBBaseDict['two'],
        'thirteen':DBBaseDict['one']+DBBaseDict['three'],
        'fourteen':DBBaseDict['one']+DBBaseDict['four'],
        'fifteen':DBBaseDict['one']+DBBaseDict['five'],
        'sixteen':DBBaseDict['one']+DBBaseDict['six'],
        'seventeen':DBBaseDict['one']+DBBaseDict['seven'],
        'eighteen':DBBaseDict['one']+DBBaseDict['eight'],
        'nineteen':DBBaseDict['one']+DBBaseDict['nine'],
        'twenty':DBBaseDict['two']+DBBaseDict['zero'],
        'thirty':DBBaseDict['three']+DBBaseDict['zero'],
        'forty':DBBaseDict['four']+DBBaseDict['zero'],
        'fifty':DBBaseDict['five']+DBBaseDict['zero'],
        'sixty':DBBaseDict['six']+DBBaseDict['zero'],
        'seventy':DBBaseDict['seven']+DBBaseDict['zero'],
        'eighty':DBBaseDict['eight']+DBBaseDict['zero'],
        'ninety':DBBaseDict['nine']+DBBaseDict['zero'],
        'hundred':DBBaseDict['zero']*2,
        'thousand':DBBaseDict['zero']*3,
        'million':DBBaseDict['zero']*6,
        'billion':DBBaseDict['zero']*9,
        'trillion':DBBaseDict['zero']*12,
        'quadrillion':DBBaseDict['zero']*15,
        'quintillion':DBBaseDict['zero']*18,
        'sextillion':DBBaseDict['zero']*21,
        'septillion':DBBaseDict['zero']*24,
        'octillion':DBBaseDict['zero']*27,
        'nonillion':DBBaseDict['zero']*30,
        'decillion':DBBaseDict['zero']*33,
        'undecillion':DBBaseDict['zero']*36,
        'duodecillion':DBBaseDict['zero']*39,
        'tredecillion':DBBaseDict['zero']*42,
        'quattuordecillion':DBBaseDict['zero']*45,
        'quindecillion':DBBaseDict['zero']*48,
        'sexdecillion':DBBaseDict['zero']*51,
        'septendecillion':DBBaseDict['zero']*54,
        'octodecillion':DBBaseDict['zero']*57,
        'novendecillion':DBBaseDict['zero']*60,
        'vigintillion':DBBaseDict['zero']*63
        }

def convert(Nums):
    CNum = ''
    LTrack = []
    for I in Nums:
        if I in DBBaseDict.keys():
            CNum = CNum+DBBaseDict[I]
            CNum = CNum+'.'
            LTrack.append(DBBaseDict[I].count('0'))
        elif I in DBExtDic.keys():
            CNum = CNum+DBExtDic[I]
            LTrack.append(DBExtDic[I].count('0'))
            CNum = CNum+'.'
    
    CNum = CNum.split('.')
    del CNum[-1]
    #print(CNum)

    MathParts = []
    C = 0
    for LT in range(len(LTrack)):
        try:
            if LTrack[LT] > 1:
                if int(CNum[LT]) == 0 and int(MathParts[-1]) in range(1,20):
                    MathParts[-1] = MathParts[-1]+CNum[LT]
                elif C == 2:
                    MathParts.append(MathParts[-1]+CNum[LT])
                    del MathParts[-2]
                    C = 0
                else:
                    MathParts.append(CNum[LT])
            elif LTrack[LT] == 0:
                if C == 1:
                    C = 2
                else:
                    MathParts.append(CNum[LT])
            elif LTrack[LT] == 1 and int(CNum[LT]) == 0:
                MathParts.append(CNum[LT])
            elif LTrack[LT] == 1 and len(CNum[LT+1]) == 1 and int(CNum[LT+1]) in range(1,10):
                MathParts.append(str(int(CNum[LT])+int(CNum[LT+1])))
                C = 1
            elif LTrack[LT] == 1 and len(CNum[LT+1]) > 1:
                MathParts.append(CNum[LT])
        except IndexError:
            MathParts.append(CNum[LT])
    #print(MathParts)

    MathPartsAssemble = []
    Checker = 0
    for parts in range(len(MathParts)):
        try:
            if Checker == 1:
                Checker = 0
            elif int(MathParts[parts]) == 0:
                MathPartsAssemble[-1] = MathPartsAssemble[-1]+MathParts[parts]
            elif len(MathParts[parts]) == 1:
                MathPartsAssemble.append(MathParts[parts])
            elif MathParts[parts][-2:].count('0') == 2 and len(MathParts[parts]) == 3 and int(MathParts[parts+1][0:2]) > 0 and len(MathParts[parts+1]) < 3:
                MathPartsAssemble.append(str(int(MathParts[parts])+int(MathParts[parts+1][0:2])))
                MathPartsAssemble[-1] = MathPartsAssemble[-1]+MathParts[parts+1][2:]
                Checker = 1
            elif MathParts[parts][-2:].count('0') == 2 and len(MathParts[parts]) == 3 and int(MathParts[parts+1][0:2]) > 0 and len(MathParts[parts+1]) > 2 and int(MathParts[parts+1][3:]) == 0:
                if int(MathParts[parts+1][0]) in range(1,10) and int(MathParts[parts+1][1]) == 0:
                    MathPartsAssemble.append(str(int(MathParts[parts])+int(MathParts[parts+1][0])))
                    MathPartsAssemble[-1] = MathPartsAssemble[-1]+MathParts[parts+1][1:]
                    Checker = 1
                else:
                    MathPartsAssemble.append(str(int(MathParts[parts])+int(MathParts[parts+1][0:2])))
                    MathPartsAssemble[-1] = MathPartsAssemble[-1]+MathParts[parts+1][2:]
                    Checker = 1
            else:
                MathPartsAssemble.append(MathParts[parts])
        except IndexError:
            MathPartsAssemble.append(MathParts[parts])
    
    for _ in range(MathPartsAssemble.count('')):
        MathPartsAssemble.remove('')

        
    #print(MathPartsAssemble)
    FinalNum = 0


    
    for N in range(len(MathPartsAssemble)):
        if FinalNum == 0:
            FinalNum+=int(MathPartsAssemble[N])
        elif int(MathPartsAssemble[N]) == 0:
            FinalNum = int(str(FinalNum)+MathPartsAssemble[N])
        elif int(MathPartsAssemble[N-1]) == 0 and len(MathPartsAssemble[N]) <= len(MathPartsAssemble[N-1]):
            FinalNum+=int(MathPartsAssemble[N])
        elif int(MathPartsAssemble[N-1]) == 0 and len(MathPartsAssemble[N]) > len(MathPartsAssemble[N-1]):
            FinalNum = int(str(FinalNum)+str(MathPartsAssemble[N]))
        elif len(MathPartsAssemble[N]) == 2 and int(MathPartsAssemble[N-1]) > int(MathPartsAssemble[N]) and int(MathPartsAssemble[N-1][-2:]) == 0:
            FinalNum+=int(MathPartsAssemble[N])
        elif len(MathPartsAssemble[N]) == 2:
            FinalNum = int(str(FinalNum)+str(MathPartsAssemble[N]))
        elif FinalNum > int(MathPartsAssemble[N]) and int(str(FinalNum)[-len(MathPartsAssemble[N]):]) == 0:
            FinalNum+=int(MathPartsAssemble[N])
        elif len(MathPartsAssemble[N]) >= len(str(FinalNum)):
            FinalNum = int(str(FinalNum)+str(MathPartsAssemble[N]))
        else:
            FinalNum = int(str(FinalNum)+str(MathPartsAssemble[N]))
        
    print(FinalNum)

#except the user input and resolve the simple conversions first
def numbers():
    N = input('Please input a real number in words up to vigintillion: ')
    if ' ' in N:
        tmp = N.split(' ')
        convert(tmp)
    elif N.lower() in DBBaseDict.keys():
        print(DBBaseDict[N])
    elif N.lower() in DBExtDic.keys():
        print(DBExtDic[N])
    else:
        print('Oh, you typed an incorrect number please try again.')
numbers()