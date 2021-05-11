**Example 1: 创建报警规则**



Input: 

```
tccli monitor CreateAlertRule --cli-unfold-argument  \
    --InstanceId my-prom-gg \
    --RuleState 2 \
    --Expr "up{service \
    --Duration 5m \
    --Receivers 34224 \
    --RuleName test
```

Output: 
```
{
    "Response": {
        "RequestId": "hfd437lxxdj3455-qxdb3eyydvw4doxm",
        "RuleId": "arule-f2vx2owo"
    }
}
```

