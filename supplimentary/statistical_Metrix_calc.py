"""This code calculates statistical metrics,
   originaly written by Peter A. Rochford, moodified by Rai.M"""

#====Load Required Libraries =========
from collections import OrderedDict
import numpy as np
import pandas as pd
import pickle
from math import sqrt
import skill_metrics as sm
from sys import version_info
from sklearn.metrics import mean_squared_error
#=== Load datasets to be calculated ======
beij  = pd.read_excel(r'/mnt/h/Paper_work/Beijing.xlsx',sheet_name='Sheet1')
chen = pd.read_excel(r'/mnt/h/Paper_work/Chengdu.xlsx',sheet_name='Sheet1')
lang = pd.read_excel(r'/mnt/h/Paper_work/Langtang.xlsx',sheet_name='Sheet1')
newd = pd.read_excel(r'/mnt/h/Paper_work/New_Delhi.xlsx',sheet_name='Sheet1')
kara = pd.read_excel(r'/mnt/h/Paper_work/Pakistan_karachi.xlsx',sheet_name='Sheet1')
uzbe = pd.read_excel(r'/mnt/h/Paper_work/Uzbekistan.xlsx',sheet_name='Sheet1')
#===================================================================================
#===== Dropping/Removing NA values from Dataframe ===========
bei = beij.dropna()
che = chen.dropna()
lan = lang.dropna()
new = newd.dropna()
kar = kara.dropna()
uzb = uzbe.dropna()


stats = OrderedDict()
#===== Variables includedes in dataframe  ============
#===== [Temp_Obs,Temp_Mod  RH_Obs,RH_Mod WS_Obs,WS_Mod]

#===== Calculate all metrics for BEIJING ============
#===  Get RMSE/RMSD =================================
stats['rms_bei_temp'] = sqrt(mean_squared_error(bei.Temp_Obs,bei.Temp_Mod))
stats['rms_bei_rh']   = sqrt(mean_squared_error(bei.RH_Obs,bei.RH_Mod))
stats['rms_bei_ws']   = sqrt(mean_squared_error(bei.WS_Obs,bei.WS_Mod))
#=== Get Mean Bias ==========================================
stats['mb_bei_temp']  = sm.bias(bei.Temp_Obs,bei.Temp_Mod)
stats['mb_bei_rh']    = sm.bias(bei.RH_Obs,bei.RH_Mod)
stats['mb_bei_ws']    = sm.bias(bei.WS_Obs,bei.WS_Mod)
#=== Get Correlation Coeff.=================================
stats['cc_bei_temp']  = np.corrcoef(bei.Temp_Obs,bei.Temp_Mod)[0,1]
stats['cc_bei_rh']    = np.corrcoef(bei.RH_Obs,bei.RH_Mod)[0,1]
stats['cc_bei_ws']    = np.corrcoef(bei.WS_Obs,bei.WS_Mod)[0,1]
#=== Get Standard Deviation =================================
stats['sd_bei_temp']  = np.std(bei.Temp_Mod)
stats['sd_bei_rh']    = np.std(bei.RH_Mod)
stats['sd_bei_ws']    = np.std(bei.WS_Mod)
#=== Get Nash-Sutcliffe efficiency (NSE) =================
stats['nse_bei_temp']  = sm.nse(bei.Temp_Obs,bei.Temp_Mod)
stats['nse_bei_rh']    = sm.nse(bei.RH_Obs,bei.RH_Mod)
stats['nse_bei_ws']    = sm.nse(bei.WS_Obs,bei.WS_Mod)

#===== Calculate all metrics for CHENGDU ============
#===  Get RMSE/RMSD =================================
stats['rms_che_temp'] = sqrt(mean_squared_error(che.Temp_Obs,che.Temp_Mod))
stats['rms_che_rh']   = sqrt(mean_squared_error(che.RH_Obs,che.RH_Mod))
stats['rms_che_ws']   = sqrt(mean_squared_error(che.WS_Obs,che.WS_Mod))
#=== Get Mean Bias ==========================================
stats['mb_che_temp']  = sm.bias(che.Temp_Obs,che.Temp_Mod)
stats['mb_che_rh']    = sm.bias(che.RH_Obs,che.RH_Mod)
stats['mb_che_ws']    = sm.bias(che.WS_Obs,che.WS_Mod)
#=== Get Correlation Coeff.=================================
stats['cc_che_temp']  = np.corrcoef(che.Temp_Obs,che.Temp_Mod)[0,1]
stats['cc_che_rh']    = np.corrcoef(che.RH_Obs,che.RH_Mod)[0,1]
stats['cc_che_ws']    = np.corrcoef(che.WS_Obs,che.WS_Mod)[0,1]
#=== Get Standard Deviation =================================
stats['sd_che_temp']  = np.std(che.Temp_Mod)
stats['sd_che_rh']    = np.std(che.RH_Mod)
stats['sd_che_ws']    = np.std(che.WS_Mod)
#=== Get Nash-Sutcliffe efficiency (NSE) =================
stats['nse_che_temp']  = sm.nse(che.Temp_Obs,che.Temp_Mod)
stats['nse_che_rh']    = sm.nse(che.RH_Obs,che.RH_Mod)
stats['nse_che_ws']    = sm.nse(che.WS_Obs,che.WS_Mod)

#===== Calculate all metrics for LANGTANG ============
#===  Get RMSE/RMSD =================================
stats['rms_lan_temp'] = sqrt(mean_squared_error(lan.Temp_Obs,lan.Temp_Mod))
stats['rms_lan_rh']   = sqrt(mean_squared_error(lan.RH_Obs,lan.RH_Mod))
stats['rms_lan_ws']   = sqrt(mean_squared_error(lan.WS_Obs,lan.WS_Mod))
#=== Get Mean Bias ==========================================
stats['mb_lan_temp']  = sm.bias(lan.Temp_Obs,lan.Temp_Mod)
stats['mb_lan_rh']    = sm.bias(lan.RH_Obs,lan.RH_Mod)
stats['mb_lan_ws']    = sm.bias(lan.WS_Obs,lan.WS_Mod)
#=== Get Correlation Coeff.=================================
stats['cc_lan_temp']  = np.corrcoef(lan.Temp_Obs,lan.Temp_Mod)[0,1]
stats['cc_lan_rh']    = np.corrcoef(lan.RH_Obs,lan.RH_Mod)[0,1]
stats['cc_lan_ws']    = np.corrcoef(lan.WS_Obs,lan.WS_Mod)[0,1]
#=== Get Standard Deviation =================================
stats['sd_lan_temp']  = np.std(lan.Temp_Mod)
stats['sd_lan_rh']    = np.std(lan.RH_Mod)
stats['sd_lan_ws']    = np.std(lan.WS_Mod)
#=== Get Nash-Sutcliffe efficiency (NSE) =================
stats['nse_lan_temp']  = sm.nse(lan.Temp_Obs,lan.Temp_Mod)
stats['nse_lan_rh']    = sm.nse(lan.RH_Obs,lan.RH_Mod)
stats['nse_lan_ws']    = sm.nse(lan.WS_Obs,lan.WS_Mod)

#===== Calculate all metrics for NEW-DELHI ============
#===  Get RMSE/RMSD =================================
stats['rms_new_temp'] = sqrt(mean_squared_error(new.Temp_Obs,new.Temp_Mod))
stats['rms_new_rh']   = sqrt(mean_squared_error(new.RH_Obs,new.RH_Mod))
stats['rms_new_ws']   = sqrt(mean_squared_error(new.WS_Obs,new.WS_Mod))
#=== Get Mean Bias ==========================================
stats['mb_new_temp']  = sm.bias(new.Temp_Obs,new.Temp_Mod)
stats['mb_new_rh']    = sm.bias(new.RH_Obs,new.RH_Mod)
stats['mb_new_ws']    = sm.bias(new.WS_Obs,new.WS_Mod)
#=== Get Correlation Coeff.=================================
stats['cc_new_temp']  = np.corrcoef(new.Temp_Obs,new.Temp_Mod)[0,1]
stats['cc_new_rh']    = np.corrcoef(new.RH_Obs,new.RH_Mod)[0,1]
stats['cc_new_ws']    = np.corrcoef(new.WS_Obs,new.WS_Mod)[0,1]
#=== Get Standard Deviation =================================
stats['sd_new_temp']  = np.std(new.Temp_Mod)
stats['sd_new_rh']    = np.std(new.RH_Mod)
stats['sd_new_ws']   = np.std(new.WS_Mod)
#=== Get Nash-Sutcliffe efficiency (NSE) =================
stats['nse_new_temp']  = sm.nse(new.Temp_Obs,new.Temp_Mod)
stats['nse_new_rh']    = sm.nse(new.RH_Obs,new.RH_Mod)
stats['nse_new_ws']    = sm.nse(new.WS_Obs,new.WS_Mod)

#===== Calculate all metrics for KARACHI ============
#===  Get RMSE/RMSD =================================
stats['rms_kar_temp'] = sqrt(mean_squared_error(kar.Temp_Obs,kar.Temp_Mod))
stats['rms_kar_rh']   = sqrt(mean_squared_error(kar.RH_Obs,kar.RH_Mod))
stats['rms_kar_ws']   = sqrt(mean_squared_error(kar.WS_Obs,kar.WS_Mod))
#=== Get Mean Bias ==========================================
stats['mb_kar_temp']  = sm.bias(kar.Temp_Obs,kar.Temp_Mod)
stats['mb_kar_rh']    = sm.bias(kar.RH_Obs,kar.RH_Mod)
stats['mb_kar_ws']    = sm.bias(kar.WS_Obs,kar.WS_Mod)
#=== Get Correlation Coeff.=================================
stats['cc_kar_temp']  = np.corrcoef(kar.Temp_Obs,kar.Temp_Mod)[0,1]
stats['cc_kar_rh']    = np.corrcoef(kar.RH_Obs,kar.RH_Mod)[0,1]
stats['cc_kar_ws']    = np.corrcoef(kar.WS_Obs,kar.WS_Mod)[0,1]
#=== Get Standard Deviation =================================
stats['sd_kar_temp']  = np.std(kar.Temp_Mod)
stats['sd_kar_rh']    = np.std(kar.RH_Mod)
stats['sd_kar_ws']    = np.std(kar.WS_Mod)
#=== Get Nash-Sutcliffe efficiency (NSE) =================
stats['nse_kar_temp']  = sm.nse(kar.Temp_Obs,kar.Temp_Mod)
stats['nse_kar_rh']    = sm.nse(kar.RH_Obs,kar.RH_Mod)
stats['nse_kar_ws']    = sm.nse(kar.WS_Obs,kar.WS_Mod)

#===== Calculate all metrics for UZBEKISTAN ============
#===  Get RMSE/RMSD =================================
stats['rms_uzb_temp'] = sqrt(mean_squared_error(uzb.Temp_Obs,uzb.Temp_Mod))
stats['rms_uzb_rh']   = sqrt(mean_squared_error(uzb.RH_Obs,uzb.RH_Mod))
stats['rms_uzb_ws']   = sqrt(mean_squared_error(uzb.WS_Obs,uzb.WS_Mod))
#=== Get Mean Bias ==========================================
stats['mb_uzb_temp']  = sm.bias(uzb.Temp_Obs,uzb.Temp_Mod)
stats['mb_uzb_rh']    = sm.bias(uzb.RH_Obs,uzb.RH_Mod)
stats['mb_uzb_ws']    = sm.bias(uzb.WS_Obs,uzb.WS_Mod)
#=== Get Correlation Coeff.=================================
stats['cc_uzb_temp']  = np.corrcoef(uzb.Temp_Obs,uzb.Temp_Mod)[0,1]
stats['cc_uzb_rh']    = np.corrcoef(uzb.RH_Obs,uzb.RH_Mod)[0,1]
stats['cc_uzb_ws']    = np.corrcoef(uzb.WS_Obs,uzb.WS_Mod)[0,1]
#=== Get Standard Deviation =================================
stats['sd_uzb_temp']  = np.std(uzb.Temp_Mod)
stats['sd_uzb_rh']    = np.std(uzb.RH_Mod)
stats['sd_uzb_ws']    = np.std(uzb.WS_Mod)
#=== Get Nash-Sutcliffe efficiency (NSE) =================
stats['nse_uzb_temp']  = sm.nse(uzb.Temp_Obs,uzb.Temp_Mod)
stats['nse_uzb_rh']    = sm.nse(uzb.RH_Obs,uzb.RH_Mod)
stats['nse_uzb_ws']    = sm.nse(uzb.WS_Obs,uzb.WS_Mod)


# Write statistics to Excel file.
filename = 'all_met.xlsx'
sm.write_stats(filename,stats,overwrite=True)

