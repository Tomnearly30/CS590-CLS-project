# CS590-CLS-project
# "EffectorPrediction.py" is a pipeline which use result from "signalp" for effector prediction of Eukaryotic organism.

#  The Features used for Effector prediction are: AA size within 300 and cys counts >= 4, which you can alter to fit your own purpose.

# Run under Unix or Linux environment. Must preinstall "signalp" and put  "EffectorPrediction.py" in the same directory as "signalp".
# Before running, read "signalp" instruction and set path properly.
# When running "EffectorPrediction.py", use the format like 
#                               'Python EffectorPrediction.py proteindatabase.fasta signalpoutput EffectorPredictionouput' 
# An be sure to have "EffectorPrediction.py" and proteindatabase.fasta in the same fold,too.
