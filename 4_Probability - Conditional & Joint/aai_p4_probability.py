# -*- coding: utf-8 -*-
"""AAI_P4_Probability.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxFHyPC3gsSHvsIozbwQbvm9AXgUiRNR
"""

#Conditional Probability...

def conditional():
  pass_stats=0.15
  pass_codingWStats=0.60
  pass_codingWOStats=0.40
  prob_both=pass_stats*pass_codingWStats

  print("The probability that applicant passes both is",round(prob_both,3))
  prob_coding=(prob_both)+((1-pass_stats)*pass_codingWOStats)
  print("Probability that he/she passes only coding is",round(prob_coding,3))
  stats_given_coding=prob_both/prob_coding
  print("Conditional Probability is",round(stats_given_coding,3))

print("Hey SPC")
conditional()

#Joint Probability...

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()
data=pd.read_csv('/content/dataAAIPRAC4.csv',header=None, names=['x','y'])
sns.jointplot(data['x'],data['y'],kind='kde').plot_joint(sns.scatterplot)
plt.show()