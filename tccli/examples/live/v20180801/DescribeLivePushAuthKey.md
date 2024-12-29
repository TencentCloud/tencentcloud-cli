**Example 1: 请求示例**



Input: 

```
tccli live DescribeLivePushAuthKey --cli-unfold-argument  \
    --DomainName 5000.livepush.myqcloud.com
```

Output: 
```
{
    "Response": {
        "PushAuthKeyInfo": {
            "DomainName": "5000.livepush.myqcloud.com",
            "Enable": 1,
            "MasterAuthKey": "PUl5VIKKFB1KazNB",
            "BackupAuthKey": "AKID0QJ82oYdLJIgA",
            "AuthDelta": 300
        },
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

