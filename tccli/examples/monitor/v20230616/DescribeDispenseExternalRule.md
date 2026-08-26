**Example 1: 转发规则查询，指定id**



Input: 

```
tccli monitor DescribeDispenseExternalRule --cli-unfold-argument  \
    --RuleId 8388612
```

Output: 
```
{
    "Response": {
        "Rule": {
            "DispenseConditions": [
                {
                    "ConditionId": 8388609,
                    "DispenseFilters": [
                        {
                            "Expression": "=",
                            "Key": "appid2",
                            "Values": [
                                "1258344701"
                            ]
                        }
                    ],
                    "ExtMetric": "DiskUsage"
                }
            ],
            "DispenseRegions": [
                "gz"
            ],
            "ExtMetric": [],
            "ExtNamespace": "QCE/CVM",
            "Name": "hyzev-test",
            "Period": [
                60
            ],
            "Producer": {
                "Brokers": "11.150.215.105:9092",
                "Merge": 1,
                "Password": "***",
                "ProtocolType": 2,
                "Topic": "Barad_Hyzevtest",
                "Type": "Kafka",
                "Username": "hyzev"
            },
            "RuleId": 8388612,
            "Status": 1,
            "UpdateTime": 1755228861
        },
        "RequestId": "a61604bc-cae2-495e-980f-0f61fbd40218"
    }
}
```

