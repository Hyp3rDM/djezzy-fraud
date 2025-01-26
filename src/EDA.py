import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

fraud = pd.read_csv("../data/fraud.csv", delimiter=";")
non_fraud = pd.read_csv("../data/non-fraud.csv", delimiter=";")

# Enforcing Data Types
fraud.replace("?", np.nan, inplace=True)
non_fraud.replace("?", np.nan, inplace=True)

fraud.cell_id = fraud.cell_id.astype("float64")
non_fraud.cell_id = non_fraud.cell_id.astype("float64")

fraud.Charging_Tm = pd.to_datetime(fraud.Charging_Tm)
non_fraud.Charging_Tm = pd.to_datetime(non_fraud.Charging_Tm)

fraud.Call_Type = fraud.Call_Type.astype('category')
fraud.DESTINATION_CAT = fraud.DESTINATION_CAT.astype('category')
fraud.MU_Device_type_Segment = fraud.MU_Device_type_Segment.astype('category')
fraud.MU_HANDSET_MOBILE_TECH = fraud.MU_HANDSET_MOBILE_TECH.astype('category')
non_fraud.Call_Type = non_fraud.Call_Type.astype('category')
non_fraud.DESTINATION_CAT = non_fraud.DESTINATION_CAT.astype('category')
non_fraud.MU_HANDSET_DUAL_SIM = non_fraud.MU_HANDSET_DUAL_SIM.astype('category')
non_fraud.MU_Device_type_Segment = non_fraud.MU_Device_type_Segment.astype('category')
non_fraud.MU_HANDSET_MOBILE_TECH = non_fraud.MU_HANDSET_MOBILE_TECH.astype('category')
