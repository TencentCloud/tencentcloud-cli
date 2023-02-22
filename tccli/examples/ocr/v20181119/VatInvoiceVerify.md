**Example 1: 增值税发票核验示例代码**

增值税发票核验示例代码

Input: 

```
tccli ocr VatInvoiceVerify --cli-unfold-argument  \
    --InvoiceNo 04000000 \
    --InvoiceCode 1300000000 \
    --InvoiceDate 2019-12-11 \
    --Additional 88.50
```

Output: 
```
{
    "Response": {
        "Invoice": {
            "Code": "1300000000",
            "Number": "04000000",
            "Date": "20191211",
            "BuyerName": "栾城区一厂",
            "BuyerTaxCode": "921467MA773940",
            "BuyerAddressPhone": "栾城区北留营村15012345678",
            "BuyerBankAccount": "中国农业银行股份有限公司第一分理处",
            "SellerName": "石家庄市第一石油经销有限公司",
            "SellerTaxCode": "911301047981234567",
            "SellerAddressPhone": "石家庄市桥西区师范街01号 0311-12345678",
            "SellerBankAccount": "",
            "Remark": "",
            "MachineNo": "661510100000",
            "Type": "01",
            "CheckCode": "85518065011000000000",
            "IsAbandoned": "",
            "HasSellerList": "",
            "SellerListTitle": "",
            "SellerListTax": "",
            "AmountWithoutTax": "88.50",
            "TaxAmount": "11.50",
            "AmountWithTax": "100.00",
            "Items": [
                {
                    "LineNo": "1",
                    "Name": "*乙醇汽油*92#汽油",
                    "Spec": "",
                    "Unit": "升",
                    "Quantity": "15.479876160990711",
                    "UnitPrice": "5.716814159292035",
                    "AmountWithoutTax": "88.50",
                    "TaxRate": "13%",
                    "TaxAmount": "11.50",
                    "TaxClassifyCode": ""
                }
            ],
            "TaxBureau": "",
            "TrafficFreeFlag": ""
        },
        "VehicleInvoiceInfo": {
            "MotorBankAccount": "",
            "VinNo": "",
            "MotorBankName": "",
            "BizCheckFormNo": "",
            "PlateModel": "",
            "BuyerNo": "",
            "CarType": "",
            "TaxtationOrgName": "",
            "TaxtationOrgCode": "",
            "EngineNo": "",
            "PayTaxesNo": "",
            "Tonnage": "",
            "MotorTaxRate": "",
            "CertificateNo": "",
            "ProduceAddress": "",
            "LimitCount": "",
            "ImportNo": "",
            "SellerTel": "",
            "SellerAddress": ""
        },
        "UsedVehicleInvoiceInfo": {
            "BuyerTel": "",
            "MarketBankAccount": "",
            "BuyerNo": "",
            "ManagementOffice": "",
            "Seller": "",
            "MarketAddress": "",
            "SellerNo": "",
            "BuyerAddress": "",
            "Buyer": "",
            "AuctioneerTel": "",
            "AuctioneerAddress": "",
            "MarketTaxpayerNum": "",
            "VehicleIdentifyNo": "",
            "VehicleLicenseNo": "",
            "AuctioneerTaxpayerNum": "",
            "MarketTel": "",
            "AuctioneerBankAccount": "",
            "Auctioneer": "",
            "VehicleTotalPrice": "",
            "RegisterNo": "",
            "SellerAddress": "",
            "TaxBureau": "",
            "SellerTel": "",
            "Market": ""
        },
        "RequestId": "163b7f97-0b1f-4054-b8e5-bdfb5a6c213f"
    }
}
```

