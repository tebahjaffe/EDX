import numpy as np
from datetime import datetime

def datestrtonum(s):
    s=s.decode('utf-8')
    return datetime.strptime(s,"%m/%d/%y").date().weekday()

def summarize(array,open_,high_,low_,close_):
    monday_open = open_[array[0]]
    week_high = np.max(np.take(high_,array))
    week_low = np.min(np.take(low_,array))
    friday_close = close_[array[-1]]
    return ("AAPL",monday_open,week_high,week_low,friday_close)

dates_,open_,high_,low_,close_=np.loadtxt("/Users/tebahsaboun/Downloads/AAPL.csv",delimiter=",",converters={0:datestrtonum},usecols=(0,1,2,3,4),skiprows=1,unpack=True)

dates_=dates_[13:29]
close_=close_[13:29]

first_monday = np.ravel(np.where(dates_ == 0))[0]
last_friday = np.ravel(np.where(dates_ == 4))[-1]

week_indices = np.arange(first_monday,last_friday+1)
week_indices = np.split(week_indices,3)

# week_indices
 
# [array([1, 2, 3, 4, 5]),
# array([ 6,  7,  8,  9, 10]),
# array([11, 12, 13, 14, 15])]

week_summary=np.apply_along_axis(summarize,1,week_indices,open_,high_,low_,close_)

# week_summary

#array([['AAPL', '0.3995', '0.4141', '0.3684', '0.4652'],
#      ['AAPL', '0.4323', '0.5272', '0.4323', '0.4523'],
#      ['AAPL', '0.5143', '0.5143', '0.4706', '0.4779']],
#     dtype='<U6')


np.savetxt("week_summary.csv",week_summary,delimiter=",",fmt="%s")

close_BHP=np.loadtxt("/Users/tebahsaboun/Downloads/5306_Code/ch4code/ch4code/BHP.csv",delimiter=",",usecols=6)
close_VALE=np.loadtxt("/Users/tebahsaboun/Downloads/5306_Code/ch4code/ch4code/VALE.csv",delimiter=",",usecols=6)

returns_BHP = np.diff(close_BHP)/close_BHP[:-1]
returns_VALE = np.diff(close_VALE)/close_VALE[:-1]

covariance = np.cov(returns_BHP,returns_VALE)
correlation = covariance/(returns_BHP.std()*returns_VALE.std())

difference = close_BHP - close_VALE
avg_diff = np.mean(difference)
dev_diff = np.std(difference)

np.abs(difference - avg_diff) > 2*dev_diff

t = np.arange(len(returns_BHP))

plt.plot(t,returns_BHP,lw=1,label="BHP Returns")
plt.plot(t,returns_VALE,'--',lw=2,label="VALE Returns")