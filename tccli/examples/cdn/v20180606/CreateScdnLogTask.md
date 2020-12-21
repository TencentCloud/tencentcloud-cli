**Example 1: 创建scdn日志事件任务**



Input: 

```
tccli cdn CreateScdnLogTask --cli-unfold-argument  \
    --Domain xx \
    --AttackType xx \
    --Ip xx \
    --AttackTypes xx \
    --DefenceMode xx \
    --Mode xx \
    --StartTime 2020-09-22 00:00:00 \
    --Domains xx \
    --EndTime 2020-09-22 00:00:00 \
    --Conditions.0.Operator xx \
    --Conditions.0.Value xx \
    --Conditions.0.Key xx
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "RequestId": "xx"
    }
}
```

