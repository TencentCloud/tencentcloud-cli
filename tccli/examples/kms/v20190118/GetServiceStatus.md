**Example 1: 查询服务状态**

查询服务状态

Input: 

```
tccli kms GetServiceStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ServiceEnabled": true,
        "InvalidType": 1,
        "UserLevel": 0,
        "ProResourceId": "kms_pro_12345",
        "ProRenewFlag": 1,
        "ProExpireTime": 1603701385,
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00",
        "ExclusiveHSMEnabled": false,
        "ExclusiveVSMEnabled": false,
        "SubscriptionInfo": "Prepaid_KMS"
    }
}
```

