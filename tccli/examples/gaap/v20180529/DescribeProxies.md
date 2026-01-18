**Example 1: 查询通道实例列表**



Input: 

```
tccli gaap DescribeProxies --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AccessRegion": "Guangzhou",
                "AccessRegionInfo": {
                    "FeatureBitmap": 207,
                    "IDCType": "dc",
                    "RegionArea": "SouthChina",
                    "RegionAreaName": "SouthChina",
                    "RegionId": "Guangzhou",
                    "RegionName": "广州（原中国大陆-华南大区）",
                    "SupportFeature": null
                },
                "BanStatus": "RECOVER",
                "Bandwidth": 10,
                "BillingType": 2,
                "ClientIPMethod": [
                    0
                ],
                "Concurrent": 2,
                "CreateTime": 1768205817,
                "Domain": "",
                "FeatureBitmap": 71,
                "ForwardIP": "",
                "GroupId": "lg-joaaddy1",
                "Http3Supported": 1,
                "IP": "",
                "IPAddressVersion": "IPv4",
                "IPList": [],
                "InBanBlacklist": 0,
                "InstanceId": "link-kicu7m5b",
                "IsAutoScaleProxy": 0,
                "IsSupportTLSChoice": 1,
                "ModifyConfigTime": null,
                "NetworkType": "normal",
                "PackageType": "Thunder",
                "PolicyId": null,
                "ProjectId": 0,
                "ProxyId": "link-kicu7m5b",
                "ProxyName": "default",
                "ProxyType": 100,
                "RealServerRegion": "Shanghai",
                "RealServerRegionInfo": {
                    "FeatureBitmap": 207,
                    "IDCType": "dc",
                    "RegionArea": "EastChina",
                    "RegionAreaName": "EastChina",
                    "RegionId": "Shanghai",
                    "RegionName": "上海（原中国大陆-华东大区）",
                    "SupportFeature": null
                },
                "RelatedGlobalDomains": [],
                "Scalarable": 1,
                "Status": "CREATE_FAILED",
                "SupportProtocols": [
                    "TCP"
                ],
                "SupportSecurity": 1,
                "TagSet": [],
                "Version": "3.0"
            }
        ],
        "ProxySet": [
            {
                "AccessRegion": "Guangzhou",
                "AccessRegionInfo": {
                    "FeatureBitmap": 207,
                    "IDCType": "dc",
                    "RegionArea": "SouthChina",
                    "RegionAreaName": "SouthChina",
                    "RegionId": "Guangzhou",
                    "RegionName": "广州（原中国大陆-华南大区）",
                    "SupportFeature": null
                },
                "BanStatus": "RECOVER",
                "Bandwidth": 10,
                "BillingType": 2,
                "ClientIPMethod": [
                    0
                ],
                "Concurrent": 2,
                "CreateTime": 1768205817,
                "Domain": "",
                "FeatureBitmap": 71,
                "ForwardIP": "",
                "GroupId": "lg-joaaddy1",
                "Http3Supported": 1,
                "IP": "",
                "IPAddressVersion": "IPv4",
                "IPList": [],
                "InBanBlacklist": 0,
                "InstanceId": "link-kicu7m5b",
                "IsAutoScaleProxy": 0,
                "IsSupportTLSChoice": 1,
                "ModifyConfigTime": null,
                "NetworkType": "normal",
                "PackageType": "Thunder",
                "PolicyId": null,
                "ProjectId": 0,
                "ProxyId": "link-kicu7m5b",
                "ProxyName": "default",
                "ProxyType": 100,
                "RealServerRegion": "Shanghai",
                "RealServerRegionInfo": {
                    "FeatureBitmap": 207,
                    "IDCType": "dc",
                    "RegionArea": "EastChina",
                    "RegionAreaName": "EastChina",
                    "RegionId": "Shanghai",
                    "RegionName": "上海（原中国大陆-华东大区）",
                    "SupportFeature": null
                },
                "RelatedGlobalDomains": [],
                "Scalarable": 1,
                "Status": "CREATE_FAILED",
                "SupportProtocols": [
                    "TCP"
                ],
                "SupportSecurity": 1,
                "TagSet": [],
                "Version": "3.0"
            }
        ],
        "TotalCount": 32,
        "RequestId": "c8bb6c5b-a425-4ace-a22c-c488d06811ba"
    }
}
```

