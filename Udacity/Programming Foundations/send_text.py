from twilio.rest import Client 
 
account_sid = 'AC07cad4cc68c4b8caf21b63da90901ab6' 
auth_token = '7b8af9ba923a1621b8c7feb3a64466af' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(
                              body="No quiero lentejas",
                              from_='+34911061952',        
                              to='+34645754432' 
                          ) 
 
print(message.sid)
