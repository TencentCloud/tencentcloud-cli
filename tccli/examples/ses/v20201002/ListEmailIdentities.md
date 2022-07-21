**Example 1: 获取列表**



Input: 

```
tccli ses ListEmailIdentities --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "EmailIdentities": [
            {
                "IdentityName": "mail.qcloud.com",
                "IdentityType": "DOMAIN",
                "SendingEnabled": false,
                "CurrentReputationLevel": 2,
                "DailyQuota": 5000
            }
        ],
        "MaxReputationLevel": 10,
        "MaxDailyQuota": 10000
    }
}
```

