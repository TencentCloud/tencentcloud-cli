**Example 1: 获取边界防护CC防护等级列表**



Input: 

```
tccli antiddos DescribeCCLevelList --cli-unfold-argument  \
    --Business edge \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794",
        "Total": 1,
        "LevelList": [
            {
                "InstanceId": "edge-000000xe",
                "Ip": "1.2.1.1",
                "Protocol": "HTTP",
                "Domain": "1.ase.com",
                "Level": "loose",
                "CreateTime": "2020-03-27 14:32:12",
                "ModifyTime": "2020-03-27 14:32:32"
            }
        ]
    }
}
```

