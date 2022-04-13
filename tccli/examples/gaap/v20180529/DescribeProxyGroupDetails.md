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
        "RequestId": "xx",
        "ProxyGroupDetail": {
            "Status": 0,
            "Http3Supported": 0,
            "Domain": "xx",
            "ClientIPMethod": [
                0
            ],
            "RealServerRegionInfo": {
                "RegionId": "xx",
                "RegionAreaName": "xx",
                "IDCType": "xx",
                "FeatureBitmap": 1,
                "RegionArea": "xx",
                "RegionName": "xx"
            },
            "TagSet": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "ProxyNum": 0,
            "CreateUin": "xx",
            "PackageType": "xx",
            "OwnerUin": "xx",
            "GroupId": "xx",
            "GroupName": "xx",
            "Version": "xx",
            "PolicyId": "xx",
            "IsOldGroup": false,
            "ProjectId": 0,
            "IPAddressVersion": "xx",
            "CreateTime": 1552978237,
            "DnsDefaultIp": "xx"
        }
    }
}
```

