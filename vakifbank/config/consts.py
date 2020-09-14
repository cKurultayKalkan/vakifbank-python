DEBUG = 0
MCC = 3501
StoreNumber = 1307

CURRENCY_TYPES = {
    'TRY': 949,
    'USD': 840,
    'EUR': 978,
    'GBP': 826,
}

CARD_TYPES = {
    'VISA': 100,
    'MASTERCARD': 200,
    'TROY': 300
}

TRANSACTION_TYPES = {
    'Sale': 'Satış/Taksitli Satış',
    'Cancel': 'İptal',
    'Refund': 'İade',
    'Auth': 'Ön Prov.',
    'Capture': 'Ön Prov. Kapama',
    'Reversal': 'Teknik İptal',
    'CampaignSearch': '',
    'BatchClosedSuccessSearch': '',
    'SurchargeSearch': '',
    'VFTSale': 'Vade Farklı Satış',
    'VFTSearch': 'Vade Farklı Sorgu',
    'TKSale': 'Tarım Kart Eşit Taksitli Satış',
    'TKFlexSale': 'Tarım Kart Esnek Taksitli Satış',
    'PointSale': 'Puan Harcama',
    'PointSearch': 'Puan Sorgu',
    'CardTest': 'Kart Kontrol',
}

__all__ = [
    'CARD_TYPES',
    'CURRENCY_TYPES',
    'DEBUG'
]
