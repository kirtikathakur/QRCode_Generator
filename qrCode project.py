import qrcode
data = 'https://thakurs.biz/'
img = qrcode.make(data)
img.save('C:/Users/kirti/OneDrive/Desktop/UL SCHOOL/CS6361-PYTHON LANGAUGE ENGINEERING/projects_portfolio/myqrcode.png')
