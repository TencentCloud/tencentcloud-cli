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
                    "RegionId": "EastChina",
                    "RegionName": "中国大陆-华东"
                },
                "RelatedGlobalDomains": [
                    "xx"
                ],
                "Version": "3.0",
                "PolicyId": null,
                "Scalarable": 1,
                "Status": "RUNNING",
                "ProxyType": 1,
                "ForwardIP": "1.1.1.1",
                "ProxyId": "link-12345678",
                "RealServerRegion": "NorthChina",
                "Concurrent": 2,
                "RealServerRegionInfo": {
                    "RegionId": "NorthChina",
                    "RegionName": "中国大陆-华北"
                },
                "IP": "1.1.1.2",
                "AccessRegion": "EastChina",
                "ProjectId": 0,
                "BillingType": 0,
                "SupportProtocols": [
                    "TCP",
                    "UDP",
                    "HTTP",
                    "HTTPS"
                ],
                "Domain": "link-12345678.gaapqcloud.com",
                "IPAddressVersion": "IPv4",
                "CreateTime": 1,
                "InstanceId": "link-12345678",
                "Bandwidth": 10,
                "SupportSecurity": 0,
                "TagSet": [
                    {
                        "TagKey": "gaaptest",
                        "TagValue": "www"
                    }
                ],
                "ClientIPMethod": [
                    0
                ],
                "ProxyName": "test",
                "NetworkType": "xx",
                "ModifyConfigTime": 1,
                "GroupId": null
            }
        ],
        "TotalCount": 1,
        "ProxySet": [
            {
                "AccessRegionInfo": {
                    "RegionId": "EastChina",
                    "RegionName": "中国大陆-华东"
                },
                "RelatedGlobalDomains": [
                    "xx"
                ],
                "Version": "3.0",
                "PolicyId": null,
                "Scalarable": 1,
                "Status": "RUNNING",
                "ProxyType": 1,
                "ForwardIP": "1.1.1.1",
                "ProxyId": "link-12345678",
                "RealServerRegion": "NorthChina",
                "Concurrent": 2,
                "RealServerRegionInfo": {
                    "RegionId": "NorthChina",
                    "RegionName": "中国大陆-华北"
                },
                "IP": "1.1.1.2",
                "AccessRegion": "EastChina",
                "ProjectId": 0,
                "BillingType": 0,
                "SupportProtocols": [
                    "TCP",
                    "UDP",
                    "HTTP",
                    "HTTPS"
                ],
                "Domain": "link-12345678.gaapqcloud.com",
                "IPAddressVersion": "IPv4",
                "CreateTime": 1,
                "InstanceId": "link-12345678",
                "Bandwidth": 10,
                "SupportSecurity": 0,
                "TagSet": [
                    {
                        "TagKey": "gaaptest",
                        "TagValue": "www"
                    }
                ],
                "ClientIPMethod": [
                    0
                ],
                "ProxyName": "test",
                "NetworkType": "",
                "ModifyConfigTime": 1,
                "GroupId": null
            }
        ],
        "RequestId": "1c54137e-e4da-42e1-8565-1bc2d99794a3"
    }
}
```

