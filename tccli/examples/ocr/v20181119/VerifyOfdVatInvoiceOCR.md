**Example 1: OFD发票识别示例代码**



Input: 

```
tccli ocr VerifyOfdVatInvoiceOCR --cli-unfold-argument  \
    --OfdFileUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Note": "xx",
        "GoodsInfos": [
            {
                "TaxAmount": "xx",
                "Specification": "xx",
                "MeasurementDimension": "xx",
                "Item": "xx",
                "Amount": "xx",
                "TaxScheme": "xx",
                "Price": "xx",
                "Quantity": "xx"
            }
        ],
        "InvoiceClerk": "xx",
        "InvoiceCode": "xx",
        "Type": "xx",
        "TaxExclusiveTotalAmount": "xx",
        "TaxTotalAmount": "xx",
        "Seller": {
            "AddrTel": "xx",
            "Name": "xx",
            "FinancialAccount": "xx",
            "TaxId": "xx"
        },
        "TaxInclusiveTotalAmount": "xx",
        "Payee": "xx",
        "Checker": "xx",
        "RequestId": "xx",
        "TaxControlCode": "xx",
        "Buyer": {
            "AddrTel": "xx",
            "Name": "xx",
            "FinancialAccount": "xx",
            "TaxId": "xx"
        },
        "IssueDate": "xx",
        "InvoiceNumber": "xx",
        "InvoiceCheckCode": "xx",
        "MachineNumber": "xx"
    }
}
```

