**Example 1: 查询通道组详情**



Input: 

```
tccli gaap DescribeProxyGroupDetails --cli-unfold-argument  \
    --GroupId lg-123456
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
            "OwnerUin": "12345678",
            "CreateUin": "12345678",
            "GroupName": "grup-name",
            "DnsDefaultIp": "127.0.0.1",
            "Domain": "www.domain.com",
            "PolicyId": "gsp-123456",
            "RealServerRegionInfo": {
                "RegionId": "Beijing",
                "RegionName": "BEIJING",
                "RegionArea": "NorthChina",
                "RegionAreaName": "NorthChina",
                "IDCType": "dc",
                "FeatureBitmap": 1,
                "SupportFeature": {
                    "NetworkType": [
                        "normal"
                    ]
                }
            },
            "IsOldGroup": true,
            "GroupId": "lg-123456",
            "TagSet": [
                {
                    "TagKey": "tag_key",
                    "TagValue": "tag_value"
                }
            ],
            "Version": "3.0",
            "ClientIPMethod": [
                0
            ],
            "IPAddressVersion": "IPv4",
            "PackageType": "BGP",
            "Http3Supported": 0,
            "FeatureBitmap": 0,
            "IsSupportTLSChoice": 1
        },
        "RequestId": "bf46572b-700d-4797-831c-7fcf8232358a"
    }
}
```

