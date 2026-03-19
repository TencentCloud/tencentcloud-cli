**Example 1: 查看全部规则**

查看全部规则

Input: 

```
tccli cwp DescribeReverseShellRulesAggregation --cli-unfold-argument  \
    --Limit 2 \
    --Offset 0 \
    --Filters.0.Name WhiteType \
    --Filters.0.Values 0 1 \
    --By ModifyTime \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CreateTime": "2024-07-11 19:01:28",
                "DestIp": "",
                "DestPort": "",
                "GroupID": "adc1",
                "HandleHistory": 1,
                "Id": 1,
                "IsGlobal": 1,
                "MachinesNums": "全部服务器",
                "ModifyTime": "2024-07-11 19:01:28",
                "Operator": "",
                "ProcessName": "",
                "RuleRegexp": "ssh*.d",
                "Status": 0,
                "UuidHostips": [
                    {
                        "Hostip": "",
                        "Uuid": ""
                    }
                ],
                "WhiteType": 1
            },
            {
                "CreateTime": "2024-07-09 20:05:43",
                "DestIp": "",
                "DestPort": "",
                "GroupID": "adc1",
                "HandleHistory": 1,
                "Id": 2,
                "IsGlobal": 0,
                "MachinesNums": "2",
                "ModifyTime": "2024-07-11 16:57:00",
                "Operator": "",
                "ProcessName": "",
                "RuleRegexp": "sshd*c",
                "Status": 0,
                "UuidHostips": [
                    {
                        "Hostip": "1.1.1.2",
                        "Uuid": "8c09e1b1-5611-45b3-9c02-737996011b81"
                    },
                    {
                        "Hostip": "2.3.4.5",
                        "Uuid": "8c09e1b1-5611-45b3-9c02-737996011b82"
                    }
                ],
                "WhiteType": 1
            }
        ],
        "RequestId": "8c09e1b1-5611-45b3-9c02-737996011b8d",
        "TotalCount": 21
    }
}
```

