**Example 1: 增值税发票核验示例代码**

增值税发票核验示例代码

Input: 

```
tccli ocr VatInvoiceVerifyNew --cli-unfold-argument  \
    --InvoiceCode 144002288010 \
    --InvoiceNo 04138864 \
    --InvoiceDate 2022-11-16 \
    --Amount 498.90 \
    --CheckCode 00000000005672311400 \
    --RegionCode 4400 \
    --SellerTaxCode 44078819091887401X \
    --EnableCommonElectronic True
```

Output: 
```
{
    "Response": {
        "Invoice": {
            "AmountWithTax": "498.90",
            "AmountWithoutTax": "0.00",
            "BuyerAddressPhone": "",
            "BuyerBankAccount": "",
            "BuyerName": "",
            "BuyerTaxCode": "",
            "CheckCode": "",
            "Code": "144002288010",
            "Date": "",
            "HasSellerList": "",
            "IsAbandoned": "N",
            "Items": [],
            "MachineNo": "",
            "Number": "04138864",
            "Remark": "",
            "SellerAddressPhone": "",
            "SellerBankAccount": "",
            "SellerListTax": "",
            "SellerListTitle": "",
            "SellerName": "广州市天河区员美丽美食店",
            "SellerTaxCode": "",
            "TaxAmount": "0.00",
            "TaxBureau": "",
            "TrafficFreeFlag": "N",
            "Type": "102"
        },
        "PassInvoiceInfoList": [],
        "RequestId": "f3cd280c-6d3a-41c5-8493-4ed98f8b2755",
        "UsedVehicleInvoiceInfo": {
            "Auctioneer": "",
            "AuctioneerAddress": "",
            "AuctioneerBankAccount": "",
            "AuctioneerTaxpayerNum": "",
            "AuctioneerTel": "",
            "Buyer": "",
            "BuyerAddress": "",
            "BuyerNo": "",
            "BuyerTel": "",
            "ManagementOffice": "",
            "Market": "",
            "MarketAddress": "",
            "MarketBankAccount": "",
            "MarketTaxpayerNum": "",
            "MarketTel": "",
            "RegisterNo": "",
            "Seller": "",
            "SellerAddress": "",
            "SellerNo": "",
            "SellerTel": "",
            "TaxBureau": "",
            "VehicleIdentifyNo": "",
            "VehicleLicenseNo": "",
            "VehicleTotalPrice": ""
        },
        "VehicleInvoiceInfo": {
            "BizCheckFormNo": "",
            "BuyerNo": "",
            "CarType": "",
            "CertificateNo": "",
            "EngineNo": "",
            "ImportNo": "",
            "LimitCount": "",
            "MotorBankAccount": "",
            "MotorBankName": "",
            "MotorTaxRate": "",
            "PayTaxesNo": "",
            "PlateModel": "",
            "ProduceAddress": "",
            "SellerAddress": "",
            "SellerTel": "",
            "TaxtationOrgCode": "",
            "TaxtationOrgName": "",
            "Tonnage": "",
            "VinNo": ""
        }
    }
}
```

