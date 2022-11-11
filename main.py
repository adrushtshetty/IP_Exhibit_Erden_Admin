
from flask import Flask, request, jsonify, render_template, url_for, redirect
import fileinput
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'dev':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)

@app.route('/home')
def home_page():
    return render_template("index.html")

@app.route('/interview_form')
def interview():
    return render_template("forms-elements.html")


@app.route('/mail_form')
def mailFormUI():
    output="Not Sent"
    return render_template('eo_Form.html',status='{}'.format(output))


class MIMEText:
    pass


@app.route('/mail_form',methods=['POST'])
def mailForm():
    import fileinput
    import shutil
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    name = request.form['name']
    email = request.form['usMail']
    crop=request.form['usCrop']
    clink=request.form['usCLink']
    blink=request.form['usBLink']
    msg = request.form['usMsg']


    Usr = name
    mail = email
    cName = crop
    cLink = clink
    cBuyLink = blink
    Umsg=str(msg)
    rplLink = '<img alt="crop" class="big" src="' + cLink + '" style="display: block; height: auto; border: 0; width: 393px; max-width: 100%;" title="crop" width="393"/>'

    buyNowLink = '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="' + cBuyLink + '" style="height:38px;width:93px;v-text-anchor:middle;" arcsize="11%" stroke="false" fillcolor="#2bd95e"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:14px"><![endif]--><a href="' + cBuyLink + '" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2bd95e;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;">Buy Now</span></span></a>'
    filename = cName + '.html'
    shutil.copy('mail.html', filename)
    print(filename)

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--UserName-->", Usr), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--CropName-->", cName), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(
                '<img alt="crop" class="big" src="https://lh3.googleusercontent.com/ot5wOM6j47MsALSkfsLZ9YfzYs9tDI8k-kq3WP2dSvRUaeaRZuMOICz4jJcRYLcjOtleS1GCD31-F4wCRjYYVpvVCYm1XGm6ONyx6zPv6Lsac6wEJDVeDpfWstxscXeXK6AR8_bZHA=w2400" style="display: block; height: auto; border: 0; width: 393px; max-width: 100%;" title="crop" width="393"/>',
                rplLink), end='')
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(
                '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="height:38px;width:93px;v-text-anchor:middle;" arcsize="11%" stroke="false" fillcolor="#2bd95e"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:14px"><![endif]--><a href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2bd95e;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;">Buy Now</span></span></a>',
                buyNowLink), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--MESSAGE	-->',Umsg), end='')



    file1 = open(filename, 'r')
    Lines = file1.readlines()

    str1 = (''.join(Lines))

    me = "cropmanagementmail@gmail.com"
    you = mail
    # you=request.form['Mail']
    print(you)
    # you = "adrushtshetty@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Crop Management"
    msg['From'] = me
    msg['To'] = you
    html = str1

    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('cropmanagementmail@gmail.com', 'mzukjnytdubqtxql')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()
    output='Sent'
    unit = request.form['unit']
    amount = request.form['amount']
    from csv import writer

    l1 = [cName, cLink, cBuyLink, Umsg, unit, amount]

    with open("productsStored.csv", 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(l1)
        f_object.close()

    filename = cName + '_product.html'
    filename1=filename
    shutil.copy('product.html', filename1)
    print(filename1)

    rplLink = '<img src="' + cLink + '" alt="">'
    bcLink = '<a href="' + cBuyLink + '" target="_blank" rel="noreferrer noopener" class="cart-btn"></i> Buy Now</a></i> Buy Now</a>'

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Unit-->", unit), end='')

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace("<!--CROPNAME-->", cName), end='')

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Price-->", amount), end='')

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace("<!--MESSAGE-->", Umsg), end='')

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace(
                '<a href="https://www.flipkart.com/shop-360-garden-fresh-coffea-arabica-coffee-seeds-growing-pack-20-seed/p/itmada448286f3e6?pid=PAEFJCRSSY7Y6BFF&lid=LSTPAEFJCRSSY7Y6BFFCZJBVM&marketplace=FLIPKART&fm=factBasedRecommendation%2FrecentlyViewed&iid=R%3Arv%3Bpt%3App%3Buid%3A82d41b1a-52aa-11ed-af3b-3732172e4dd6%3B.PAEFJCRSSY7Y6BFF&ppt=pp&ppn=pp&ssid=eth3zi6f740000001666512756511&otracker=pp_reco_Recently%2BViewed_1_37.productCard.RECENTLY_VIEWED_SHOP%2B360%2BGARDEN%2BFresh%2BCoffea%2Barabica%2B%252F%2BCoffee%2BSeeds%2BFor%2BGrowing%2B-%2BPack%2Bof%2B20%2BSeeds%2BSeed_PAEFJCRSSY7Y6BFF_factBasedRecommendation%2FrecentlyViewed_0&otracker1=pp_reco_PINNED_factBasedRecommendation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_1_NA_view-all&cid=PAEFJCRSSY7Y6BFF" target="_blank" rel="noreferrer noopener" class="cart-btn"></i> Buy Now</a>',
                bcLink), end='')

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace('<img src="static1/images/coffee.jpg" alt="">', rplLink), end='')

    with fileinput.FileInput(filename1, inplace=True) as file:
        for line in file:
            print(line.replace(
                '<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="height:38px;width:93px;v-text-anchor:middle;" arcsize="11%" stroke="false" fillcolor="#2bd95e"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:14px"><![endif]--><a href="https://ip-exhibit-crop-management.herokuapp.com/shop" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#2bd95e;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:20px;padding-right:20px;font-size:14px;display:inline-block;letter-spacing:normal;"><span dir="ltr" style="word-break: break-word; line-height: 28px;">Buy Now</span></span></a>',
                bcLink), end='')

    import fileinput
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    # 'cropmanagementmail@gmail.com', 'mzukjnytdubqtxql'
    fromaddr = "cropmanagementmail@gmail.com"
    toaddr = "adrushtshetty@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = cName + " to be Added to shop page"

    body = """
    Dear DEV,
    PFA the product page for the above mentioned crop for pushing.

    Best Regards
    Admin
    """

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filename1, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename1)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "mzukjnytdubqtxql")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return render_template('eo_Form.html',status='{}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)

