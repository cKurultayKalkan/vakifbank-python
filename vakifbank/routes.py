BASE_URL = "https://vakifbank.com.tr/"

# VIRTUAL POS
POS_BASE = "https://onlineodeme.vakifbank.com.tr:4443"
POS_TEST = "https://onlineodemetest.vakifbank.com.tr:4443"
THREED_BASE = "https://3dsecure.vakifbank.com.tr"
THREED_TEST = "https://3dsecuretest.vakifbank.com.tr"
POS_ENROLL = "MPIAPI/MPI_Enrollment.aspx"
POS_API = "VposService/TransactionServices.asmx"
POS_SERVICE_SEARCH = 'UIService/TransactionSearchOperations.asmx'
POS_SERVICE_HELPER = '/UIService/MerchantServices.asmx'

# COMMON PAYMENT
CP_BASE = "https://cpweb.vakifbank.com.tr"
CP_TEST = "https://cptest.vakifbank.com.tr"
CP_ENROLL = "CommonPayment/api/RegisterTransaction"
CP_API = "CommonPayment/SecurePayment"
CP_TRANSACTION = "CommonPayment/api/VposTransaction"


class ServiceUrl:
    def __init__(self, service_type, mode=0):
        if service_type == 'VPos':

            base = POS_BASE if mode else POS_TEST
            base3d = THREED_BASE if mode else THREED_TEST

            self.enroll = f"{base3d}/{POS_ENROLL}"
            self.api = f"{base}/{POS_API}"
            self.transaction = f"{base}/{POS_SERVICE_SEARCH}"
            self.helper = f"{base}/{POS_SERVICE_HELPER}"
        elif service_type == 'CP':

            base = CP_BASE if mode else CP_TEST

            self.enroll = f"{base}/{CP_ENROLL}"
            self.api = f"{base}/{CP_API}"
            self.transaction = f"{base}/{CP_TRANSACTION}"
