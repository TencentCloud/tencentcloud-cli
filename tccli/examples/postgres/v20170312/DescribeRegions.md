**Example 1: 查询所有地域**



Input: 

```
tccli postgres DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "0872c9bb-0540-4ac4-80cf-ba63bd771b0a",
        "TotalCount": 7,
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "华南地区(广州)",
                "RegionId": 1,
                "SupportInternational": 0,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-chengdu",
                "RegionName": "西南地区(成都)",
                "RegionId": 16,
                "SupportInternational": 0,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "华东地区(上海)",
                "RegionId": 4,
                "SupportInternational": 0,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-toronto",
                "RegionName": "北美地区(多伦多)",
                "RegionId": 6,
                "SupportInternational": 1,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "ap-shanghai-fsi",
                "RegionName": "华东地区(上海金融)",
                "RegionId": 7,
                "SupportInternational": 0,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "华北地区(北京)",
                "RegionId": 8,
                "SupportInternational": 0,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-siliconvalley",
                "RegionName": "美国西部(硅谷)",
                "RegionId": 15,
                "SupportInternational": 1,
                "RegionState": "AVAILABLE"
            }
        ]
    }
}
```

