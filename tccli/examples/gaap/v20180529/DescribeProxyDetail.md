**Example 1: 查询通道详情**



Input: 

```
tccli gaap DescribeProxyDetail --cli-unfold-argument  \
    --ProxyId link-4qlu8i3j
```

Output: 
```
{
    "Response": {
        "ProxyDetail": {
            "InstanceId": "link-4qlu8i3j",
            "CreateTime": 1728542120,
            "ProjectId": 1323575,
            "ProxyName": "test-proxy",
            "AccessRegion": "Beijing",
            "RealServerRegion": "Shanghai",
            "Bandwidth": 10,
            "Concurrent": 2,
            "Status": "RUNNING",
            "Domain": "link-4qlu8i3j.gaapqcloud.com.cn",
            "IP": "43.137.75.190",
            "Version": "3.0",
            "ProxyId": "link-4qlu8i3j",
            "Scalarable": 1,
            "SupportProtocols": [
                "TCP",
                "UDP"
            ],
            "GroupId": null,
            "PolicyId": "sp-e6on5s9d",
            "AccessRegionInfo": {
                "RegionId": "Beijing",
                "RegionName": "北京（原中国大陆-华北大区）",
                "RegionArea": "NorthChina",
                "RegionAreaName": "NorthChina",
                "IDCType": "dc",
                "FeatureBitmap": 79,
                "SupportFeature": null
            },
            "RealServerRegionInfo": {
                "RegionId": "Shanghai",
                "RegionName": "上海（原中国大陆-华东大区）",
                "RegionArea": "EastChina",
                "RegionAreaName": "EastChina",
                "IDCType": "dc",
                "FeatureBitmap": 79,
                "SupportFeature": null
            },
            "ForwardIP": "124.222.42.242;118.25.142.34;",
            "TagSet": [
                {
                    "TagKey": "test",
                    "TagValue": "10"
                }
            ],
            "SupportSecurity": 1,
            "BillingType": 1,
            "RelatedGlobalDomains": [],
            "ModifyConfigTime": 1728542120,
            "ProxyType": 100,
            "ClientIPMethod": [
                0,
                1
            ],
            "IPAddressVersion": "IPv4",
            "NetworkType": "normal",
            "PackageType": "Thunder",
            "BanStatus": "RECOVER",
            "IPList": [
                {
                    "IP": "43.137.75.190",
                    "Provider": "BGP",
                    "Bandwidth": 10
                }
            ],
            "Http3Supported": 1,
            "InBanBlacklist": 0,
            "FeatureBitmap": 71,
            "IsAutoScaleProxy": 0,
            "IsSupportTLSChoice": 1
        },
        "RequestId": "8d5cae87-74ac-4122-98e8-3aab1f7040b9"
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

