**Example 1: CreateRedInvoiceV2**



Input: 

```
tccli cpdp CreateRedInvoiceV2 --cli-unfold-argument  \
    --InvoicePlatformId 0 \
    --OrderId test195992
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585106019061",
        "ErrCode": "SUCCESS",
        "ErrMessage": "请求成功",
        "Result": {
            "InvoiceId": "123456"
        }
    }
}
```

