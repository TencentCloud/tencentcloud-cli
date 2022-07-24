**Example 1: 增值税发票核验示例代码**



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
            "BuyerName": "栾城区xxx厂",
            "BuyerTaxCode": "92XXXXMAXXXXXX",
            "BuyerAddressPhone": "栾城区北留营村15012345678",
            "BuyerBankAccount": "中国农业银行股份有限公司xx分理处xx",
            "SellerName": "石家庄市XXX石油经销有限公司",
            "SellerTaxCode": "911301047981234567",
            "SellerAddressPhone": "石家庄市桥西区师范街xx号 0311-12345678",
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
                    "TaxAmount": "11.50"
                }
            ]
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
            "Tonnage": "xx",
            "MotorTaxRate": "xx",
            "CertificateNo": "xx",
            "ProduceAddress": "xx",
            "LimitCount": "xx",
            "ImportNo": "xx",
            "SellerTel": "xx",
            "SellerAddress": "xx"
        },
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
        "RequestId": "163b7f97-0b1f-4054-b8e5-bdfb5a6c213f"
    }
}
```

