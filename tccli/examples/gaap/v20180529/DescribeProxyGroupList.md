**Example 1: 查询通道组列表**



Input: 

```
tccli gaap DescribeProxyGroupList --cli-unfold-argument  \
    --ProjectId 0 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "8b6bb93c-0dce-4513-a274-1410f276307c",
        "ProxyGroupList": [
            {
                "Status": 0,
                "Domain": null,
                "ProjectId": 0,
                "GroupName": "t4",
                "TagSet": [],
                "RealServerRegionInfo": {
                    "RegionId": "EastChina",
                    "RegionName": "EastChina",
                    "RegionArea": "EastChina",
                    "RegionAreaName": "EastChina",
                    "IDCType": "ec"
                },
                "GroupId": "lg-mh4k07v5"
            },
            {
                "Status": 0,
                "Domain": null,
                "ProjectId": 0,
                "GroupName": "sandytest2",
                "TagSet": [],
                "RealServerRegionInfo": {
                    "RegionId": "EastChina",
                    "RegionName": "EastChina",
                    "RegionArea": "EastChina",
                    "RegionAreaName": "EastChina",
                    "IDCType": "ec"
                },
                "GroupId": "lg-d5y6ei3b"
            }
        ]
    }
}
```

