**Example 1: 查询数据库代理规格配置**



Input: 

```
tccli cdb DescribeProxyCustomConf --cli-unfold-argument  \
    --InstanceId xx \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Count": 3,
        "CustomConf": [
            {
                "Cpu": 2,
                "Device": "Z3",
                "DeviceType": "custom",
                "Memory": 4000,
                "Type": "高可用版本"
            },
            {
                "Cpu": 4,
                "Device": "Z3",
                "DeviceType": "custom",
                "Memory": 8000,
                "Type": "高可用版本"
            },
            {
                "Cpu": 8,
                "Device": "Z3",
                "DeviceType": "custom",
                "Memory": 16000,
                "Type": "高可用版本"
            }
        ],
        "RequestId": "9bd2a785-2dc0-47dc-b285-2b154a218ea1",
        "WeightRule": [
            {
                "LessThan": 2000,
                "Weight": 1
            },
            {
                "LessThan": 8000,
                "Weight": 2
            },
            {
                "LessThan": 16000,
                "Weight": 4
            },
            {
                "LessThan": 32000,
                "Weight": 8
            },
            {
                "LessThan": 48000,
                "Weight": 10
            },
            {
                "LessThan": 64000,
                "Weight": 12
            },
            {
                "LessThan": 96000,
                "Weight": 14
            },
            {
                "LessThan": 128000,
                "Weight": 16
            },
            {
                "LessThan": 192000,
                "Weight": 24
            },
            {
                "LessThan": 256000,
                "Weight": 30
            },
            {
                "LessThan": 488000,
                "Weight": 50
            },
            {
                "LessThan": 690000,
                "Weight": 75
            },
            {
                "LessThan": -1,
                "Weight": 100
            }
        ]
    }
}
```

