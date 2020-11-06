**Example 1: 借贷反欺诈接口示例**



Input: 

```
tccli af QueryAntiFraud --cli-unfold-argument  \
    --Nonce 62972 \
    --Region all \
    --SecretId AKIDufPRYgmsWyC8NtsRMq3t8CdkGWohJNmE \
    --Timestamp 1467872277 \
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
    --PostTime 1436664316 \
    --Uid 00000000000000000000000033121475 \
    --UserIp 8.8.8.8 \
    --mac 00-01-6C-06-A6-29 \
    --WifiSSID testwifi \
    --WifiBSSID 00-04-C3-A1-2B-22 \
    --Signature Wn0Wuy3jkncGNvwf485XMxJaVmU%3D
```

Output: 
```
{
    "CodeDesc": "Success",
    "Found": 1,
    "IdFound": 1,
    "PostTime": "1436664316",
    "RiskInfo": [
        {
            "RiskCode": 1107
        }
    ],
    "RiskScore": 70
}
```

