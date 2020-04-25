import tkinter as tk
from PIL import ImageTk
import urllib.request
import webbrowser
import json
root = tk.Tk()

url = "https://api.nomics.com/v1/currencies/ticker?key=9d876aa144dc791bff11cb5b07a01d3d&" \
      "ids=BTC,ETH,XRP&interval=1d,30d&convert=USD"


class nomics_api:

    def crypto_json(self, url):
        return urllib.request.urlopen(url).read()

    def conv_object(self):
        obj = json.loads(nomics.crypto_json(url))
        return json.dumps(obj, indent=2)


nomics = nomics_api()


def link():
    return webbrowser.open("https://cryptowat.ch")


FILENAME = r"C:\Users\HP\stockimage.jpg"
root.title('CRYPTO_PRICE_IN_REAL_TIME')
root.geometry("780x439")
canvas = tk.Canvas(root, width=700, height=439)
canvas.pack()
tk_img = ImageTk.PhotoImage(file=FILENAME)
canvas.create_image(125, 125, image=tk_img)
quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red")
quit_button_window = canvas.create_window(450, 300, anchor='nw', window=quit_button)

web_link = tk.Button(root, text="visit CRYPTO WATCH", command=link, anchor='w', width=30, bg="green")
web_link_window = canvas.create_window(290, 10, anchor='nw', window=web_link)


def live_price():
    st = json.loads(nomics.crypto_json(url))

    btc_cap = tk.Label(root, text="BTC MARKET-CAP : " + "\r" + st[0]['market_cap'] + " USD")
    canvas.create_window(10, 80, anchor='nw', window=btc_cap)

    eth_cap = tk.Label(root, text="ETH MARKET-CAP : " + "\r" + st[1]['market_cap'] + " USD")
    canvas.create_window(10, 150, anchor='nw', window=eth_cap)

    btc_price = tk.Label(root, text="BTC PRICE: " + "\r" + st[0]['price'] + " USD")
    canvas.create_window(400, 80, anchor='nw', window=btc_price)

    eth_price = tk.Label(root, text="ETH PRICE: " + "\r" + st[1]['price'] + " USD")
    canvas.create_window(400, 150, anchor='nw', window=eth_price)

    time_stamp = tk.Label(root, text="DATE : " + st[1]['price_timestamp'])
    canvas.create_window(200, 330, anchor='nw', window=time_stamp)
    root.after(1000, live_price)


live_price()
root.mainloop()





