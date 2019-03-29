import numpy as np
import pandas as pd

def data_prep():
    df = pd.read_csv('data.csv')

    df.drop(['PurchaseID','PurchaseTimestamp',
        'PurchaseDate','PRIMEUNIT','AUCGUART','ForSale','Color',
        'WheelType','Nationality','TopThreeAmericanName','WarrantyCost',
        'MMRCurrentRetailRatio'],axis=1,inplace=True)

    c_name = "VehYear"
    df[c_name] = df[c_name].fillna(0).astype(int)
    df = df[df[c_name] != 0]
    
    c_name = "Transmission"
    df[c_name] = df[c_name].mask(df[c_name] == "Manual", "MANUAL")
    df[c_name] = df[c_name].mask(df[c_name] == "?", "AUTO")
    
    c_name = "WheelTypeID"
    df[c_name] = df[c_name].mask(df[c_name] == "0", "?")
    df[c_name] = df[c_name].fillna("?")

    c_name = "VehBCost"
    df[c_name] = df[c_name].mask(df[c_name] == "?", "0")
    df[c_name] = pd.to_numeric(df[c_name])
    df[c_name] = df[c_name].mask(df[c_name] < 0, 0)

    c_name = "IsOnlineSale"
    df[c_name] = np.where(df[c_name] == "0", False, True)
    
    c_name = "IsBadBuy"
    df[c_name] = df[c_name].astype(bool)
    
    collection = ["MMRAcquisitionAuctionAveragePrice",
              "MMRAcquisitionAuctionCleanPrice",
              "MMRAcquisitionRetailAveragePrice",
              "MMRAcquisitonRetailCleanPrice",
              "MMRCurrentAuctionAveragePrice",
              "MMRCurrentAuctionCleanPrice",
              "MMRCurrentRetailAveragePrice",
              "MMRCurrentRetailCleanPrice",]

    for c_name in collection:
        df[c_name] = df[c_name].mask(df[c_name] == "?", 0)
        df[c_name] = df[c_name].mask(df[c_name] == "#VALUE!", 0)
        df[c_name] = pd.to_numeric(df[c_name])
        df[c_name] = df[c_name].mask(df[c_name] == 1, 0)
        
    
    df = pd.get_dummies(df)

    df = df.dropna()
    
    return df