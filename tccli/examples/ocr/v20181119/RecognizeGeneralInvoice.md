**Example 1: 通用票据识别（高级版）**

通用票据识别（高级版）识别多张票据

Input: 

```
tccli ocr RecognizeGeneralInvoice --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/invoice/MixedInvoiceDetect/MixedInvoiceDetect1.jpg \
    --EnableMultiplePage True
```

Output: 
```
{
    "Response": {
        "MixedInvoiceItems": [
            {
                "Code": "OK",
                "Type": 3,
                "SubType": "VatSpecialInvoice",
                "TypeDescription": "增值税发票",
                "SubTypeDescription": "增值税专用发票",
                "Polygon": {
                    "LeftBottom": {
                        "X": 19,
                        "Y": 888
                    },
                    "LeftTop": {
                        "X": 19,
                        "Y": 31
                    },
                    "RightBottom": {
                        "X": 1347,
                        "Y": 888
                    },
                    "RightTop": {
                        "X": 1345,
                        "Y": 31
                    }
                },
                "Angle": 0,
                "SingleInvoiceInfos": {
                    "AirTransport": null,
                    "BusInvoice": null,
                    "ElectronicFlightTicketFull": null,
                    "ElectronicTrainTicketFull": null,
                    "MachinePrintedInvoice": null,
                    "MedicalHospitalizedInvoice": null,
                    "MedicalOutpatientInvoice": null,
                    "MotorVehicleSaleInvoice": null,
                    "NonTaxIncomeElectronicBill": null,
                    "NonTaxIncomeGeneralBill": null,
                    "OtherInvoice": null,
                    "QuotaInvoice": null,
                    "ShippingInvoice": null,
                    "TaxiTicket": null,
                    "TollInvoice": null,
                    "TrainTicket": null,
                    "UsedCarPurchaseInvoice": null,
                    "VatCommonInvoice": null,
                    "VatElectronicCommonInvoice": null,
                    "VatElectronicInvoiceBlockchain": null,
                    "VatElectronicInvoiceFull": null,
                    "VatElectronicInvoiceToll": null,
                    "VatElectronicSpecialInvoice": null,
                    "VatElectronicSpecialInvoiceFull": null,
                    "VatInvoiceRoll": null,
                    "VatSalesList": null,
                    "TaxPayment": null,
                    "CustomsPaymentReceipt": null,
                    "VatSpecialInvoice": {
                        "AcquisitionMark": 0,
                        "AgentMark": 0,
                        "BlockChainMark": 0,
                        "Buyer": "深圳市腾讯计算机系统有限公司",
                        "BuyerAddrTel": "深圳市南山区高新区高新南一路飞亚达大厦5-10楼0755-86013388",
                        "BuyerBankAccount": "招商银行深圳分行振兴支行817282299619961",
                        "BuyerTaxID": "440300708461136",
                        "CheckCode": "",
                        "Ciphertext": "*7-0<84019---5+68315-99->/51,>814<1/7922/<-23/908+>7474+3,78312-072<3<729-+4<6*315-094,->/5>18493/1-60*6-43/90<--78",
                        "City": "深圳市",
                        "Code": "4403152130",
                        "CodeConfirm": "4403152130",
                        "CompanySealContent": "发票专用章,深圳市游戏科技有限公司,04000,NANDN",
                        "CompanySealMark": 1,
                        "Date": "2016年04月11日",
                        "ElectronicFullMark": 0,
                        "ElectronicFullNumber": "",
                        "FormName": "发票联",
                        "FormType": "三",
                        "Issuer": "张三",
                        "Kind": "服务",
                        "MachineCode": "",
                        "Number": "14998456",
                        "NumberConfirm": "14998456",
                        "OilMark": 0,
                        "PretaxAmount": "778.44",
                        "Province": "广东省",
                        "QRCodeMark": 0,
                        "Receiptor": "李明",
                        "Remark": "",
                        "Reviewer": "晓艾",
                        "Seller": "深圳市游戏科技有限公司",
                        "SellerAddrTel": "深圳市南山区高新南一道3号赋安科技大楼A座301室0755-86315454",
                        "SellerBankAccount": "浦发行深圳科技园支行79210154740015474",
                        "SellerTaxID": "440300094040109",
                        "ServiceName": "",
                        "SubTax": "",
                        "SubTotal": "",
                        "Tax": "46.71",
                        "TaxSealContent": "",
                        "Title": "深圳增值税专用发票",
                        "Total": "825.15",
                        "TotalCn": "捌佰贰拾伍圆壹角伍分",
                        "TransitMark": 0,
                        "TravelTax": "",
                        "VatInvoiceItemInfos": [
                            {
                                "DateEnd": "",
                                "DateStart": "",
                                "LicensePlate": "",
                                "Name": "技术服务费",
                                "Price": "",
                                "Quantity": "",
                                "SerialNumber": "",
                                "Specification": "",
                                "Tax": "46.71",
                                "TaxRate": "6%",
                                "Total": "778.44",
                                "Unit": "",
                                "VehicleType": ""
                            }
                        ]
                    },
                    "BankSlip": null,
                    "OnlineTaxiItinerary": null,
                    "CustomsDeclaration": null,
                    "OverseasInvoice": null,
                    "ShoppingReceipt": null,
                    "SaleInventory": null,
                    "MotorVehicleSaleInvoiceElectronic": null,
                    "UsedCarPurchaseInvoiceElectronic": null,
                    "ElectronicTollSummary": null
                },
                "Page": 1,
                "CutImage": "",
                "ItemPolygon": []
            }
        ],
        "RequestId": "c129cda9-e306-472e-817b-4e133ac5c706",
        "TotalPDFCount": 1
    }
}
```

