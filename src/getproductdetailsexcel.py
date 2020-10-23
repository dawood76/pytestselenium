import csv
import json

data = {}
parks_citroen = {}
parks_nissan = {}
nissan_nissan = {}
parks_peugeot = {}
parks_renault = {}
parks_toyota = {}
suzuki_suzuki = {}

def get_shipping_price(shipping):
    try:
        price = shipping.split(":")[1]
    except:
        pass
    return price


def read_data_from_megami():
    with open('megami.csv', 'r') as file:
        reader = csv.reader(file)
        count = 0;
        for row in reader:
            if count == 0:
                print(row[11])
                count = count + 1;
                continue
            count = count + 1;
            data[row[1]] = {}
            data[row[1]]['brand'] = row[8]
            data[row[1]]['sellers'] = []
            sellers = row[3].split(',')
            for seller in sellers:
                details = get_seller_details(seller+" "+row[8], row[1])
                temp = {}
                temp['name'] = seller;
                temp['price'] = details['price']
                temp['sale_price'] = details['sale_price']
                temp['qty'] = details['qty']
                temp['shipping'] = details['shipping']
                data[row[1]]['sellers'].append(temp)

        print(data)
            #data[row[1]]['description'] = row[6]
            #data[row[1]]['quantity'] = row[12]
                #data[row[1]]['shipping'] = get_shipping_price(row)


def read_data_from_pricefile():
    sellers = ['Parks-Citroen-price', "Nissan-Nissan-price", "Parks-Nissan-price",
               "Parks-Peugeot-price", "Parks-Renault-price", "Parks-Toyota-price",
               "Suzuki-Suzuki-price"]

    for seller in sellers:
        with open(seller+".csv", 'r') as file:
            reader = csv.reader(file)
            count = 0
            pricing_data = {}
            for row in reader:
                if count == 0:
                    count = count + 1;
                    continue
                else:
                    pricing_data[row[0]] = {}
                    pricing_data[row[0]]['price'] = row[1]
                    pricing_data[row[0]]['sale_price'] = row[4]
                    pricing_data[row[0]]['qty'] = row[3]
                    pricing_data[row[0]]['shipping'] = get_shipping_price(row[2])
        update_seller_price(seller, pricing_data)







def read_data_from_OnboardedMPNList():
    with open('OnboardedMPNList.csv', 'r') as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count == 0:
                count = count + 1
                continue

            data[row[0]]['make'] = row[1]


def update_seller_price(seller, pricing_data):
    if seller == "Parks-Citroen-price":
        global parks_citroen
        parks_citroen= pricing_data;

    elif seller == "Nissan-Nissan-price":
        global nissan_nissan
        nissan_nissan = pricing_data

    elif seller == "Parks-Nissan-price":
        global parks_nissan
        parks_nissan = pricing_data

    elif seller == "Parks-Peugeot-price":
        global parks_peugeot
        parks_peugeot = pricing_data

    elif seller == "Parks-Renault-price":
        global parks_renault
        parks_renault = pricing_data

    elif seller == "Parks-Toyota-price":
        global parks_toyota
        parks_toyota = pricing_data

    elif seller == "Suzuki-Suzuki-price":
        global suzuki_suzuki
        suzuki_suzuki = pricing_data


def get_seller_details(seller, mpn):
    if seller == 'Parks Renault':
        return parks_renault[mpn]


def dump_data_to_json():
    with open("data.json", "w") as write_file:
        json.dump(data, write_file)


def get_product_details_from_csv():
    read_data_from_pricefile()
    read_data_from_megami();
    read_data_from_OnboardedMPNList();
    return data;


get_product_details_from_csv()