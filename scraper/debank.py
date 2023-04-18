from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pprint import pprint
import re

def removeStr(str):
    number=str.split(" ")
    lst=[number[0],number[1]]
    return lst


def Info(data):
	dateTime=data.find_element(By.CLASS_NAME,"History_sinceTime__3JN2E").text
	txt_link=data.find_element(By.TAG_NAME,"a").get_attribute("href")
	return [dateTime,txt_link]

def FunctionProtocol(data):
	txt=data.find_element(By.CLASS_NAME,"History_interAddressExplain__2VXp7").text
	address=data.find_element(By.CLASS_NAME,"History_greyText__KIi2L").get_attribute("href")
	if txt.find("\n")!=-1:	
		txt=txt.split("\n")
		function=txt[0]
		protocol=txt[1]
		return {"function":function,"protocol":protocol,"address":address.split(".com")[1]}
	return {"function":txt,"protocol":None,"address":address.split(".com")[1]}

def Gas(data):
	gas=data.find_element(By.CLASS_NAME,"History_txExplain__-I6jt").text
	if len(gas)==0:
		return {
			"amount":None,
			"amount_usd":None,
			"token":None
		}
	amount_usd=data.find_element(By.CLASS_NAME,"History_gasPrice__2TKTX").text.replace("(","").replace(")","").replace("$","")
	a=data.find_element(By.CLASS_NAME,"History_txGasInfo__2HxNS").text
	amount=re.split("[a-zA-Z]+",a)[0]
	symbole=re.split("[0-9,.()$]+",a)[1]
	return {
		"amount":amount,
		"amount_usd":amount_usd,
		"token":symbole
	}


def Token(data):
	isThere=data.find_element(By.CLASS_NAME,"History_tokenChange__b7tZ9").text
	if(len(isThere)==0):
		return None
	elements=data.find_elements(By.CLASS_NAME,"History_proposalFlag__1NcfY")
	return elements
	
def loopOfData(data):
	lst=[]
	for i in data:
		info=Info(i)
		function=FunctionProtocol(i)
		element=Token(i)
		token=Element(element)
		gas=Gas(i)
		information={
			"datatime":info[0],
			"txt_link":info[1],
			"function":function["function"],
			"protocol":function["protocol"],
			"address":function["address"],
			"token1":token[0],
			"token2":token[1],
			"gas":gas
		}
		lst.append(information)
	return lst
	
def Element(elements):
	if elements==None:
		token=[{
			"address":None,
			"symbole":None,
			"amount":None,
			"amount_usd":None
			},{
			"address":None,
			"symbole":None,
			"amount":None,
			"amount_usd":None
			}
		]
		return token
	lst=[]
	for i in elements:
		
		address=i.find_element(By.CLASS_NAME,"History_tokenChangeItem__3NN7B").get_attribute("data-id")
		symbole=i.find_element(By.CLASS_NAME,"History_tokenChangeItem__3NN7B").get_attribute("data-name")
		sign=i.find_element(By.CLASS_NAME,"History_tokenChangeText__2dydx").text
		a=i.find_element(By.CLASS_NAME,"History_tokenSymbol__2LgpT").text
		amount=sign[0]+removeStr(a)[0]
		amount_usd=i.find_element(By.CLASS_NAME,"History_tokenPrice__2SUw_").text.replace("(","").replace(")","").replace("$","")
		token={
			"address":address,
			"symbole":symbole,
			"amount":amount,
			"amount_usd":amount_usd
		}
		lst.append(token)
	if len(lst)==1:
		token={
			"address":None,
			"symbole":None,
			"amount":None,
			"amount_usd":None
		}
		lst.append(token)
	return lst


def ButtonList(btn):
	lst=[]
	for i in btn:
		txt=i.text
		lst.append(txt)
	return lst


def scrape_debank(address,chain):
	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options= chrome_options)
	url=f"https://debank.com/profile/{address}/history?chain={chain}"
	driver.get(url)
	data=driver.find_elements(By.CLASS_NAME,"History_tableLine__3dtlF")
	data=loopOfData(data)	
	return data


if __name__=="__main__":
	
	address=input("Enter Address: ")
	chain=input("Enter Chain: ")
	data=scrape_debank(address,chain)
	pprint(test)
