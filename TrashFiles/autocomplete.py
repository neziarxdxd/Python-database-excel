words=[ 'abnormal',
  'arm-wrestling',
  'absolute',
  'airplane',
  'airport',
  'amazing',
  'apple',
  'ball' ]



news=[]
text = ""
text= "".join(i for i in text if i.isalpha())

for i in words:
    if (i.lower()).startswith(text):
        news.append(i)

if len(news)==0:
    print(words[0:5])
else:
    print(news[0:5])


