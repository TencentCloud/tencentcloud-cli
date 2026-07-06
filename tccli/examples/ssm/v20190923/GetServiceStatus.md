**Example 1: 获取 SSM 服务开通状态**

获取 SSM 服务开通状态

Input: 

```
tccli ssm GetServiceStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessKeyEscrowEnabled": true,
        "ExpireTime": "2027-02-01 19:30:31",
        "InvalidType": 1,
        "PayModel": "Prepaid_SSM",
        "QPSLimit": 1000,
        "RenewFlag": 1,
        "RequestId": "9a405d03-5cff-452b-bf0a-8576e2c1e1be",
        "ResourceId": "SSM-Prepaid-rt64sffg",
        "SecretLimit": 5900,
        "ServiceEnabled": true,
        "TotalCount": 5541
    }
}
```

