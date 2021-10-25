**Example 1: 获取边缘节点实例配额**



Input: 

```
tccli ecm DescribePackingQuotaGroup --cli-unfold-argument  \
    --Filters.0.Name Zone \
    --Filters.0.Values ap-beijing-ecm-ct \
    --Filters.1.Name InstanceType \
    --Filters.1.Values SN3ne.2XLARGE16 \
    --Filters.2.Name DataDiskSize \
    --Filters.2.Values 100
```

Output: 
```
{
    "Response": {
        "PackingQuotaSet": [
            {
                "ZoneId": 10580001,
                "Zone": "ap-beijing-ecm-cm3-1",
                "ISPId": "CMCC",
                "PackingQuotaInfos": [
                    {
                        "InstanceType": "S4.LARGE8",
                        "PackingQuota": 49
                    }
                ]
            },
            {
                "ZoneId": 10650001,
                "Zone": "ap-beijing-ecm-cu3-1",
                "ISPId": "CUCC",
                "PackingQuotaInfos": [
                    {
                        "InstanceType": "S4.LARGE8",
                        "PackingQuota": 100
                    },
                    {
                        "InstanceType": "SN3ne.LARGE8",
                        "PackingQuota": 5
                    }
                ]
            }
        ],
        "RequestId": "f32d1e05-a8cb-4848-a16c-2d6b4ce47420"
    }
}
```

