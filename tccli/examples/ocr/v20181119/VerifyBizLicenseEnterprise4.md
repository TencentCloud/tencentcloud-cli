**Example 1: 企业四要素核验**



Input: 

```
tccli ocr VerifyBizLicenseEnterprise4 --cli-unfold-argument  \
    --CreditCode 92130aaaaaaaa1BXA \
    --EntName 隆aaaaaaaa商户） \
    --LrName aba \
    --IdNum 13aaaaaaaa6
```

Output: 
```
{
    "Response": {
        "IsCreditCodeConsistent": true,
        "IsEntNameConsistent": true,
        "IsIdNumConsistent": false,
        "IsLrNameConsistent": true,
        "OperatingPeriod": "/",
        "OperatingStatus": "1",
        "RequestId": "6e6ef488-b1cf-4722-8f36-ae9386c22cb2",
        "StatusCode": 0,
        "VerifyResult": 0
    }
}
```

