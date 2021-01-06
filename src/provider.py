class Provider:
    def __init__(self, tryRate: float,usdRate:float,euroRate:float, providerName):
        self.usdRate = float(usdRate)
        self.euroRate = float(euroRate)
        self.tryRate = float(tryRate)
        self.providerName = providerName
        
    