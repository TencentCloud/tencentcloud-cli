**Example 1: 查询通道实例列表**



Input: 

```
tccli gaap DescribeProxies --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AccessRegionInfo": {
                    "RegionId": "Beijing",
                    "RegionAreaName": "NorthChina",
                    "IDCType": "dc",
                    "FeatureBitmap": 79,
                    "RegionArea": "Beijing",
                    "RegionName": "北京（原中国大陆-华北大区）",
                    "SupportFeature": null
                },
                "RelatedGlobalDomains": [],
                "Version": "3.0",
                "PolicyId": null,
                "Scalarable": 1,
                "IPList": [
                    {
                        "IP": "43.137.75.190",
                        "Provider": "BGP",
                        "Bandwidth": 10
                    }
                ],
                "Status": "RUNNING",
                "ProxyType": 100,
                "ForwardIP": "124.222.42.242;118.25.142.34;",
                "ProxyId": "link-4qlu8i3j",
                "RealServerRegion": "Shanghai",
                "Concurrent": 2,
                "RealServerRegionInfo": {
                    "RegionId": "Shanghai",
                    "RegionAreaName": "上海（原中国大陆-华东大区）",
                    "IDCType": "dc",
                    "FeatureBitmap": 79,
                    "RegionArea": "EastChina",
                    "RegionName": "EastChina",
                    "SupportFeature": null
                },
                "IP": "43.137.75.190",
                "Http3Supported": 0,
                "InBanBlacklist": 0,
                "AccessRegion": "Beijing",
                "ProjectId": 1323575,
                "BillingType": 1,
                "SupportProtocols": [
                    "TCP",
                    "UDP"
                ],
                "PackageType": "Thunder",
                "FeatureBitmap": 71,
                "Domain": "link-4qlu8i3j.gaapqcloud.com.c",
                "IPAddressVersion": "IPv4",
                "BanStatus": "RECOVER",
                "CreateTime": 1728542120,
                "InstanceId": "link-4qlu8i3j",
                "Bandwidth": 10,
                "SupportSecurity": 1,
                "TagSet": [
                    {
                        "TagKey": "test-01",
                        "TagValue": "10"
                    }
                ],
                "ClientIPMethod": [
                    0,
                    1
                ],
                "ProxyName": "test-proxy",
                "NetworkType": "normal",
                "ModifyConfigTime": 1728542120,
                "GroupId": null
            }
        ],
        "TotalCount": 1,
        "ProxySet": [
            {
                "AccessRegionInfo": {
                    "RegionId": "Beijing",
                    "RegionAreaName": "NorthChina",
                    "IDCType": "dc",
                    "FeatureBitmap": 79,
                    "RegionArea": "Beijing",
                    "RegionName": "北京（原中国大陆-华北大区）",
                    "SupportFeature": null
                },
                "RelatedGlobalDomains": [],
                "Version": "3.0",
                "PolicyId": null,
                "Scalarable": 1,
                "IPList": [
                    {
                        "IP": "43.137.75.190",
                        "Provider": "BGP",
                        "Bandwidth": 10
                    }
                ],
                "Status": "RUNNING",
                "ProxyType": 100,
                "ForwardIP": "124.222.42.242;118.25.142.34;",
                "ProxyId": "link-4qlu8i3j",
                "RealServerRegion": "Shanghai",
                "Concurrent": 2,
                "RealServerRegionInfo": {
                    "RegionId": "Shanghai",
                    "RegionAreaName": "上海（原中国大陆-华东大区）",
                    "IDCType": "dc",
                    "FeatureBitmap": 79,
                    "RegionArea": "EastChina",
                    "RegionName": "EastChina",
                    "SupportFeature": null
                },
                "IP": "43.137.75.190",
                "Http3Supported": 0,
                "InBanBlacklist": 0,
                "AccessRegion": "Beijing",
                "ProjectId": 1323575,
                "BillingType": 1,
                "SupportProtocols": [
                    "TCP",
                    "UDP",
                    "HTTP",
                    "HTTPS"
                ],
                "PackageType": "Thunder",
                "FeatureBitmap": 71,
                "Domain": "link-4qlu8i3j.gaapqcloud.com.c",
                "IPAddressVersion": "IPv4",
                "BanStatus": "RECOVER",
                "CreateTime": 1728542120,
                "InstanceId": "link-4qlu8i3j",
                "Bandwidth": 10,
                "SupportSecurity": 1,
                "TagSet": [
                    {
                        "TagKey": "test-01",
                        "TagValue": "10"
                    }
                ],
                "ClientIPMethod": [
                    0,
                    1
                ],
                "ProxyName": "test-proxy",
                "NetworkType": "normal",
                "ModifyConfigTime": 1728542120,
                "GroupId": null
            }
        ],
        "RequestId": "bf46572b-700d-4797-831c-7fcf8232358d"
    }
}
```

