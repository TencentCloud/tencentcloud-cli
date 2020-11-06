**Example 1: QueryInvoice**



Input: 

```
tccli cpdp QueryInvoice --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --InvoicePlatformId 0 \
    --OrderId test195992
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1584287242140",
        "Result": {
            "code": 0,
            "data": {
                "tax_amount": "",
                "is_red_washed": 0,
                "amount_without_tax": "",
                "ticket_code": "",
                "ticket_date": "",
                "check_code": "",
                "pdf_url": "",
                "message": "SUCCESS",
                "ticket_sn": "",
                "order_sn": "",
                "status": 5,
                "amount_with_tax": ""
            },
            "message": "success"
        }
    }
}
```

