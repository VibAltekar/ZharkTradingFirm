import requests
import os
print("zhark one")
def ball_out(epochs=200,delays=False):
    dat_arr = []
    havebtc = 0
    dat_len = 0
    buyp = -1
    pnl = 0
    numt = -1
    unsold = False
    #with open("data.txt","r+") as dfile:
    while dat_len < epochs:
        if dat_len >= epochs-2 and havebtc == 1:
            unsold = True
            dat_len = 100
        if numt > 30:
            if havebtc == 0:
                print("havent bought btc, reseting buyp")
                numt = 0
                dat_arr = []
            if havebtc ==1:
                print("unable to sell btc, reseting flux")
                flux = flux/3
        if numt > 60:
            flux = 7
        #r= requests.get("http://localhost:5000/live-data")
        r = requests.get("http://finvibby.herokuapp.com/live-data")
        got_price = r.json()[1]
        if type(got_price) == int:
            #dfile.write(str(got_price))
            dat_arr.append(got_price)
            if len(dat_arr) == 10:
                buyp = (min(dat_arr) + sorted(dat_arr)[1])/2
                flux = (max(dat_arr) - buyp)/2
                print("FLUX is ",flux)
            if len(dat_arr) > 10:
                if got_price <= buyp and havebtc == 0:
                    print("bought at ", got_price)
                    havebtc = 1
                    numt = 0
                if got_price > buyp + flux and havebtc == 1:
                    print("sold at ",got_price)
                    pnl+=(got_price-buyp)
                    havebtc = 0
                    numt = 0
                    dat_arr = []
        dat_len +=1
        numt +=1
        if unsold == True and havebtc == 0:
            print("sold last bit")
            dat_len = epochs+1000
        print("itercount " + str(dat_len) + " dead iters " + str(numt))

    print("-----------------------")
    os.system("say 'done'")
    print(pnl)
    return pnl

if __name__ == '__main__':
    made = 0
    for i in range(10):
        made += ball_out()
    print("Total Money Made $" + str(made))
