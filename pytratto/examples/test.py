# -*- coding:utf-8 -*-

from pytratto.systems.Systems import *
from pytratto.connectivity.Connectivity import *


# telnet to a cisco switch
m = SystemProfiles['IOS']

# change 20 for 22 and telnet for ssh for ssh enabled devices
s = Session("10.251.6.51", 22, "telnet", m)
s.login("yourusername", "yourpassword")

# if you need to issue an "enable" command
s.escalateprivileges("yourenablepassword")

show_clock_results = s.sendcommand("show clock")
print(show_clock_results)

s.logout()
