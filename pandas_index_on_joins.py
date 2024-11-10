import numpy as np
import pandas as pd

registration=pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bob','Charlie','David']})
registration=registration.set_index('name')
logins=pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bob']})

print(pd.merge(registration,logins,left_index=True,right_on='name',how='right'))