**Example 1: OFD发票识别示例代码**

ofd发票识别

Input: 

```
tccli ocr VerifyOfdVatInvoiceOCR --cli-unfold-argument  \
    --OfdFileUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Buyer": {
            "AddrTel": "北京海淀区西钓鱼台嘉园北门13392342520",
            "FinancialAccount": "北京农商行32445333322211",
            "Name": "科游迈利有限公司",
            "TaxId": "9150010807MGZHI002"
        },
        "Checker": "张嘉诺",
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
        "InvoiceCheckCode": "17803957977493679699",
        "InvoiceClerk": "任盈盈",
        "InvoiceCode": "050001700111",
        "InvoiceNumber": "62346438",
        "IssueDate": "2020年06月18日",
        "MachineNumber": "016000015903",
        "Note": "对应正数发票代码:050001700111号码:62346436",
        "Payee": "张一诺",
        "RequestId": "7ea56704-eb43-455a-a608-6d79f5e70b37",
        "Seller": {
            "AddrTel": "北京市海淀区颐和园西路一亩园11号",
            "FinancialAccount": "建设银行625555888900998711",
            "Name": "深圳高灯云科技有限公司",
            "TaxId": "91500300MA5FNDGU8Y"
        },
        "TaxControlCode": "002280/993-4692+</-0-5-57+1-61>739+2/07>*5++3-30>+2154-80/*576>3/411+3/3>->*/--++6875624-<41<0>*0<11*/2-1922<7>4",
        "TaxExclusiveTotalAmount": "-300.00",
        "TaxInclusiveTotalAmount": "-318.00",
        "TaxTotalAmount": "-18.00",
        "Type": "026"
    }
}
```

