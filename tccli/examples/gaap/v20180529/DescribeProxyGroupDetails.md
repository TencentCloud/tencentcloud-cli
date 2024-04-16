**Example 1: 查询通道组详情**



Input: 

```
tccli gaap DescribeProxyGroupDetails --cli-unfold-argument  \
    --GroupId lg
```

Output: 
```
{
    "Response": {
        "ProxyGroupDetail": {
            "CreateTime": 0,
            "ProjectId": 0,
            "ProxyNum": 0,
            "Status": 0,
            "OwnerUin": "abc",
            "CreateUin": "abc",
            "GroupName": "abc",
            "DnsDefaultIp": "abc",
            "Domain": "abc",
            "RealServerRegionInfo": {
                "RegionId": "abc",
                "RegionName": "abc",
                "RegionArea": "abc",
                "RegionAreaName": "abc",
                "IDCType": "abc",
                "FeatureBitmap": 1,
                "SupportFeature": {
                    "NetworkType": [
                        "abc"
                    ]
                }
            },
            "IsOldGroup": true,
            "GroupId": "abc",
            "TagSet": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "PolicyId": "abc",
            "Version": "abc",
            "ClientIPMethod": [
                0
            ],
            "IPAddressVersion": "abc",
            "PackageType": "abc",
            "Http3Supported": 0,
            "FeatureBitmap": 0,
            "IsSupportTLSChoice": 1
        },
        "RequestId": "abc"
    }
}
```

