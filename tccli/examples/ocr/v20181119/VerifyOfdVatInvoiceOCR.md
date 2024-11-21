**Example 1: OFD发票识别示例代码**

ofd发票识别

Input: 

```
tccli ocr VerifyOfdVatInvoiceOCR --cli-unfold-argument  \
    --OfdFileUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg
```

Output: 
```
{
    "Response": {
        "Buyer": {
            "AddrTel": "北京*****嘉园北门",
            "FinancialAccount": "北京****11",
            "Name": "科*****限公司",
            "TaxId": "915****002"
        },
        "Checker": "张***",
        "GoodsInfos": [
            {
                "Amount": "-100.00",
                "Item": "*餐饮服务*餐费",
                "MeasurementDimension": "次",
                "Price": "25",
                "Quantity": "-4",
                "Specification": "",
                "TaxAmount": "-6.00",
                "TaxScheme": "6%"
            },
            {
                "Amount": "-100.00",
                "Item": "*餐饮服务*餐费",
                "MeasurementDimension": "次",
                "Price": "25",
                "Quantity": "-4",
                "Specification": "",
                "TaxAmount": "-6.00",
                "TaxScheme": "6%"
            },
            {
                "Amount": "-100.00",
                "Item": "*餐饮服务*餐费",
                "MeasurementDimension": "次",
                "Price": "25",
                "Quantity": "-4",
                "Specification": "",
                "TaxAmount": "-6.00",
                "TaxScheme": "6%"
            }
        ],
        "InvoiceCheckCode": "1780***699",
        "InvoiceClerk": "任**",
        "InvoiceCode": "0***11",
        "InvoiceNumber": "62***8",
        "IssueDate": "2020年06月18日",
        "MachineNumber": "016****903",
        "Note": "对应正*****436",
        "Payee": "张***",
        "RequestId": "7ea56704-eb43-455a-a608-6d79f5e70b37",
        "Seller": {
            "AddrTel": "北京****号",
            "FinancialAccount": "建设*****711",
            "Name": "深圳*****有限公司",
            "TaxId": "915****8Y"
        },
        "TaxControlCode": "00228*****2274",
        "TaxExclusiveTotalAmount": "-300.00",
        "TaxInclusiveTotalAmount": "-318.00",
        "TaxTotalAmount": "-18.00",
        "Type": "026",
        "AirTicketInfo": {
            "PassengerName": "李**",
            "ValidIdNumber": "440183********372",
            "Endorsement": "BUDEQIANZHUAN不得签转/****变更退票收费",
            "NumberOfGPOrder": "",
            "ElectronicInvoiceAirTransportReceiptNumber": "2344****0553",
            "DetailInformationOfAirTicketTuple": [
                {
                    "DepartureStation": "CAN 广州",
                    "DestinationStation": "CGO 郑州",
                    "FlightSegment": "1",
                    "Carrier": "南航",
                    "Flight": "CZ3***",
                    "SeatClass": "T",
                    "CarrierDate": "2023-01-30",
                    "DepartureTime": "07:25",
                    "FareBasis": "TCP0***",
                    "EffectiveDate": "2023-01-30",
                    "ExpirationDate": "2023-01-30",
                    "FreeBaggageAllowance": "20K"
                }
            ],
            "Fare": "458",
            "FuelSurcharge": "70",
            "VatRate": "0.08",
            "VatTaxAmount": "47",
            "CivilAviationDevelopmentFund": "50.00",
            "OtherTaxes": "0.00",
            "TotalAmount": "600",
            "ElectronicTicketNum": "",
            "VerificationCode": "0**3",
            "PromptInformation": "",
            "Insurance": "0.00",
            "AgentCode": "CAN0***570",
            "IssueParty": "中国南****限公司",
            "IssueDate": "2023-02-07",
            "IssuingStatus": "正常",
            "MarkingOfDomesticOrInternational": "国内",
            "NameOfPurchaser": "兴*****分公司",
            "NameOfSeller": "中国****限公司",
            "UnifiedSocialCreditCodeOfPurchaser": "914***673B"
        },
        "RailwayTicketInfo": {
            "TypeOfVoucher": "电子发票（铁路电子客票）",
            "ElectronicTicketNum": "3067*****22",
            "DateOfIssue": "2022-03-17",
            "TypeOfBusiness": "退",
            "DepartureStation": "南京",
            "PhonicsOfDepartureStation": "Nanjing",
            "DestinationStation": "上海虹桥",
            "PhonicsOfDestinationStation": "Shanghaihongqiao",
            "TrainNumber": "D1****1",
            "TravelDate": "2022-01-20",
            "DepartureTime": "06:20",
            "AirConditioningCharacteristics": "",
            "SeatLevel": "一等座",
            "Carriage": "03车",
            "Seat": "01F号",
            "Fare": "48.00",
            "ElectronicInvoiceRailwayETicketNumber": "221******0011",
            "IdNumber": "142*****1627",
            "Name": "汪某某",
            "TotalAmountExcludingTax": "52.28",
            "TaxRate": "0.06",
            "TaxAmount": "2.72",
            "NameOfPurchaser": "铁路客票****单位",
            "UnifiedSocialCreditCodeOfPurchaser": "9111***858",
            "NumberOfOriginalInvoice": "22****0010"
        }
    }
}
```

