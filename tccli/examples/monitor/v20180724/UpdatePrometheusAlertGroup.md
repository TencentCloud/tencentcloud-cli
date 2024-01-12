**Example 1: 更新告警分组**



Input: 

```
tccli monitor UpdatePrometheusAlertGroup --cli-unfold-argument  \
    --GroupId alert-34xae12s \
    --InstanceId prom-7vp71mk0 \
    --GroupName 更新告警分组测试 \
    --AMPReceivers notice-xxxxxx \
    --Rules.0.RuleName 规则-1 \
    --Rules.0.Labels.0.Key k1 \
    --Rules.0.Labels.0.Value v1 \
    --Rules.0.Annotations.0.Key summary \
    --Rules.0.Annotations.0.Value {{$value}} \
    --Rules.0.Annotations.1.Key describe \
    --Rules.0.Annotations.1.Value 规则1告警 \
    --Rules.0.Expr expr1
```

Output: 
```
{
    "Response": {
        "GroupId": "alert-34xae12s",
        "RequestId": "02c92b99-abc9-431b-8b08-42b9977d51cf"
    }
}
```

