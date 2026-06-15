import logging
import numpy as np
logging.basicConfig(level=logging.INFO)
P_Spam = 0.4
P_Normal = 0.6
P_Trung_Spam = 0.8
P_Thuong_Spam = 0.7
P_Trung_Normal = 0.1
P_Thuong_Normal = 0.05

score_spam = np.log(P_Spam) + np.log(P_Trung_Spam) + np.log(P_Thuong_Spam)
score_normal =  np.log(P_Normal) + np.log(P_Trung_Normal) + np.log(P_Thuong_Normal)
logging.info("score_spam: " + str(score_spam))
logging.info("score_normal: " + str(score_normal))
if score_spam > score_normal:
    logging.info("Probability of spam is greater than normal")
else :
    logging.info("Probability of spam is less than normal")