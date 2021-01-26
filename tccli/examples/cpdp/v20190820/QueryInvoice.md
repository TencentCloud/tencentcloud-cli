**Example 1: QueryInvoice**



Input: 

```
tccli cpdp QueryInvoice --cli-unfold-argument  \
    --InvoicePlatformId 0 \
    --OrderId test195992
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1584287242140",
        "Result": {
            "Code": 0,
            "Data": {
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
            },
            "Message": "success",
            "Order": {
                "OrderId": "xx",
                "Name": "xx",
                "Items": [
                    {
                        "Status": "xx",
                        "TaxCode": "xx",
                        "Name": "xx",
                        "Models": "xx",
                        "Price": 0.0,
                        "AmountHasTax": 0.0,
                        "Discount": 0.0,
                        "Total": 0,
                        "Unit": "xx"
                    }
                ],
                "SellerName": "xx",
                "Amount": 0.0,
                "AmountHasTax": 0.0,
                "Discount": 0.0,
                "InvoiceType": 0,
                "StoreNo": "xx",
                "OrderDate": "xx"
            }
        }
    }
}
```

