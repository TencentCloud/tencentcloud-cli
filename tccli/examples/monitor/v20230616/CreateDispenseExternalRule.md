**Example 1: 转发接口：创建转发规则**



Input: 

```
tccli monitor CreateDispenseExternalRule --cli-unfold-argument  \
    --Name honor-qce/lb-lb_vip3 \
    --ExtNamespace QCE/LB \
    --ExtMetrics VConnum VNewConn \
    --Period 60 \
    --Producer.ProtocolType 2 \
    --Producer.Type Kafka \
    --Producer.Brokers 127.0.0.1 \
    --Producer.Topic Barad_Comm \
    --DispenseConditions.0.ExtMetric VConnum \
    --DispenseConditions.0.DispenseFilters.0.Key uuid \
    --DispenseConditions.0.DispenseFilters.0.Values 123 \
    --DispenseConditions.0.DispenseFilters.0.Expression = \
    --DispenseConditions.1.ExtMetric VConnum \
    --DispenseConditions.1.DispenseFilters.0.Key appid \
    --DispenseConditions.1.DispenseFilters.0.Values 123 \
    --DispenseConditions.1.DispenseFilters.0.Expression = \
    --DispenseConditions.2.ExtMetric VNewConn \
    --DispenseConditions.2.DispenseFilters.0.Key test \
    --DispenseConditions.2.DispenseFilters.0.Values 124 \
    --DispenseConditions.2.DispenseFilters.0.Expression in
```

Output: 
```
{
    "Response": {
        "RequestId": "e897c5d2-fa85-47c4-85e6-3491517e0dd0",
        "RuleId": 17
    }
}
```

