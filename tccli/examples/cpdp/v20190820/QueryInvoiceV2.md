**Example 1: QueryInvoiceV2**



Input: 

```
tccli cpdp QueryInvoiceV2 --cli-unfold-argument  \
    --InvoicePlatformId 0 \
    --OrderId test195992
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1584287242140",
        "ErrCode": "SUCCESS",
        "ErrMessage": "请求成功",
        "Result": {
            "TaxAmount": "",
            "IsRedWashed": 0,
            "AmountWithoutTax": "",
            "TicketCode": "",
            "TicketDate": "",
            "CheckCode": "",
            "PdfUrl": "",
            "Message": "SUCCESS",
            "TicketSn": "",
            "OrderSn": "",
            "OrderId": "",
            "Status": 5,
            "AmountWithTax": ""
        }
    }
}
```

