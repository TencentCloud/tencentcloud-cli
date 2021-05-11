**Example 1: 更新报警规则**



Input: 

```
tccli monitor UpdateAlertRule --cli-unfold-argument  \
    --InstanceId my-prom-gg \
    --RuleId arule-omq28fcm \
    --RuleState 2 \
    --RuleName exampleName \
    --Expr job:request_latency_seconds:mean5m{job \
    --Duration 1m \
    --Receivers 33432
```

Output: 
```
{
    "Response": {
        "RequestId": "qyh38g1ium4-41o5k994o7hcxuq96zab",
        "RuleId": "arule-omq28fcm"
    }
}
```

