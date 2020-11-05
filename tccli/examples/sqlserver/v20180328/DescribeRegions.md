**Example 1: Querying all regions**



Input: 

```
tccli sqlserver DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "9b0beca5-f3ea-44d3-97de-ec8f02effaea",
        "TotalCount": 9,
        "RegionSet": [
            {
                "Region": "ap-hongkong",
                "RegionName": "Hong Kong (China)",
                "RegionId": 5,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai-fsi",
                "RegionName": "Shanghai Finance",
                "RegionId": 7,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shantou",
                "RegionName": "Shantou",
                "RegionId": 2,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "ap-tianjin",
                "RegionName": "Tianjin",
                "RegionId": 3,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "na-toronto",
                "RegionName": "North America",
                "RegionId": 6,
                "RegionState": "UNAVAILABLE"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "Beijing",
                "RegionId": 8,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shenzhen-fsi",
                "RegionName": "Shenzhen Finance",
                "RegionId": 11,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-guangzhou",
                "RegionName": "Guangzhou",
                "RegionId": 1,
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "Shanghai",
                "RegionId": 4,
                "RegionState": "AVAILABLE"
            }
        ]
    }
}
```

