import numpy as np
import pandas as pd

registration=pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bob','Charlie','David']})

logins=pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bob']})

print(pd.merge(registration,logins,how='right',on='name'))