**Example 1: 查询通道详情**



Input: 

```
tccli gaap DescribeProxyDetail --cli-unfold-argument  \
    --ProxyId link-12345678
```

Output: 
```
{
    "Response": {
        "ProxyDetail": {
            "InstanceId": "abc",
            "CreateTime": 1,
            "ProjectId": 0,
            "ProxyName": "abc",
            "AccessRegion": "abc",
            "RealServerRegion": "abc",
            "Bandwidth": 0,
            "Concurrent": 0,
            "Status": "abc",
            "Domain": "abc",
            "IP": "abc",
            "Version": "abc",
            "ProxyId": "abc",
            "Scalarable": 0,
            "SupportProtocols": [
                "abc"
            ],
            "GroupId": "abc",
            "PolicyId": "abc",
            "AccessRegionInfo": {
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
            "ForwardIP": "abc",
            "TagSet": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "SupportSecurity": 0,
            "BillingType": 0,
            "RelatedGlobalDomains": [
                "abc"
            ],
            "ModifyConfigTime": 1,
            "ProxyType": 1,
            "ClientIPMethod": [
                0
            ],
            "IPAddressVersion": "abc",
            "NetworkType": "abc",
            "PackageType": "abc",
            "BanStatus": "abc",
            "IPList": [
                {
                    "IP": "abc",
                    "Provider": "abc",
                    "Bandwidth": 0
                }
            ],
            "Http3Supported": 0,
            "InBanBlacklist": 0,
            "FeatureBitmap": 0,
            "IsAutoScaleProxy": 0,
            "IsSupportTLSChoice": 0
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 查询通道详情2**



Input: 

```
tccli gaap DescribeProxyDetail --cli-unfold-argument  \
    --ProxyId link-4m6fx36h
```

Output: 
```
{
    "Response": {
        "ProxyDetail": {
            "InstanceId": "abc",
            "CreateTime": 1,
            "ProjectId": 0,
            "ProxyName": "abc",
            "AccessRegion": "abc",
            "RealServerRegion": "abc",
            "Bandwidth": 0,
            "Concurrent": 0,
            "Status": "abc",
            "Domain": "abc",
            "IP": "abc",
            "Version": "abc",
            "ProxyId": "abc",
            "Scalarable": 0,
            "SupportProtocols": [
                "abc"
            ],
            "GroupId": "abc",
            "PolicyId": "abc",
            "AccessRegionInfo": {
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
            "ForwardIP": "abc",
            "TagSet": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "SupportSecurity": 0,
            "BillingType": 0,
            "RelatedGlobalDomains": [
                "abc"
            ],
            "ModifyConfigTime": 1,
            "ProxyType": 1,
            "ClientIPMethod": [
                0
            ],
            "IPAddressVersion": "abc",
            "NetworkType": "abc",
            "PackageType": "abc",
            "BanStatus": "abc",
            "IPList": [
                {
                    "IP": "abc",
                    "Provider": "abc",
                    "Bandwidth": 0
                }
            ],
            "Http3Supported": 0,
            "InBanBlacklist": 0,
            "FeatureBitmap": 0,
            "IsAutoScaleProxy": 0,
            "IsSupportTLSChoice": 0
        },
        "RequestId": "abc"
    }
}
```

