**Example 1: 获取服务开启状态**



Input: 

```
tccli ssm GetServiceStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "1a327ad8-5fef-41d5-b1a1-73d58af83d66",
        "ServiceEnabled": true,
        "InvalidType": 1,
        "AccessKeyEscrowEnabled": true
    }
}
```

