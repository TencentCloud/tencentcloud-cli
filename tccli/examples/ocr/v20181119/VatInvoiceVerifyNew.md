**Example 1: 增值税发票核验示例代码**



Input: 

```
tccli ocr VatInvoiceVerifyNew --cli-unfold-argument  \
    --InvoiceNo 04000000 \
    --Amount 88.50 \
    --InvoiceCode 1300000000 \
    --InvoiceDate 2019-12-11
```

Output: 
```
{
    "Response": {
        "PassInvoiceInfoList": [
            {
                "PassDateEnd": "xx",
                "Type": "xx",
                "TaxClassifyCode": "xx",
                "NumberPlate": "xx",
                "PassDateBegin": "xx"
            }
        ],
        "UsedVehicleInvoiceInfo": {
            "BuyerTel": "xx",
            "MarketBankAccount": "xx",
            "BuyerNo": "xx",
            "ManagementOffice": "xx",
            "Seller": "xx",
            "MarketAddress": "xx",
            "SellerNo": "xx",
            "BuyerAddress": "xx",
            "Buyer": "xx",
            "AuctioneerTel": "xx",
            "AuctioneerAddress": "xx",
            "MarketTaxpayerNum": "xx",
            "VehicleIdentifyNo": "xx",
            "VehicleLicenseNo": "xx",
            "AuctioneerTaxpayerNum": "xx",
            "MarketTel": "xx",
            "AuctioneerBankAccount": "xx",
            "Auctioneer": "xx",
            "VehicleTotalPrice": "xx",
            "RegisterNo": "xx",
            "SellerAddress": "xx",
            "TaxBureau": "xx",
            "SellerTel": "xx",
            "Market": "xx"
        },
        "RequestId": "xx",
        "Invoice": {
            "TaxAmount": "xx",
            "BuyerAddressPhone": "xx",
            "SellerListTax": "xx",
            "SellerName": "xx",
            "SellerListTitle": "xx",
            "SellerAddressPhone": "xx",
            "BuyerBankAccount": "xx",
            "Type": "xx",
            "SellerBankAccount": "xx",
            "CheckCode": "xx",
            "TrafficFreeFlag": "xx",
            "Date": "xx",
            "Remark": "xx",
            "HasSellerList": "xx",
            "MachineNo": "xx",
            "Items": [
                {
                    "TaxRate": "xx",
                    "Name": "xx",
                    "AmountWithoutTax": "xx",
                    "TaxAmount": "xx",
                    "TaxClassifyCode": "xx",
                    "LineNo": "xx",
                    "UnitPrice": "xx",
                    "Spec": "xx",
                    "Unit": "xx",
                    "Quantity": "xx"
                }
            ],
            "BuyerTaxCode": "xx",
            "IsAbandoned": "xx",
            "Code": "xx",
            "SellerTaxCode": "xx",
            "AmountWithTax": "xx",
            "AmountWithoutTax": "xx",
            "Number": "xx",
            "BuyerName": "xx",
            "TaxBureau": "xx"
        },
        "VehicleInvoiceInfo": {
            "MotorBankAccount": "xx",
            "VinNo": "xx",
            "MotorBankName": "xx",
            "BizCheckFormNo": "xx",
            "PlateModel": "xx",
            "CarType": "xx",
            "TaxtationOrgName": "xx",
            "TaxtationOrgCode": "xx",
            "EngineNo": "xx",
            "PayTaxesNo": "xx",
            "BuyerNo": "xx",
            "Tonnage": "xx",
            "MotorTaxRate": "xx",
            "CertificateNo": "xx",
            "ProduceAddress": "xx",
            "LimitCount": "xx",
            "SellerTel": "xx",
            "ImportNo": "xx",
            "SellerAddress": "xx"
        }
    }
}
```

