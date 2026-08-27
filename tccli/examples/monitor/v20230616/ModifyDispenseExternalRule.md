**Example 1: 转发规则修改**



Input: 

```
tccli monitor ModifyDispenseExternalRule --cli-unfold-argument  \
    --Name hyzev-test \
    --ExtNamespace QCE/CVM \
    --Producer.ProtocolType 2 \
    --Producer.Type Kafka \
    --Producer.Brokers 11.150.215.105:9092 \
    --Producer.Topic Barad_Hyzevtest \
    --Producer.Username hyzev \
    --Producer.Password *** \
    --RuleId 8388612 \
    --Period 60 \
    --DispenseConditions.0.ExtMetric DiskUsage \
    --DispenseConditions.0.DispenseFilters.0.Key appid2 \
    --DispenseConditions.0.DispenseFilters.0.Values 1258344701 \
    --DispenseConditions.0.DispenseFilters.0.Expression =
```

Output: 
```
{
    "Response": {
        "RequestId": "a7acc9ea-585c-4c6d-b482-d919e431b82c"
    }
}
```

