# Vakıfbank Python Package


## Install

`pip install vakifbank`

## Usage

First import module from vakifbank package.

`from vakifbank.ThreeD_Payment import ThreeDPayment`

Prepare your credentials. You can get your store password and id from https://onlineodeme.vakifbank.com.tr/AdminUI/Account/Login?ReturnUrl=%2fadminui

    credentials = { 
        'HostMerchantId': YourHostMerchantId,
        'HostPassword' : YourHostPassword,
        'HostTerminalId': YourHostTerminalId 
    }

Then initialize 3D payment class with credentials.

`three_d = ThreeDPayment(credentials)`
 
Prepare your data in your website form

    data = {
        "order_id": random.randrange(1000),
        "amount": "1.00",
        "pan": CREDITCARDNUMBER,
        "expiry": EXPIRYDATE,
        "currency": currency,
        "success_url": YOUR_SUCCESS_URL,
        "fail_url": YOUR_FAIL_URL
    }
 

Prepare request data

    three_d.prepare(data) 
 
Get Enrollment Result

    three_d.enrollment_result()

Get Your Prepared Html Page
    
    threed_d.get_acs_html()
