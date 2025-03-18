**Example 1: 反欺诈评分接口**



Input: 

```
tccli af GetAntiFraud --cli-unfold-argument  \
    --BusinessSecurityData.CustomerUin 12001 \
    --BusinessSecurityData.CustomerAppid 21001 \
    --BusinessSecurityData.IdNumber 0cec189e3b86c7e4fdb222355e128ed8 \
    --BusinessSecurityData.PhoneNumber 8412d6b9f44d948e1a105dc1e2bfcbd6 \
    --BusinessSecurityData.Scene 1000 \
    --BusinessSecurityData.Name 张三 \
    --BusinessSecurityData.IdCryptoType 1 \
    --BusinessSecurityData.PhoneCryptoType 1 \
    --BusinessSecurityData.NameCryptoType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Found": "1",
            "IdFound": "1",
            "RiskScore": "37",
            "RiskInfo": [],
            "Message": "Success",
            "CodeDesc": "Success",
            "Code": "0",
            "OtherModelScores": [],
            "PostTime": "1741231784",
            "ExtensionOut": ""
        },
        "RequestId": "febb48d4-761f-4032-9e99-f960fbbb4c79"
    }
}
```

