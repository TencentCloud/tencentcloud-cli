**Example 1: 获取CC清洗阈值列表**



Input: 

```
tccli antiddos DescribeCCThresholdList --cli-unfold-argument  \
    --Business bgp-multip \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794",
        "Total": 1,
        "ThresholdList": [
            {
                "InstanceId": "bgp-000000432",
                "Ip": "1.2.1.1",
                "Protocol": "HTTP",
                "Domain": "1.ase.com",
                "Threshold": 1000,
                "CreateTime": "2020-03-27 14:32:12",
                "ModifyTime": "2020-03-27 14:32:32"
            }
        ]
    }
}
```

