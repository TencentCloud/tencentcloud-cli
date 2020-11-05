**Example 1: Querying all regions**



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
                "RegionName": "South China (Guangzhou)",
                "RegionId": 1,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-chengdu",
                "RegionName": "Southwest China (Chengdu)",
                "RegionId": 16,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "East China (Shanghai)",
                "RegionId": 4,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-toronto",
                "RegionName": "North America (Toronto)",
                "RegionId": 6,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "ap-shanghai-fsi",
                "RegionName": "East China (Shanghai Finance)",
                "RegionId": 7,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "North China (Beijing)",
                "RegionId": 8,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-siliconvalley",
                "RegionName": "West US (Silicon Valley)",
                "RegionId": 15,
                "RegionState": "AVAILABLE"
            }
        ]
    }
}
```

