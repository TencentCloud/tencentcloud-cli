**Example 1: Querying available acceleration regions by origin server region**



Input: 

```
tccli gaap DescribeAccessRegionsByDestRegion --cli-unfold-argument  \
    --DestRegion SouthChina
```

Output: 
```
{
    "Response": {
        "AccessRegionSet": [
            {
                "RegionId": "eu-moscow",
                "RegionName": "Russia",
                "ConcurrentList": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "BandwidthList": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ]
            }
        ],
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd",
        "TotalCount": 1
    }
}
```

