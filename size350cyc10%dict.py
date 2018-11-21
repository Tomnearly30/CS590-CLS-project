import sys

### open file ###

def readFASTA(filename):
    with open(filename) as file:
     return file.read().split('>')[1:]

### create dictionary with ID and protein sequence for every protein ###

def dicProtein(filename):

      return{seq.partition('\n')[0]: seq.partition('\n')[2].replace('\n','') for seq in readFASTA(filename)}


#def get_key(dict):

               #return [k for k, v in dict.items() if v >= 0]

### search for protein within 350aa residue ###
    
def sizeevaluation(dict):
    return {k:v for k, v in dict.items() if len(v) <= 350}



### count protein number of dictionary ###
def countgenenumber(dict):
    return len([k for k, v in dict.items() if len(v) >= 0])

### cyc content evaluation, Now standard is 10% of whol sequence###

def cysevaluation(dict):
    return {k:v for k, v in dict.items() if v.count('C')/len(v) >= 0.1}

### main part ###

file = sys.argv[1]

a = readFASTA(file)

print(a[0:2])

b = dicProtein(file)

print(b)


c = sizeevaluation(b)

print(c)

d = cysevaluation(c)

print(d)

print(countgenenumber(b))
print(countgenenumber(c))
print(countgenenumber(d))


