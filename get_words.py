import re

import pandas as pd
print('-'*99)
with open('./py/js_basice.txt') as fin:
    content = fin.read()
# print(content.split())

# re.split
words = re.split(r'[\s.()-?]+', content)
print(words)

# pandas as pd
print(pd.Series(words).value_counts()[:30])
print('-'*99)