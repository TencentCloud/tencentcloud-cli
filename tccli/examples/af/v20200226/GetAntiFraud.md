**Example 1: 反欺诈评分接口**



Input: 

```
tccli af GetAntiFraud --cli-unfold-argument  \
    --BusinessSecurityData.AppIdU 0 \
    --BusinessSecurityData.PhoneCryptoType 0 \
    --BusinessSecurityData.WifiSSID 0 \
    --BusinessSecurityData.IdCryptoType 0 \
    --BusinessSecurityData.Imsi 0 \
    --BusinessSecurityData.CustomerSubUin 0 \
    --BusinessSecurityData.Mac 0 \
    --BusinessSecurityData.Idfa 0 \
    --BusinessSecurityData.Authorization 0 \
    --BusinessSecurityData.Address 0 \
    --BusinessSecurityData.Imei 0 \
    --BusinessSecurityData.WifiBSSID 0 \
    --BusinessSecurityData.BankCardNumber 0 \
    --BusinessSecurityData.ExtensionId 0 \
    --BusinessSecurityData.Name 0 \
    --BusinessSecurityData.ExtensionIn 0 \
    --BusinessSecurityData.CustomerUin 0 \
    --BusinessSecurityData.UserIp 0 \
    --BusinessSecurityData.PhoneNumber 0 \
    --BusinessSecurityData.CustomerAppid 0 \
    --BusinessSecurityData.NameCryptoType 0 \
    --BusinessSecurityData.Uid 0 \
    --BusinessSecurityData.WifiMac xx \
    --BusinessSecurityData.BusinessId 0 \
    --BusinessSecurityData.Scene 0 \
    --BusinessSecurityData.IdNumber 0 \
    --BusinessSecurityData.EmailAddress 0 \
    --BusinessSecurityData.AccountType 0 \
    --BusinessCryptoData.CryptoType 0 \
    --BusinessCryptoData.CryptoContent 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "OtherModelScores": "00",
            "PostTime": "00",
            "Code": "00",
            "RiskInfo": "00",
            "ExtensionOut": "00",
            "IdFound": "00",
            "CodeDesc": "00",
            "Found": "00",
            "Message": "00",
            "RiskScore": "00"
        },
        "RequestId": "00"
    }
}
```

