**Example 1: 设置扩缩容缓冲值**



Input: 

```
tccli gse PutScalingPolicy --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-ay03mhdm \
    --Name scaling1 \
    --PolicyType TargetBased \
    --MetricName PercentAvailableGameServerSessions \
    --TargetConfiguration.TargetValue 30
```

Output: 
```
{
    "Response": {
        "Name": "",
        "RequestId": "a6b88256-7dc4-4682-99ed-9e10dfb66044"
    }
}
```

