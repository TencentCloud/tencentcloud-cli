**Example 1: 金融借贷反欺诈接口示例----加密请求**



Input: 

```
tccli af DescribeAntiFraud --cli-unfold-argument  \
    --BusinessCryptoData.CryptoType 1 \
    --BusinessCryptoData.CryptoContent mpa4yYHKA0QAky02zcMIawK2P8Irhk9UYn9+/lwMGeGrUVRF7tSJWAw7tYPB5Qx15vJ9ifBnzzvCW4AQCZucI3Uxe7JnP1OJnYy/oPykxIeJzNkE/7lzNyKLiZD954K3FqaQ2AZ0lioXpYUX+r2W7g==
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": "0",
            "Message": "Success",
            "Found": "1",
            "IdFound": "1",
            "RiskScore": "61",
            "RiskInfo": [
                {
                    "RiskCode": "21001",
                    "RiskValue": "2"
                }
            ],
            "OtherModelScores": [
                {
                    "ModelId": "0",
                    "ModelScore": "61"
                },
                {
                    "ModelId": "1",
                    "ModelScore": "36"
                }
            ]
        },
        "RequestId": "07c816d7-5bc3-4e95-ba1f-32ce3e5683e5"
    }
}
```

**Example 2: 金融借贷反欺诈接口示例----明文请求**



Input: 

```
tccli af DescribeAntiFraud --cli-unfold-argument  \
    --BusinessSecurityData.AppIdU xx \
    --BusinessSecurityData.PhoneCryptoType xx \
    --BusinessSecurityData.WifiSSID xx \
    --BusinessSecurityData.IdCryptoType xx \
    --BusinessSecurityData.Imsi xx \
    --BusinessSecurityData.Mac xx \
    --BusinessSecurityData.Idfa xx \
    --BusinessSecurityData.Address xx \
    --BusinessSecurityData.UserIp xx \
    --BusinessSecurityData.WifiBSSID xx \
    --BusinessSecurityData.BankCardNumber xx \
    --BusinessSecurityData.Name xx \
    --BusinessSecurityData.Imei xx \
    --BusinessSecurityData.PhoneNumber xx \
    --BusinessSecurityData.NameCryptoType xx \
    --BusinessSecurityData.Uid xx \
    --BusinessSecurityData.WifiMac xx \
    --BusinessSecurityData.BusinessId xx \
    --BusinessSecurityData.Scene xx \
    --BusinessSecurityData.IdNumber xx \
    --BusinessSecurityData.EmailAddress xx \
    --BusinessSecurityData.AccountType xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": "0",
            "Message": "Success",
            "Found": "1",
            "IdFound": "1",
            "RiskScore": "61",
            "RiskInfo": [
                {
                    "RiskCode": "21001",
                    "RiskValue": "2"
                }
            ],
            "OtherModelScores": [
                {
                    "ModelId": "0",
                    "ModelScore": "61"
                },
                {
                    "ModelId": "1",
                    "ModelScore": "36"
                }
            ]
        },
        "RequestId": "07c816d7-5bc3-4e95-ba1f-32ce3e5683e5"
    }
}
```

