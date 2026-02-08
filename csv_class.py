import urllib.request

goog_url = 'https://drive.google.com/uc?id=1OT84-j5J5z2tHoUvikJtoJFInWmlyYzY&export=download'
def download_stock_data(csv_url):
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line +'\n')
    fx.close()

download_stock_data(goog_url)