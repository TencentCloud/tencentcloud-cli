**Example 1: 查询地域以及可用区**



Input: 

```
tccli bm DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionInfoSet": [
            {
                "RegionId": 1,
                "RegionDescription": "华南地区（广州）",
                "Region": "ap-guangzhou",
                "ZoneInfoSet": [
                    {
                        "ZoneId": 1000100003,
                        "ZoneDescription": "广州物理机一区 ",
                        "Zone": "ap-guangzhou-bls-1"
                    }
                ]
            },
            {
                "RegionId": 4,
                "RegionDescription": "华东地区（上海）",
                "Region": "ap-shanghai",
                "ZoneInfoSet": [
                    {
                        "ZoneId": 1000400001,
                        "ZoneDescription": "上海物理机一区",
                        "Zone": "ap-shanghai-bls-1"
                    },
                    {
                        "ZoneId": 1000400003,
                        "ZoneDescription": "上海物理机三区",
                        "Zone": "ap-shanghai-bls-3"
                    }
                ]
            },
            {
                "RegionId": 8,
                "RegionDescription": "华北地区（北京）",
                "Region": "ap-beijing",
                "ZoneInfoSet": [
                    {
                        "ZoneId": 1000800001,
                        "ZoneDescription": "北京物理机一区",
                        "Zone": "ap-beijing-bls-1"
                    },
                    {
                        "ZoneId": 1000800002,
                        "ZoneDescription": "北京物理机二区",
                        "Zone": "ap-beijing-bls-2"
                    },
                    {
                        "ZoneId": 1000800003,
                        "ZoneDescription": "北京物理机三区",
                        "Zone": "ap-beijing-bls-3"
                    },
                    {
                        "ZoneId": 1000800004,
                        "ZoneDescription": "北京物理机四区",
                        "Zone": "ap-beijing-bls-4"
                    }
                ]
            },
            {
                "RegionId": 19,
                "RegionDescription": "西南地区（重庆）",
                "Region": "ap-chongqing",
                "ZoneInfoSet": [
                    {
                        "ZoneId": 1001900001,
                        "ZoneDescription": "重庆物理机一区",
                        "Zone": "ap-chongqing-bls-1"
                    }
                ]
            }
        ],
        "RequestId": "63caeffd-4782-4704-87d6-c9ce36532c0e"
    }
}
```

