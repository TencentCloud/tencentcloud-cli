**Example 1: 查询通道组列表**



Input: 

```
tccli gaap DescribeProxyGroupList --cli-unfold-argument  \
    --ProjectId 0 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ProxyGroupList": [
            {
                "GroupId": "lg-nq8hpbvb",
                "Http3Supported": 1,
                "FeatureBitmap": 7,
                "Domain": null,
                "GroupName": "勿删-通道组",
                "ProjectId": 0,
                "RealServerRegionInfo": {
                    "RegionId": "Shanghai",
                    "RegionName": "上海（原中国大陆-华东大区）",
                    "RegionArea": "EastChina",
                    "RegionAreaName": "EastChina",
                    "IDCType": "dc",
                    "FeatureBitmap": 207,
                    "SupportFeature": null
                },
                "Status": "RUNNING",
                "TagSet": [],
                "Version": "3.0",
                "CreateTime": 1742284135,
                "ProxyType": 0
            }
        ],
        "RequestId": "c027bc0f-f904-43e7-8c3f-b1a3cfea0325"
    }
}
```

