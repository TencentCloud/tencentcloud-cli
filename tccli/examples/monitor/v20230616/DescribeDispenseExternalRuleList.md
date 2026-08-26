**Example 1: 转发规则列表查询**



Input: 

```
tccli monitor DescribeDispenseExternalRuleList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 4
```

Output: 
```
{
    "Response": {
        "RuleList": [
            {
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
            }
        ],
        "TotalCount": 22,
        "RequestId": "428f911a-871e-4138-8a7b-c425bacb0398"
    }
}
```

