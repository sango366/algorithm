import sys

input_price = input('insert: ')
if not input_price.isdecimal():
    print("数値を入力してください");
    sys.exit()

product_price = input('insert: ')
if not product_price.isdecimal():
    print("数値を入力してください");
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print("お金が不足しています。");
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 5, 1]

for i in coin:
    r = change // i;
    change %= i;
    print(str(i) + ': ' + str(r))