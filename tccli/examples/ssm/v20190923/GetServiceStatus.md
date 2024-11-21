**Example 1: 获取服务开启状态**



Input: 

```
tccli ssm GetServiceStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessKeyEscrowEnabled": true,
        "ExpireTime": "2024-09-10 10:19:21",
        "InvalidType": 1,
        "PayModel": "Postpaid_SSM",
        "QPSLimit": 0,
        "RenewFlag": 0,
        "RequestId": "b370f1c4-3e1c-4922-8ab2-6f717240f6ad",
        "ResourceId": "test-rsid",
        "SecretLimit": 0,
        "ServiceEnabled": true,
        "TotalCount": 0
    }
}
```

