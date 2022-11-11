import shutil
import fileinput
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
Usr=input("Please enter user name: ")
mail=input("Please enter user's mail id: ")
cName=input("Please enter crop name: ")
cLink=input("Please the link for the image of the crop here: ")
cBuyLink=input("Please the link for buying the crop here: ")
unit=input("Please enter the unit here: ")
amount=input("Please enter the price for the said unit: ")
msg=input("Please enter your msg here: ")
from csv import writer

l1 = [cName,cLink,cBuyLink,msg,unit,amount]

with open("productsStored.csv", 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(l1)
    f_object.close()

filename=cName+'.html'
shutil.copy('product.html', filename)
print(filename)

rplLink='<img src="'+cLink+'" alt="">'
bcLink='<a href="'+cBuyLink+'" target="_blank" rel="noreferrer noopener" class="cart-btn"></i> Buy Now</a></i> Buy Now</a>'

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace("<!--Unit-->", unit), end='')


with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace("<!--CROPNAME-->", cName), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace("<!--Price-->", amount), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace("<!--MESSAGE-->", msg), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('<a href="https://www.flipkart.com/shop-360-garden-fresh-coffea-arabica-coffee-seeds-growing-pack-20-seed/p/itmada448286f3e6?pid=PAEFJCRSSY7Y6BFF&lid=LSTPAEFJCRSSY7Y6BFFCZJBVM&marketplace=FLIPKART&fm=factBasedRecommendation%2FrecentlyViewed&iid=R%3Arv%3Bpt%3App%3Buid%3A82d41b1a-52aa-11ed-af3b-3732172e4dd6%3B.PAEFJCRSSY7Y6BFF&ppt=pp&ppn=pp&ssid=eth3zi6f740000001666512756511&otracker=pp_reco_Recently%2BViewed_1_37.productCard.RECENTLY_VIEWED_SHOP%2B360%2BGARDEN%2BFresh%2BCoffea%2Barabica%2B%252F%2BCoffee%2BSeeds%2BFor%2BGrowing%2B-%2BPack%2Bof%2B20%2BSeeds%2BSeed_PAEFJCRSSY7Y6BFF_factBasedRecommendation%2FrecentlyViewed_0&otracker1=pp_reco_PINNED_factBasedRecommendation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_1_NA_view-all&cid=PAEFJCRSSY7Y6BFF" target="_blank" rel="noreferrer noopener" class="cart-btn"></i> Buy Now</a>', bcLink), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('<img src="static1/images/coffee.jpg" alt="">', rplLink), end='')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="height:38px;width:93px;v-text-anchor:middle;" arcsize="11%" stroke="false" fillcolor="#2bd95e"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:14px"><![endif]--><a href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2bd95e;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;">Buy Now</span></span></a>', bcLink), end='')


# 'cropmanagementmail@gmail.com', 'mzukjnytdubqtxql'
fromaddr = "cropmanagementmail@gmail.com"
toaddr = "adrushtshetty@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = cName+" to be Added to shop page"

body = """
Dear DEV,
PFA the product page for the above mentioned crop for pushing.

Best Regards
Admin
"""

msg.attach(MIMEText(body, 'plain'))


attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "mzukjnytdubqtxql")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()