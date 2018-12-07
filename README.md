# CS590-CLS-project

# The whole project contains two parts, the first one is Effector Prediction, the second one is protein comparison.

##### First Part #####
# "EffectorPrediction.py" is a pipeline which use result from "signalp" for effector prediction of Eukaryotic organism.

#  The Features used for here are: amino acid number within 300 and cys counts >= 4, which you can alter to fit your own purpose.

# Run under Unix or Linux environment. Must preinstall "signalp"
# You can download "signalp" from http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?signalp.

# Before running, You'll need to unzip signalp-4.1f.Linux.tar.gz on your local server. Then Read "signalp-4.1.readme". Use vim to open "signalp", set the path as your install path and change "max number of sequences per run" into 30000.
# Put "EffectorPrediction.py" and proteindatabase.fasta into "signalp" install directory.
# When running "EffectorPrediction.py", use the format like:
#                               >Python EffectorPrediction.py proteindatabase.fasta tempOUTPUT finalOUTPUT 

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
