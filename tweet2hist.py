# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import twitter
from pit import Pit
import re
import numpy as np

config = Pit.get('twitter.com', {'require': 
                                 {'ConsumerKey':",'ConsumerSecret':",
                                  'AccessToken':",'AccessTokenSecret':"}})

api = twitter.Api(config['ConsumerKey'], config['ConsumerSecret'], 
                  config['AccessToken'], config['AccessTokenSecret'])

statuses = api.GetSearch(term='withings', per_page=100, page=25)

data = []
p = re.compile('(My weight|u"体重"): ([0-9\.]+) (lb|kg)')
for status in statuses:
    m = p.match(status.text)
    if m:
        if m.group(3) == 'lb':
            data.append(float(m.group(2))*0.4536)
        else:
            data.append(float(m.group(2)))

ary = np.asarray(data)
fig = plt.figure(1)
plt.subplot(111)
plt.axis([40,160,0,5])
plt.grid(True)
plt.hist(ary, 100)
plt.show()

