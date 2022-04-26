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
                "UDP"
            ],
            "PackageType": "xx",
            "Domain": "xx",
            "IPAddressVersion": "xx",
            "BanStatus": "xx",
            "CreateTime": 1,
            "InstanceId": "xx",
            "Bandwidth": 10,
            "SupportSecurity": 1,
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
        },
        "RequestId": "xx"
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
        "RequestId": "fe6deb4c-3bf9-4b92-9bec-047d44d8d7c4",
        "ProxyDetail": {
            "InstanceId": "link-4m6fx36h",
            "ProxyId": "link-4m6fx36h",
            "CreateTime": 1646712299,
            "ProjectId": 0,
            "ProxyName": "test8",
            "ProxyType": 100,
            "AccessRegion": "Guangzhou",
            "RealServerRegion": "Shanghai",
            "Bandwidth": 10,
            "NetworkType": "normal",
            "Concurrent": 2,
            "Status": "RUNNING",
            "Domain": "link-4m6fx36h.gaapacc.com.cn",
            "IP": "1.14.225.21",
            "IPList": [
                {
                    "IP": "1.14.225.21",
                    "Provider": "BGP",
                    "Bandwidth": 10
                }
            ],
            "AccessRegionInfo": {
                "RegionId": "Guangzhou",
                "RegionName": "广州（原中国大陆-华南大区）",
                "RegionArea": "SouthChina",
                "RegionAreaName": "SouthChina",
                "IDCType": "dc",
                "FeatureBitmap": 79
            },
            "RealServerRegionInfo": {
                "RegionId": "Shanghai",
                "RegionName": "上海（原中国大陆-华东大区）",
                "RegionArea": "EastChina",
                "RegionAreaName": "EastChina",
                "IDCType": "dc",
                "FeatureBitmap": 79
            },
            "TagSet": [],
            "ModifyConfigTime": 1646712299,
            "IPAddressVersion": "IPv4",
            "PackageType": "Thunder",
            "BanStatus": "RECOVER",
            "Http3Supported": 0,
            "InBanBlacklist": 0,
            "ClientIPMethod": [
                0,
                1
            ],
            "GroupId": null,
            "PolicyId": "sp-nahrld9t",
            "Version": "3.0",
            "SupportProtocols": [
                "TCP",
                "UDP"
            ],
            "Scalarable": 1,
            "SupportSecurity": 1,
            "BillingType": 0,
            "RelatedGlobalDomains": [
                "gd-rv1p5ak9.gaapacc.com.cn"
            ],
            "ForwardIP": "124.222.196.15;124.221.127.42;"
        }
    }
}
```

