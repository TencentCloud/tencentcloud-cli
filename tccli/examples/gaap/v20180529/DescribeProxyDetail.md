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
                "RegionId": "SoutheastAsia",
                "RegionName": "新加坡"
            },
            "RelatedGlobalDomains": [],
            "Version": "3.0",
            "PolicyId": "",
            "Scalarable": 1,
            "Status": "RUNNING",
            "ProxyType": 100,
            "ForwardIP": "154.8.156.36;140.143.138.143;",
            "InstanceId": "link-ibqy8dqv",
            "RealServerRegion": "NorthChina",
            "Concurrent": 2,
            "RealServerRegionInfo": {
                "RegionId": "NorthChina",
                "RegionName": "中国大陆-华北大区"
            },
            "IP": "129.226.3.36",
            "AccessRegion": "SoutheastAsia",
            "ProjectId": 0,
            "BillingType": 0,
            "SupportProtocols": [
                "TCP",
                "UDP"
            ],
            "Domain": "link-ibqy8dqv.gaapqcloud.com",
            "CreateTime": 1598417633,
            "ProxyId": "link-ibqy8dqv",
            "Bandwidth": 10,
            "SupportSecurity": 1,
            "TagSet": [],
            "ProxyName": "p_weidzhao_test",
            "NetworkType": "",
            "ModifyConfigTime": 1598417633,
            "GroupId": "",
            "ClientIPMethod": 1,
            "IPAddressVersion": "IPv4"
        },
        "RequestId": "2a3ba5c4-aa37-4f01-825a-04140b4b25da"
    }
}
```

