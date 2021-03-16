# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:28:44 2021

@author: Syl
"""

total = 100
TP + TN + FP + FN = 100



TN + TN + FP + FP + 6 = 100
2TN + 2FP = 94

TN + FP = 47

FP = 47 - TN

TP + FN = 53

TP = 53- FN

0.9 = TP/53

#les gens qui restent
TP + FN = TN + FP +6


TP = TN + FP - FN + 6

# Sensibilité
TP / (TP+FN) = 0.9

TP = 0.9*TP + 0.9*FN


#specificité 
TN / (TN + FP) = 0.94

TN = 0.94*TN + 0.94*FP




0.9*TP + 0.9*FN +0.94*TN + 0.94*FP + FP + FN = 100

0.9*TP + 1.9*FN +0.94*TN + 1.94*FP  = 100

# ON cherche en 2 

TP /(TP + FP)
TP / (53 - FN + 47 -TN )
TP / (100 - (FN + TN)) = x 