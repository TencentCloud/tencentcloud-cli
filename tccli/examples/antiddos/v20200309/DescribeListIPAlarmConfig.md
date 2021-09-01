**Example 1: 获取单IP告警阈值配置列表**



Input: 

```
tccli antiddos DescribeListIPAlarmConfig --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterIp 1.1.1.1 \
    --FilterInstanceId bgpip-0000011x \
    --FilterAlarmType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a3056c16-1cb6-4bdb-9d3b-a2361fe5b63c",
        "ConfigList": [
            {
                "AlarmType": 2,
                "AlarmThreshold": 2000,
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            },
            {
                "AlarmType": 1,
                "AlarmThreshold": 5000,
                "InstanceDetailList": [
                    {
                        "EipList": [
                            "1.1.1.1"
                        ],
                        "InstanceId": "bgpip-0000011x"
                    }
                ]
            }
        ],
        "Total": 2
    }
}
```

