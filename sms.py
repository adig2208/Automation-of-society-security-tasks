from twilio.rest import Client


class sendsms():

    def send(self,name , cmpny ,mno,to):

        # the following line needs your Twilio Account SID and Auth Token
        
        client = Client("*****", "******")
        print(name)
        print(cmpny)
        print(mno)
        print(to)
        
        msg = name + " from " + cmpny + " is here to deliver your package. Contact Number : " +mno 
        print(msg)


       
        client.messages.create(to="your number", 
                            from_="twilio number", 
                            body=msg)