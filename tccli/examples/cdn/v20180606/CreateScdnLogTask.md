**Example 1: 创建scdn日志事件任务**



Input: 

```
tccli cdn CreateScdnLogTask --cli-unfold-argument  \
    --Domain test.com \
    --AttackType xss \
    --Ip 10.0.0.1 \
    --AttackTypes xss \
    --DefenceMode observe \
    --Mode waf \
    --StartTime 2020-09-22 00:00:00 \
    --Domains test.com \
    --EndTime 2020-09-22 00:00:00 \
    --Conditions.0.Operator include \
    --Conditions.0.Value 10.0.0.1 \
    --Conditions.0.Key ip
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "RequestId": "1abbe623-4b0e-4727-ab51-7624902d47f4"
    }
}
```

