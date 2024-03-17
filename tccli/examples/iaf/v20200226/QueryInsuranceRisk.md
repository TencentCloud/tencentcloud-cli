**Example 1: 保险反欺诈接口示例**



Input: 

```
tccli iaf QueryInsuranceRisk --cli-unfold-argument  \
    --AccountType 1 \
    --AppIdU 100273020 \
    --Scene 123 \
    --BankCardNumber 12345678 \
    --BusinessId 0 \
    --EmailAddress 373909726%40qq.com \
    --IdNumber 1234567890 \
    --Imei 54654654646 \
    --PhoneNumber 008613246208548 \
    --Uid 00000000000000000000000033121475 \
    --UserIp 8.8.8.8 \
    --Mac 00-01-6C-06-A6-29 \
    --WifiSSID test_wifi \
    --WifiBSSID 00-04-C3-A1-2B-22
```

Output: 
```
{
    "Response": {
        "CodeDesc": "Success",
        "Found": 1,
        "IdFound": 1,
        "RequestId": "23297af7-a805-4d9d-a9cb-825de5f8ed8c",
        "RiskInfo": [
            {
                "RiskCode": 1107,
                "RiskCodeValue": 11
            }
        ],
        "RiskScore": 70
    }
}
```

