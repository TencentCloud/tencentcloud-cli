**Example 1: CreateInvoice**



Input: 

```
tccli cpdp CreateInvoice --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --InvoicePlatformId 0 \
    --BuyerTitle 发票抬头 \
    --TitleType 1 \
    --OrderId 10test195993 \
    --BuyerTaxpayerNum 11111123242 \
    --BuyerAddress china \
    --BuyerBankName 银行名称 \
    --BuyerBankAccount 123124132213 \
    --BuyerPhone 11111111111 \
    --BuyerEmail test@email.com \
    --SellerTaxpayerNum 111111133442424 \
    --TaxAmount 123 \
    --AmountHasTax 1 \
    --AmountWithoutTax 1 \
    --InvoiceType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585106014055",
        "Result": {
            "Message": "success",
            "Data": {
                "State": 1,
                "InvoiceId": "",
                "OrderSn": ""
            },
            "Code": 0
        }
    }
}
```

