**Example 1: 查询通道组列表**



Input: 

```
tccli gaap DescribeProxyGroupList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "ProxyGroupList": [
            {
                "CreateTime": 1768205812,
                "Domain": null,
                "FeatureBitmap": 7,
                "GroupId": "lg-joaaddy1",
                "GroupName": "group-name-01",
                "Http3Supported": 1,
                "ProjectId": 0,
                "ProxyType": 0,
                "RealServerRegionInfo": {
                    "FeatureBitmap": 207,
                    "IDCType": "dc",
                    "RegionArea": "EastChina",
                    "RegionAreaName": "EastChina",
                    "RegionId": "Shanghai",
                    "RegionName": "上海（原中国大陆-华东大区）",
                    "SupportFeature": null
                },
                "Status": "CHANGING",
                "TagSet": [],
                "Version": "3.0"
            }
        ],
        "TotalCount": 17,
        "RequestId": "5fa9ade4-b5b7-4306-9b62-7e67ee3823fc"
    }
}
```

