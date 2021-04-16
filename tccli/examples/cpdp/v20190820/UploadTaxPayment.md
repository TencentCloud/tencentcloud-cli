**Example 1: 直播平台-上传代理商完税证明**



Input: 

```
tccli cpdp UploadTaxPayment --cli-unfold-argument  \
    --Channel 1 \
    --TaxId tax-xxx \
    --FileUrl http://cos.qcloud.com/tax.xlsx
```

Output: 
```
{
    "Response": {
        "RequestId": "8aadd86c-1727-40ef-9927-9f87201449af"
    }
}
```

