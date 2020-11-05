**Example 1: Querying the Connection Group Details**



Input: 

```
tccli gaap DescribeProxyGroupDetails --cli-unfold-argument  \
    --GroupId lg
```

Output: 
```
{
    "Response": {
        "RequestId": "300371ff-12fd-4d9e-983d-c429f875dfb5",
        "ProxyGroupDetail": {
            "Status": 0,
            "Domain": null,
            "ProxyNum": 0,
            "ProjectId": 0,
            "OwnerUin": "2186969362",
            "GroupId": "lg-mh4k07v5",
            "GroupName": "t4",
            "RealServerRegionInfo": {
                "RegionId": "EastChina",
                "RegionName": "EastChina"
            },
            "TagSet": [
                {
                    "TagKey": "123",
                    "TagValue": "abc"
                }
            ],
            "IsOldGroup": false,
            "CreateUin": "2202003302",
            "CreateTime": 1552978237,
            "DnsDefaultIp": ""
        }
    }
}
```

