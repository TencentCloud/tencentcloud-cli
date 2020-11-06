**Example 1: 获取L4转发规则健康检查异常结果**



Input: 

```
tccli dayu DescribeL4RulesErrHealth --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Total": 1,
        "ErrHealths": [
            {
                "Key": "rule-00000001",
                "Value": "1.1.1.1,2.2.2.2"
            }
        ],
        "ExtErrHealths": [
            {
                "Record": [
                    {
                        "Key": "RuleId",
                        "Value": "rule-00000001"
                    },
                    {
                        "Key": "Protocol",
                        "Value": "TCP"
                    },
                    {
                        "Key": "VirtualPort",
                        "Value": "1234"
                    },
                    {
                        "Key": "ErrMessage",
                        "Value": "SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6,SourceIp:2.2.2.2|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6"
                    }
                ]
            }
        ]
    }
}
```

