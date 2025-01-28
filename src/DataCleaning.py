import pandas as pd
import numpy as np

fraud = pd.read_csv("../data/fraud.csv", delimiter=";")
non_fraud = pd.read_csv("../data/non-fraud.csv", delimiter=";")

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

fraud.drop("Telesrvc", axis=1, inplace=True)
non_fraud.drop("Telesrvc", axis=1, inplace=True)

fraud.cell_id = fraud.cell_id.fillna(method='ffill')
fraud.MU_HANDSET_MOBILE_TECH = fraud.MU_HANDSET_MOBILE_TECH.fillna(method='ffill')
non_fraud.cell_id = non_fraud.cell_id.fillna(method='ffill')
non_fraud.MU_HANDSET_DUAL_SIM = non_fraud.MU_HANDSET_DUAL_SIM.fillna(method='ffill')
non_fraud.MU_HANDSET_MOBILE_TECH = non_fraud.MU_HANDSET_MOBILE_TECH.fillna(method='ffill')

fraud.sort_values(by=['Charging_Tm']).to_csv("../data/processed/1-DataCleaning/fraud.csv", index=False)
non_fraud.sort_values(by=['Charging_Tm']).to_csv("../data/processed/1-DataCleaning/non_fraud.csv", index=False)