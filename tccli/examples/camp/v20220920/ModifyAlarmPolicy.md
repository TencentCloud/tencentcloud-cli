**Example 1: ModifyAlarmPolicy**

修改告警策略基本信息

Input: 

```
tccli camp ModifyAlarmPolicy --cli-unfold-argument  \
    --ProjectID abc \
    --PolicyID abc \
    --Name abc \
    --Enable True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

