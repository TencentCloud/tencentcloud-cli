**Example 1: 查询通道实例列表**



Input: 

```
tccli gaap DescribeProxies --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name AccessRegion \
    --Filters.0.Values ap-hongkong
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AccessRegionInfo": {
                    "RegionId": "xx",
                    "RegionAreaName": "xx",
                    "IDCType": "xx",
                    "FeatureBitmap": 1,
                    "RegionArea": "xx",
                    "RegionName": "xx"
                },
                "RelatedGlobalDomains": [
                    "xx"
                ],
                "Version": "xx",
                "PolicyId": "xx",
                "Scalarable": 1,
                "IPList": [
                    {
                        "IP": "xx",
                        "Bandwidth": 0,
                        "Provider": "xx"
                    }
                ],
                "Status": "xx",
                "ProxyType": 1,
                "ForwardIP": "xx",
                "ProxyId": "xx",
                "RealServerRegion": "xx",
                "Concurrent": 2,
                "RealServerRegionInfo": {
                    "RegionId": "xx",
                    "RegionAreaName": "xx",
                    "IDCType": "xx",
                    "FeatureBitmap": 1,
                    "RegionArea": "xx",
                    "RegionName": "xx"
                },
                "IP": "xx",
                "Http3Supported": 0,
                "InBanBlacklist": 0,
                "AccessRegion": "xx",
                "ProjectId": 0,
                "BillingType": 0,
                "SupportProtocols": [
                    "TCP",
                    "UDP",
                    "HTTP",
                    "HTTPS"
                ],
                "PackageType": "xx",
                "Domain": "xx",
                "IPAddressVersion": "xx",
                "BanStatus": "xx",
                "CreateTime": 1,
                "InstanceId": "xx",
                "Bandwidth": 10,
                "SupportSecurity": 0,
                "TagSet": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ClientIPMethod": [
                    0
                ],
                "ProxyName": "xx",
                "NetworkType": "xx",
                "ModifyConfigTime": 1,
                "GroupId": "xx"
            }
        ],
        "TotalCount": 1,
        "ProxySet": [
            {
                "AccessRegionInfo": {
                    "RegionId": "xx",
                    "RegionAreaName": "xx",
                    "IDCType": "xx",
                    "FeatureBitmap": 1,
                    "RegionArea": "xx",
                    "RegionName": "xx"
                },
                "RelatedGlobalDomains": [
                    "xx"
                ],
                "Version": "xx",
                "PolicyId": "xx",
                "Scalarable": 1,
                "IPList": [
                    {
                        "IP": "xx",
                        "Bandwidth": 0,
                        "Provider": "xx"
                    }
                ],
                "Status": "xx",
                "ProxyType": 1,
                "ForwardIP": "xx",
                "ProxyId": "xx",
                "RealServerRegion": "xx",
                "Concurrent": 2,
                "RealServerRegionInfo": {
                    "RegionId": "xx",
                    "RegionAreaName": "xx",
                    "IDCType": "xx",
                    "FeatureBitmap": 1,
                    "RegionArea": "xx",
                    "RegionName": "xx"
                },
                "IP": "xx",
                "Http3Supported": 0,
                "InBanBlacklist": 0,
                "AccessRegion": "xx",
                "ProjectId": 0,
                "BillingType": 0,
                "SupportProtocols": [
                    "TCP",
                    "UDP",
                    "HTTP",
                    "HTTPS"
                ],
                "PackageType": "xx",
                "Domain": "xx",
                "IPAddressVersion": "xx",
                "BanStatus": "xx",
                "CreateTime": 1,
                "InstanceId": "xx",
                "Bandwidth": 10,
                "SupportSecurity": 0,
                "TagSet": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ClientIPMethod": [
                    0
                ],
                "ProxyName": "xx",
                "NetworkType": "xx",
                "ModifyConfigTime": 1,
                "GroupId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

