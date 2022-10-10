**Example 1: QueryCompanyTitle**



Input: 

```
tccli cpdp QueryCompanyTitle --cli-unfold-argument  \
    --Profile test \
    --CompanyTitleKeyword 公司 \
    --SellerTaxpayerNum xx \
    --InvoicePlatformId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585106014055",
        "ErrCode": "SUCCESS",
        "ErrMessage": "请求成功",
        "Result": {
            "CompanyName": "xx",
            "CompanyAddress": "xx",
            "CompanyPhone": "xx",
            "CompanyTaxpayerNum": "xx",
            "CompanyBankAccount": "xx",
            "CompanyBankName": "xx"
        }
    }
}
```

