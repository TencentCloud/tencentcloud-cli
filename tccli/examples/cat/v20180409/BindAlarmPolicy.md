**Example 1: 绑定告警策略组示例**



Input: 

```
tccli cat BindAlarmPolicy --cli-unfold-argument  \
    --TaskId 260228 \
    --PolicyGroupId 3 \
    --IfBind 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1bf13711-6023-43db-885b-596186e61bd1"
    }
}
```

