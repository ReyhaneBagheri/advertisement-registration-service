import requests
import urllib.parse

w2='null'
def fun2(imageurl):
    api_key = 'acc_035ccd735c443d4'
    api_secret = 'a114c9d21fbf8a9814166eb0ef9b6dc8'  
    image_url = imageurl
    encode= urllib.parse.quote_plus(image_url)
    #print(encode)
    response = requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % encode,
        auth=(api_key, api_secret),
        verify=False)


    a_dict=response.json()
    #print((a_dict))
    x=0
    flag=False
    w1=0
    
    z1=0
    z2='null'
    #if(a_dict =={'status': {'text': "Couldn't download image", 'type': 'error'}} ):
    for key, value in a_dict.items():
            #print("1")
        if(key !='status' ):
            #print(key)
            #print(value)
            for key2, value2 in value.items():
                #print("2")
                #print(key2)
                #print(value2)
                for  value3 in value2:
                    #print("3")
                    #print(value3)
                    
                    for key4 , value4 in value3.items():
                        #print("4")
                        x= x+1
                        if x==1:
                            #print("5")
                            if(key4 =='confidence' ):
                                #print("6")
                                w1=value4
                        if x==2:
                            if(key4 == 'tag'):
                                #print("7")
                                for key41 , value41 in value4.items():
                                    #print("8")
                                    if (key41 == 'en'):
                                        #print("9")
                                        w2 = value41
                                        #print(w2)
                                        
                        else:
                            #print("10")
                            if(key4 =='confidence' ):
                                #print("11")
                                z1=value4
                            if(key4 == 'tag'):
                                #print("12")
                                for key42 , value42 in value4.items():
                                    #print("13")
                                    if (key42 == 'en'):
                                        #print("14")
                                        if value42 =='vehicle':
                                            #print("15")
                                            if z1<50:
                                                #print("16")
                                                continue
                                            else :
                                                #print("17")
                                                z2= 'vehicle'
                                                flag = True
                                                break
                                            
                            
                
                            
            break
    if flag==True:
        #print("18")
        return w2
    else : return 'null'
    



#if __name__ =='__main__':
    #x= fun2('https://s3.ir-thr-at1.arvanstorage.ir/project-javad/217a9fe56b8111edb9bd5c879c9b432fcar1.jpg?AWSAccessKeyId=79ad1d7d-9e71-4d87-861b-63983db0e6a5&Signature=R05%2FQWOkG7G4Q1afsg6S1hdA17Y%3D&Expires=1669247838')
    #print(x)   