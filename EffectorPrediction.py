import sys
import os




##########################################################################################################################
##########################################################################################################################

#####  Module1 signalP import and result analysis #####

### open SP prediction Summaryfile ###

def readSummary(filename):
    with open(filename) as file:
     return file.read().split('#')[2:]

### create dictionary with ID and protein sequence for every protein ###

def dictSPP(filename):

     return{seq.split('\n')[6].partition('\t')[0].partition('Name=')[2]: seq.split('\n')[6] for seq in readSummary(filename)}



### Signal peptide detection ###
    
def SPdetection(dict):
    return {k:v.find('YES') for k, v in dict.items() if v.find('YES') >= 0}



### count protein number of dictionary ###

def countgenenumber1(dict):
    return len([k for k, v in dict.items() if v >= 0])

def countgenenumber2(dict):
    return len([k for k, v in dict.items() if len(v) >= 0])

#########################################################################################################################
#########################################################################################################################

#####  Module2 size and cys analysis #####

### open FASTA file ###

def readFASTA(filename):
    with open(filename) as file:
     return file.read().split('>')[1:]

### create dictionary with ID and protein sequence for every protein ###

def dicProtein(filename):

      return{seq.partition('\n')[0].partition(' ')[0]: seq.partition('\n')[2].replace('\n','') for seq in readFASTA(filename)}


### search for protein within 300aa residue ###
    
def sizeevaluation(dict):
    return {k:v for k, v in dict.items() if len(v) <= 300}

### cyc content evaluation, Now standard is 4cyc in whole sequence###

def cysevaluation(dict):
    return {k:v for k, v in dict.items() if v.count('C') >= 4}

#########################################################################################################################
#########################################################################################################################


#####  Module3 Dictionary comparing #####

def shared_keys(dict1,dict2):
   return{k:dict2.get(k) for k in dict1 if k in dict2}

#########################################################################################################################
#########################################################################################################################

### main part ###

### import local signalP software ###

arg1 = sys.argv[1]
arg2 = sys.argv[2]
outputname = sys.argv[3]
cmd = './signalp -t euk -f summary' + ' '+arg1 + '>' + ' ' + arg2
SPresult = os.system(cmd)

file = sys.argv[2]

### Output fasta ###
e = outputname + '.txt' 

f = open(e,"a")### Create new output file###

SPdict = SPdetection(dictSPP(file)) ### dictionary 1 after SP prediction

cyssizedict = cysevaluation(sizeevaluation(dicProtein(arg1))) ### dictionary 2 after size and cys analysis

finaldict = shared_keys(SPdict,cyssizedict) ### common subset of both dictionaries ###

for key in finaldict.keys():   
        f.write(">" + key )
        f.write('\r\n')
        f.write(finaldict.get(key))
        f.write('\r\n')       

f.close()

print(countgenenumber1(SPdict))

print(countgenenumber2(cyssizedict))

print(countgenenumber2(finaldict))







