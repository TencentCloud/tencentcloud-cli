**Example 1: 查询数据库代理规格配置**



Input: 

```
tccli cdb DescribeProxyCustomConf --cli-unfold-argument  \
    --InstanceId cdb-2wpip1dd \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "CustomConfInfo": [
            {
                "Device": "Z3",
                "Type": "高可用版本",
                "DeviceType": "custom",
                "Memory": 4000,
                "Cpu": 2
            }
        ],
        "WeightRule": {
            "LessThan": 2000,
            "Weight": 1
        },
        "RequestId": "9bd2a785-2dc0-47dc-b285-2b154a218ea1"
    }
}
```

