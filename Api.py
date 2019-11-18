import urllib.request
import json

def Search( Type, Amount ):

    url = 'http://open-api.myhelsinki.fi/v1/' + Type + '/?limit=' + Amount + ''
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req).read()
    Content = json.loads(r.decode())

    return Content


def Listing( Content, Amount ):
    Counter = 0
    for Order in range( int(Amount) ):
        Counter += 1
        print( str(Counter) + ") " + Content['data'][Order]['name']['fi'] )


def AdditionalInfo( Content, AdditionalChoice ):
    Index = int(AdditionalChoice) - 1
    print("Lisätietoa valitsemastasi aktiviteetista: \n")
    print( Content['data'][Index]['description']['body'] )