**Example 1: 获取地域列表**

获取地域列表

Input: 

```
tccli tcaplusdb DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionInfos": [
            {
                "RegionAbbr": "sh",
                "RegionId": 4,
                "RegionName": "Shanghai",
                "Ipv6Enable": "1"
            },
            {
                "RegionAbbr": "gz",
                "RegionId": 1,
                "RegionName": "Guangzhou",
                "Ipv6Enable": "0"
            },
            {
                "RegionAbbr": "hk",
                "RegionId": 5,
                "RegionName": "Hongkong",
                "Ipv6Enable": "1"
            }
        ],
        "RequestId": "b64fa31b-a0ca-4a06-82e9-211d610ba516",
        "TotalCount": 3
    }
}
```

