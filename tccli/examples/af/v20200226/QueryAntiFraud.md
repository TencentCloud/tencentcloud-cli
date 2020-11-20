**Example 1: 借贷反欺诈接口示例**



Input: 

```
tccli af QueryAntiFraud --cli-unfold-argument  \
    --AccountType 1 \
    --AppIdU 100273020 \
    --BankCardNumber 12345678 \
    --BusinessId 0 \
    --EmailAddress 373909726%40qq.com \
    --IdNumber 1234567890 \
    --Imei 54654654646 \
    --Imsi xxxyyzz \
    --Name %E6%9D%A8%E7%BA%A2 \
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
        "RiskInfo": [
            {
                "RiskCode": 1
            }
        ],
        "IdFound": 1,
        "RequestId": "07c816d7-5bc3-4e95-ba1f-32ce3e5683e5",
        "CodeDesc": "Success",
        "Found": 1,
        "RiskScore": 70
    }
}
```

