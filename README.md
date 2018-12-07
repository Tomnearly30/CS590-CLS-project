# CS590-CLS-project

# The whole project contains two parts, the first one is Effector Prediction, the second one is protein comparison.

##### First Part #####
# "EffectorPrediction.py" is a pipeline which use result from "signalp" for effector prediction of Eukaryotic organism.

#  The Features used for here are: amino acid number within 300 and cys counts >= 4, which you can alter to fit your own purpose.

# Run under Unix or Linux environment. Must preinstall "signalp" and put  "EffectorPrediction.py" in the same directory as "signalp".
# Before running, read "signalp" instruction and set path properly.
# When running "EffectorPrediction.py", use the format like:
#                               >Python EffectorPrediction.py aaa.fasta tempOUTPUT finalOUTPUT 
# And be sure to have "EffectorPrediction.py" and proteindatabase.fasta in the same fold,too.

##### Second Part #####
# "compare.py" is the comparison script for multiple sequence overall similarity comparison. 
# This python program accepts two fasta format files and gives the similarity score.
# It excludes labels automatically.

# on the terminal, you would use it like this:

# >>compare.py fasta1.txt fasta2.txt

# Output would look like this:

# "Similarity of the two given files is:"
# "1.0"

# Where the number would range from 0 to 1.0
