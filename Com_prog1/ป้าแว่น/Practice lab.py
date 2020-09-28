def yen_to_usd(jpy):
    usd = jpy/108.210
    return usd
def yen_to_baht(jpy):
    baht = jpy/3.49909
    return baht
def cal_shipping_rate(weight):
    if weight<= 100:
        return 0
    elif 100< weight<= 200:
        return 500
    elif 200< weight<= 300:
        return 700
    elif 400< weight<= 600:
        return 1000
    elif 600 < weight <= 800 :
        return 1500
    else:
        return 2200

jiwaru = int(input("How many AKB48 - Jiwaru Days [Type A] [Regular Edition] [CD+DVD]?: "))
ikinari = int(input("How many SKE48 - Ikinari PUNCH LINE [CD+DVD / Regular Edition / Type A]?: "))
kakumei = int(input("How many SKE48 - Kakumei no Oka [3CD+DVD / Type A]?: "))
tofu = int(input("How many Tofu Pro-Wrestling Regular Edition Blu-ray Box?: "))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
total_weight = (jiwaru*298)+(ikinari*298)+(kakumei*505)+(tofu*945)
print(f"Order weight is {total_weight:.2f} g")
print(f"Shipping rate is {cal_shipping_rate(total_weight):.2f} yen (20.33 USD) (628.73 THB)")
price = (jiwaru*1646)+(ikinari*1646)+(kakumei*4104)+(tofu*22680)
print(f"Order price is {price:.2f} yen ({yen_to_usd(price):.2f} USD) ({yen_to_baht(price):.2f} THB)")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
total_price = price + cal_shipping_rate(total_weight)
print(f"Total price is {total_price:.2f} yen ({yen_to_usd(total_price):.2f} USD) ({yen_to_baht(total_price):.2f} THB)")
print(f"Your payment is {total_price:.2f} yen ({yen_to_usd(total_price):.2f} USD) ({yen_to_baht(total_price):.2f} THB)")