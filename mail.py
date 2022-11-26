import requests 
 
class mailgan: 
    def __init__(self): 
        self.domain_name = "sandbox5247c5a96ea84cc8b960ec67b94f2622.mailgun.org" 
        self.api_key = "eb129b4dea998c113b244002b1016245-2de3d545-a2aca916" 
 
    def mailToUser(self, email, subject, text): 
        return requests.post( 
            f"https://api.mailgun.net/v3/{self.domain_name}/messages", 
            auth=("api", self.api_key), 
            data={"from": f"<mailgun@{self.domain_name}>", 
                  "to": [email], 
                  "subject": subject, 
                  "text": text})





