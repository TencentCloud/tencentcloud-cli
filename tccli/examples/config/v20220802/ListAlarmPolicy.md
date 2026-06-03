**Example 1: 查询告警列表**



Input: 

```
tccli config ListAlarmPolicy --cli-unfold-argument  \
    --Offset 10 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "AlarmPolicyList": [],
        "Total": 2,
        "RequestId": "04ec0d59-723e-4800-ae75-5209394aeabf"
    }
}
```

