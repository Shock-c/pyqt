import random
import re

txt = '_Callback({"dfs":"d"});'
friend_json = txt.replace('_Callback(', '').replace(');', '')
print(friend_json)

