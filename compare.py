#-----sequenceCompare-----
#This is used to find the similarity percentage of two fasta files 

#ACCEPTING INPUT FILES
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]

#OPENING FIRST FILE AND EXCLUDING LABELS
with open(file1) as f:
  fasta1 = f.readlines()
i=0
while i < len(fasta1):
    if fasta1[i].find(">hsa") > -1:
        fasta1.pop(i)
    i=i+1

#REMOVING SPACES AND CONCATENATING FIRST FILE
fasta1 = [x.strip() for x in fasta1]
concat1 = "".join(fasta1)

#OPENING SECOND FILE AND EXCLUDING LABELS
with open(file2) as f:
  fasta2 = f.readlines()
i=0
while i < len(fasta2):
    if fasta2[i].find(">hsa") > -1:
        fasta2.pop(i)
    i=i+1

#REMOVING SPACES AND CONCATENATING SECOND FILE
fasta2 = [x.strip() for x in fasta2]
concat2 = "".join(fasta2)

#IMPORTING SequenceMatcher FROM difflib
from difflib import SequenceMatcher

#CALCULATING OVERALL SIMILARITY SCORE
score = SequenceMatcher(None, concat1, concat2)

#OUTPUT

print("Similarity of the two given files is:")
print(score.ratio())