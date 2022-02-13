# разделение переменной
import re
datetime='2016-04-11 20:59:03'

pattern1 = '\d{4}-\d\d-\d\d'
pattern2 = '\d\d:\d\d:\d\d'
testString = datetime
date = re.findall(pattern1, testString)
time = re.findall(pattern2, testString)

print('date = ' + str(date), 'time = ' + str(time))
