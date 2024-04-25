import pandas as pd
df = pd.read_csv(r'/workspaces/Nursing-Home-Analysis/2021_CostReport_Clean.csv')
df.info(verbose=True)
extracted_columns = df[['State Code', 'Facility Name', 'Number of Beds', 'Inpatient Revenue', 'Net Patient Revenue', 'Less Total Operating Expense', 'Inpatient PPS Amount', 'Allowable Bad Debts', 'Net Income from service to patients']]
extracted_columns.to_csv(r'/workspaces/Nursing-Home-Analysis/2021_CostReport_Extracted.csv', index=False)