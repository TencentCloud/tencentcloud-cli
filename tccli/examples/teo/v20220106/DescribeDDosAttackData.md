**Example 1: 查询DDos攻击日志**



Input: 

```
tccli teo DescribeDDosAttackData --cli-unfold-argument  \
    --AttackType xx \
    --MetricNames xx \
    --ProtocolType xx \
    --Interval xx \
    --PolicyIds 0 \
    --ZoneIds xx \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00 \
    --Port 0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Msg": "xx",
        "Interval": "xx",
        "Data": [
            {
                "Value": [
                    {
                        "Max": 0,
                        "Metric": "xx",
                        "Avg": 0.0,
                        "Detail": [
                            {
                                "Value": 0
                            }
                        ],
                        "Sum": 0.0
                    }
                ],
                "Key": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

