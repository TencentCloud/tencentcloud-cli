**Example 1: Querying connection instance list**



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
                "Status": "CREATING",
                "Domain": "",
                "InstanceId": "link-01vm81tj",
                "AccessRegion": "EastChina",
                "ProxyId": "link-01vm81tj",
                "ProjectId": 0,
                "AccessRegionInfo": {
                    "RegionId": "EastChina",
                    "RegionName": "Mainland China - East China"
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
                "TagSet": [],
                "GroupId": null,
                "RealServerRegionInfo": {
                    "RegionId": "NorthChina",
                    "RegionName": "Mainland China - North China"
                }
            }
        ],
        "ProxySet": [
            {
                "Status": "CREATING",
                "Domain": "",
                "InstanceId": "link-01vm81tj",
                "AccessRegion": "EastChina",
                "ProxyId": "link-01vm81tj",
                "ProjectId": 0,
                "AccessRegionInfo": {
                    "RegionId": "EastChina",
                    "RegionName": "Mainland China - East China"
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
                    "RegionName": "Mainland China - North China"
                },
                "TagSet": [
                    {
                        "TagKey": "gaaptest",
                        "TagValue": "www"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "1c54137e-e4da-42e1-8565-1bc2d99794a3"
    }
}
```

