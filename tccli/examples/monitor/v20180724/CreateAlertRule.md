**Example 1: 创建报警规则**



Input: 

```
tccli monitor CreateAlertRule --cli-unfold-argument  \
    --Receivers 34224 \
    --InstanceId prom-abcd1234 \
    --Expr "up{service=\"rig-prometheus-agent\"}>0" \
    --Duration 5m \
    --RuleName test \
    --RuleState 2
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

