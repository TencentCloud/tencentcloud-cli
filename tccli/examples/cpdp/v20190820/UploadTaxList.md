**Example 1: 直播平台-上传代理商完税列表**



Input: 

```
tccli cpdp UploadTaxList --cli-unfold-argument  \
    --Channel 1 \
    --BeginMonth 2020-10 \
    --EndMonth 2020-11 \
    --FileUrl http://cos.qcloud.com/tax.xlsx
```

Output: 
```
{
    "Response": {
        "TaxId": "tax-0db3m7jtef",
        "RequestId": "8aadd86c-1727-40ef-9927-9f87201449af"
    }
}
```

