**Example 1: Web托管规则数据**



Input: 

```
tccli teo DescribeWebManagedRulesData --cli-unfold-argument  \
    --AttackType xx \
    --MetricNames xx \
    --ProtocolType xx \
    --Interval xx \
    --ZoneIds xx \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --Domains xx \
    --EndTime 2020-09-22T00:00:00+00:00
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
                                "Timestamp": 0,
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

