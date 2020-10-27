import csv
import json
from itertools import product

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
            data[row[1]]['superseded_mpn'] = row[27]
            data[row[1]]['sellers_makes'] = []
            sellers = row[3].split(',')
            makes = row[8].split(',')
            makes_sellers = list(product(sellers,makes))
            for seller,make in makes_sellers:
                details = get_seller_details(seller+" "+make, row[1])
                if not details:
                    continue
                temp = {}
                temp['name'] = seller;
                price = float(details['price'])
                sale_price = float(details['sale_price'])
                temp['price'] = sale_price if price > sale_price > 0 else price
                temp['price'] = round(temp['price'] , 2)
                temp['qty'] = details['qty']
                temp['shipping'] = details['shipping']
                temp['brand'] = details['brand']
                data[row[1]]['sellers_makes'].append(temp)

        #dump_data_to_json(data)


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
                    pricing_data[row[0]]['brand'] = row[5]
                    pricing_data[row[0]]['shipping'] = get_shipping_price(row[2])
        update_seller_price(seller, pricing_data)



def get_makes_models(makes,models):
    pass


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
    else:
        return False;

def get_seller_details(seller, mpn):
    if seller == 'Parks Renault':
        return parks_renault[mpn]
    elif seller == 'Parks Nissan':
        return parks_nissan[mpn]
    elif seller == 'Parks Citroen':
        return parks_citroen[mpn]
    elif seller == 'Parks Peugeot':
        return parks_peugeot[mpn]
    elif seller == 'Parks Toyota':
        return parks_toyota[mpn]
    elif seller == 'Nissan Nissan':
        return nissan_nissan[mpn]
    elif seller == 'Suzuki Suzuki_cars':
        return suzuki_suzuki[mpn]


def dump_data_to_json(data):
    with open("data.json", "w") as write_file:
        json.dump(data, write_file)


def get_product_details_from_csv():
    read_data_from_pricefile()
    read_data_from_megami();
    return data;


get_product_details_from_csv()