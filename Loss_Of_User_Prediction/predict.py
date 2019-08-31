# This Python 3 environment comes with many helpful analytics libraries installed
# For example, here's several helpful packages to load in 

import pandas as pd
import numpy as np
import random
# submit CSV to hdfs
import submittools as sub
import re  
# Input data files are available with function competitionData
from Turing import competitionData, userData
train=pd.read_csv(competitionData('/upload-dataset/�������ű���У�������㷨��1/�������ű���У�������㷨��1���ݼ�/train.csv'))
test=pd.read_csv(competitionData('/upload-dataset/�������ű���У�������㷨��1/�������ű���У�������㷨��1���ݼ�/test.csv'))
sample=pd.read_csv(competitionData('/upload-dataset/�������ű���У�������㷨��1/�������ű���У�������㷨��1���ݼ�/sample.csv'))
lost_user_info=pd.read_csv(competitionData('/upload-dataset/�������ű���У�������㷨��1/�������ű���У�������㷨��1���ݼ�/lost_user_info.csv'))
# print("ѵ����������������")
# print(train.shape[0],train.shape[1])

#������ϴ
# my_train=train[train.dtypes[train.dtypes!=np.object].index]
my_train = train.copy()
# print(my_train)#ѵ�����Ա���
re_train=my_train.pop('IS_LOST')
#print(re_train)#ѵ�����û��Ƿ���ʧ���
# print(my_train.columns.values.tolist())
del my_train['USER_ID']
del my_train['USER_ID_OLD']
del my_train['CUST_ID']
del my_train['DEVICE_NUMBER']
# del my_train['SERVICE_TYPE']
# del my_train['SERVICE_TYPE_OLD']
del my_train['LEVEL_A']
del my_train['CYCLE_ID'] #ɾ��ת��ʱ��
#ɾ����������
# del my_train['PRODUCT_ID']
# del my_train['PRODUCT_CLASS']

my_train.loc[my_train[my_train['USER_STATUS'] == '**'].index,['USER_STATUS']] = 11
my_train.loc[my_train[my_train['TRANS_ID'] != 0].index,['TRANS_ID']] = 1


#SERVICE_TYPE�������ַ���
STtmplist = []
for seroldtmp in my_train['SERVICE_TYPE']:
  STtmplist.append(re.sub("\D","",seroldtmp))
my_train['SERVICE_TYPE'] = STtmplist  
#SERVICE_TYPE_OLD�������ַ���
STOtmplist = []
for seroldtmp in my_train['SERVICE_TYPE_OLD']:
  STOtmplist.append(re.sub("\D","",seroldtmp))
my_train['SERVICE_TYPE_OLD'] = STOtmplist  
# print(my_train['SERVICE_TYPE'])

my_train['TOTAL_TIMES'] = round(my_train['TOTAL_TIMES'])
my_train['INTER_TIMES'] = round(my_train['INTER_TIMES'])
my_train['TOTAL_SMS'] = round(my_train['TOTAL_SMS'])
my_train['RATIO_FLUX'] = round(my_train['RATIO_FLUX'])
my_train['TOTAL_FLUX'] = round(my_train['TOTAL_FLUX'])
my_train['INTER_FLUX'] = round(my_train['INTER_FLUX'])
del my_train['FLUX_2G']
del my_train['FLUX_3G']
del my_train['FLUX_4G']
my_train['RATIO_FEE'] = round(my_train['RATIO_FEE'])
del my_train['TOTAL_FEE']
del my_train['TOTAL_TIME_VAR']
del my_train['IMEI']
del my_train['MANU_NAME']
del my_train['CHNL_ID']
#ɾ������
del my_train['COMP_START_DATE']
del my_train['COMP_END_DATE']
del my_train['ACT_START_DATE']
del my_train['ACT_END_DATE']
# my_train = my_train.drop(my_train[my_train.CERT_AGE == 0].index)#ɾ������Ϊ0����
# my_train.loc[my_train[my_train['CERT_AGE'] == 0].index,['CERT_AGE']] = random.randint(25,50)   #�޸�����Ϊ0����
# my_train['IMEI']/= 100000000000
# my_train.loc[my_train[my_train['ACT_START_DATE']>201806010].index,['ACT_START_DATE']] /= 1000000#��Լʱ��淶��
# my_train.loc[my_train[my_train['ACT_END_DATE']>201806010].index,['ACT_END_DATE']] /= 1000000#��Լʱ��淶��
# my_train.loc[my_train[my_train['CALL_RING']<0].index,['CALL_RING']] = 0 #����Ȧ������Ϊ0
# del my_train['IS_ACCT_AFT']

my_test=test[my_train.columns]
#test���Լ��淶��
#С��ȡ��
my_test.loc[my_test[my_test['USER_STATUS'] == '**'].index,['USER_STATUS']] = 11
my_test.loc[my_test[my_test['TRANS_ID'] != 0].index,['TRANS_ID']] = 1
my_test['TOTAL_TIMES'] = round(my_test['TOTAL_TIMES'])
my_test['INTER_TIMES'] = round(my_test['INTER_TIMES'])
my_test['TOTAL_SMS'] = round(my_test['TOTAL_SMS'])
my_test['RATIO_FLUX'] = round(my_test['RATIO_FLUX'])
my_test['TOTAL_FLUX'] = round(my_test['TOTAL_FLUX'])
my_test['INTER_FLUX'] = round(my_test['INTER_FLUX'])
my_test['RATIO_FEE'] = round(my_test['RATIO_FEE'])
#SERVICE_TYPE�������ַ���
STtmplist = []
for seroldtmp in my_test['SERVICE_TYPE']:
  STtmplist.append(re.sub("\D","",seroldtmp))
my_test['SERVICE_TYPE'] = STtmplist  
#SERVICE_TYPE_OLD�������ַ���
STOtmplist = []
for seroldtmp in my_test['SERVICE_TYPE_OLD']:
  STOtmplist.append(re.sub("\D","",seroldtmp))
my_test['SERVICE_TYPE_OLD'] = STOtmplist  
# my_test.loc[my_test[my_test['CERT_AGE'] == 0].index,['CERT_AGE']] = random.randint(25,50)   #�޸�����Ϊ0����
# my_test['IMEI'] /= 100000000000
# my_test.loc[my_test[my_test['ACT_START_DATE']>201806010].index,['ACT_START_DATE']] /= 1000000#��Լʱ��淶��
# my_test.loc[my_test[my_test['ACT_END_DATE']>201806010].index,['ACT_END_DATE']] /= 1000000#��Լʱ��淶��
# my_test.loc[my_test[my_test['CALL_RING']<0].index,['CALL_RING']] = 0 #����Ȧ������Ϊ0

print("ѵ����������������")
print(my_train.shape[0],my_train.shape[1])
print("���Լ�������������")
print(my_test.shape[0],my_test.shape[1])
# print(my_test['CERT_AGE'])


print("ѵ����������������")
print(my_train.shape[0],my_train.shape[1])
print(my_test.shape[0],my_test.shape[1])
# print(my_test['CERT_AGE'])hape[1])
print("���Լ�������������")


#������ ������ɭ��+��������+KFlod������֤
from sklearn.ensemble import RandomForestClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold
random_forest_classifier = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=20, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=-1,
            oob_score=False, random_state=False, verbose=0, warm_start=True)
parameter_grid = {'n_estimators': [37,39,42],
                  'criterion': ['gini','entropy'],
                  'max_features': [15,16,17],
                  'warm_start':[True,False]}
cross_validation = StratifiedKFold(re_train, n_folds=10,shuffle=True,random_state=2000)
grid_search = GridSearchCV(random_forest_classifier,
                           param_grid=parameter_grid,
                           cv=cross_validation)
grid_search.fit(my_train, re_train)
predict = grid_search.predict(my_test)


submits=test[['USER_ID']]
# submits['IS_LOST']=prediction_xgb
submits['IS_LOST']=predict
submits['IS_LOST']=submits['IS_LOST'].apply(lambda x: int(1) if x>0.5 else int(0))
print(submits['IS_LOST'].value_counts())

try:

	sub.submit(submits, notebookId)  #A��

except NameError:

	sub.submit(submits) #B��