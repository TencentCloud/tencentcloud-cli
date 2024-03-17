**Example 1: 定制接模接口示例**



Input: 

```
tccli afc QueryAntiFraudVip --cli-unfold-argument  \
    --AccountType 1%0D%0A \
    --AppIdU 100273020%0D%0A \
    --BankCardNumber 12345678%0D%0A \
    --BusinessId 0%0D%0A \
    --EmailAddress 373909726%2540qq.com%0D%0A \
    --IdNumber 1234567890%0D%0A \
    --Imei 54654654646%0D%0A \
    --Imsi xxxyyzz%0D%0A \
    --Name %25E6%259D%25A8%25E7%25BA%25A2%0D%0A \
    --PhoneNumber 008613246208548%0D%0A \
    --Uid 00000000000000000000000033121475%0D%0A \
    --Mac 00-01-6C-06-A6-29%0D%0A \
    --WifiSSID test%02wifi%0D%0A \
    --WifiBSSID 00-04-C3-A1-2B-22
```

Output: 
```
{
    "Response": {
        "CodeDesc": "Success",
        "Found": 1,
        "IdFound": -1,
        "RequestId": "23297af7-a805-4d9d-a9cb-825de5f8ed8c",
        "RiskInfo": [],
        "RiskScore": 800
    }
}
```

