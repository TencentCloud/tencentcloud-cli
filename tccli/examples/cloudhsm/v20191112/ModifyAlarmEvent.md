**Example 1: 修改告警事件**

修改告警事件

Input: 

```
tccli cloudhsm ModifyAlarmEvent --cli-unfold-argument  \
    --Event CPU \
    --Limit 0 \
    --Status 0 \
    --BeginTime 00:00:00 \
    --EndTime 23:59:59
```

Output: 
```
{
    "Response": {
        "RequestId": "123456789"
    }
}
```

