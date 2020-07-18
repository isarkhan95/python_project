import pandas as pd
from StyleFrame import StyleFrame,Styler

# df1 =  pd.read_excel('D:/DSR/BIDW_Daily_load_status_04_14_2020_SO.xlsx',index_col=None)
df2 =  pd.read_excel('D:/DSR/DRR.xlsx',index_col=False,header=None)
# df3 =  pd.read_excel('D:/DSR/Daily_load_status _4_14_2020_INTLAR.xlsx',index_col=None)
df4 =  pd.read_excel('D:/DSR/IURR.xlsx',index_col=False,header=None)
# df5 =  pd.read_excel('D:/DSR/Daily_Status_Report_04_14_2020_AR.xlsx',index_col=None)
final=pd.concat([df2,df4])
# final.to_excel('D:/DSR/final_dsr.xlsx',index=False)

sf = StyleFrame(final)

sf.apply_style_by_indexes(sf[sf['Status'] == 'Running on track'], cols_to_style='Status',
                          styler_obj=Styler(bg_color='green'))
sf.apply_style_by_indexes(sf[sf['Status'] == 'Delayed'], cols_to_style='Status',
                          styler_obj=Styler(bg_color='red'))
sf.apply_style_by_indexes(sf[sf['Status'] == 'Completed'], cols_to_style='Status',
                          styler_obj=Styler(bg_color='green'))
sf.apply_style_by_indexes(sf[sf['Status'] == 'On Hold'], cols_to_style='Status',
                          styler_obj=Styler(bg_color='purple'))

sf.to_excel('D:/DSR/final_dsr.xlsx').save()
sf.apply_headers_style()


