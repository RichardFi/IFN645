import numpy as np
import pandas as pd

def data_prep():
    df = pd.read_csv('datasets/CaseStudyData.csv')

    c_name = "VehYear"
    df[c_name] = df[c_name].fillna(0).astype(int)
    df = df[df[c_name] != 0]

    c_name = "Transmission"
    df[c_name] = df[c_name].mask(df[c_name] == "Manual", "MANUAL")
    df[c_name] = df[c_name].mask(df[c_name] == "?", "AUTO")
    df[c_name] = df[c_name].mask(df[c_name] == 0.0, "0")

    c_name = "IsOnlineSale"
    df[c_name] = np.where(df[c_name] == "0", False, True)

    c_name = "WheelType"
    df[c_name] = df[c_name].mask(df[c_name] == "?", "Unknown")
    df[c_name] = df[c_name].fillna("Unknown")

    df.drop(['PurchaseID','PurchaseTimestamp','PurchaseDate','WheelTypeID','PRIMEUNIT','AUCGUART','ForSale'],axis=1,inplace=True)

    c_name = "IsBadBuy"
    df[c_name] = df[c_name].astype(bool)
    


    collection = ["VehOdo","WarrantyCost",
        "MMRAcquisitionAuctionAveragePrice",
            "MMRAcquisitionAuctionCleanPrice",
            "MMRAcquisitionRetailAveragePrice",
            "MMRAcquisitonRetailCleanPrice",
            "MMRCurrentAuctionAveragePrice",
            "MMRCurrentAuctionCleanPrice",
            "MMRCurrentRetailAveragePrice",
            "MMRCurrentRetailCleanPrice",
            "MMRCurrentRetailRatio",
            "VehBCost"]

    for c_name in collection:
        df[c_name] = df[c_name].mask(df[c_name] == "?", 0)
        df[c_name] = df[c_name].mask(df[c_name] == "#VALUE!", 0)
        df[c_name] = pd.to_numeric(df[c_name])
        df[c_name] = df[c_name].mask(df[c_name] == 1, 0)

    df.drop(['Color','Auction','Make','WheelType','Nationality','Size', 'TopThreeAmericanName','VNST'],axis=1,inplace=True)


    df = pd.get_dummies(df)

    df = df.dropna()

    return df