class Auth:
    __instance = None

    @staticmethod
    def getInstance(credentials):
        if Auth.__instance is None:
            Auth(credentials.get('MerchantId'),
                 credentials.get('CustomerId'),
                 credentials.get('UserName'),
                 credentials.get('Password')
                 )
        return Auth.__instance

    def __init__(self, merchant_id, customer_id, username, password):
        self.MerchantId = merchant_id
        self.CustomerId = customer_id
        self.UserName = username
        self.Password = password
        if Auth.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Auth.__instance = self

    def getDict(self):
        return {
            "MerchantId": self.MerchantId,
            "CustomerId": self.CustomerId,
            "UserName": self.UserName,
            "Password": self.Password,
        }
