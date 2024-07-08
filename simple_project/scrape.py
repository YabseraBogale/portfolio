import requests
ulr="https://secure-retreat-92358.herokuapp.com/"
value={"fname":"Rafia","lname":"Kedir","email":"yuanizaaa@gmail.com"}
resp=requests.post(url=ulr,data=value)
print(resp.content)