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
            "ElectronicType": "",
            "HasSellerList": "",
            "IsAbandoned": "N",
            "Items": [],
            "MachineNo": "",
            "Number": "04138864",
            "Remark": "",
            "RedLetterInvoiceMark": false,
            "IssuingTypeMark": 1,
            "SellerAddressPhone": "",
            "SellerBankAccount": "",
            "SellerAgentName": "",
            "SellerAgentTaxID": "",
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
        },
        "ElectronicTrainTicket": {
            "BuyerName": "abc",
            "BuyerTaxCode": "abc",
            "Number": "abc",
            "Date": "abc",
            "TotalCN": "abc",
            "Tax": "abc",
            "ServiceType": "abc",
            "TimeGetOn": "abc",
            "TrainNumber": "abc",
            "Code": "abc",
            "SeatType": "abc",
            "DateGetOn": "abc",
            "TrainCabin": "abc",
            "StationGetOn": "abc",
            "ElectronicNumber": "abc",
            "PassengerName": "abc",
            "PassengerNo": "abc",
            "Amount": "abc",
            "StationGetOff": "abc",
            "TaxRate": "abc",
            "Seat": "abc",
            "Total": "abc",
            "CheckCode": "abc",
            "StateCode": "0"
        },
        "ElectronicAirTransport": {
            "Code": "abc",
            "Number": "abc",
            "Date": "abc",
            "Amount": "abc",
            "CheckCode": "abc",
            "Total": "abc",
            "DeductionMark": "abc",
            "StateCode": "abc",
            "BuyerTaxCode": "abc",
            "BuyerName": "abc",
            "DomesticInternationalMark": "abc",
            "PassengerName": "abc",
            "PassengerNo": "abc",
            "ElectronicNumber": "abc",
            "ElectronicAirTransportDetails": [
                {
                    "FlightSegment": "abc",
                    "StationGetOn": "abc",
                    "StationGetOff": "abc",
                    "Carrier": "abc",
                    "FlightNumber": "abc",
                    "SeatLevel": "abc",
                    "FlightDate": "abc",
                    "DepartureTime": "abc",
                    "FareBasis": "abc"
                }
            ]
        }
    }
}
```

