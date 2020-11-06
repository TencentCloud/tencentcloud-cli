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
            "Status": "CREATING",
            "Domain": "",
            "InstanceId": "link-01vm81tj",
            "AccessRegion": "EastChina",
            "ProxyId": "link-01vm81tj",
            "ProjectId": 0,
            "AccessRegionInfo": {
                "RegionId": "EastChina",
                "RegionName": "中国大陆-华东"
            },
            "RealServerRegion": "NorthChina",
            "CreateTime": "2019-03-21 21:33:45",
            "SupportProtocols": [
                "TCP",
                "UDP",
                "HTTP",
                "HTTPS"
            ],
            "Concurrent": 2,
            "Bandwidth": 10,
            "Version": "2.0",
            "PolicyId": null,
            "Scalarable": 1,
            "IP": "",
            "ProxyName": "fff",
            "GroupId": null,
            "RealServerRegionInfo": {
                "RegionId": "NorthChina",
                "RegionName": "中国大陆-华北"
            },
            "TagSet": [
                {
                    "TagKey": "gaaptest",
                    "TagValue": "www"
                }
            ]
        },
        "RequestId": "1c54137e-e4da-42e1-8565-1bc2d99794a3"
    }
}
```

