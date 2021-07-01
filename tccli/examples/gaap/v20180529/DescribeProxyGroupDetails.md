**Example 1: 查询通道组详情**



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
            "ClientIPMethod": [
                0
            ],
            "ProxyNum": 0,
            "ProjectId": 0,
            "OwnerUin": "2186969362",
            "GroupId": "lg-mh4k07v5",
            "GroupName": "t4",
            "Version": "1.0",
            "PolicyId": "vdsw",
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
            "DnsDefaultIp": "",
            "IPAddressVersion": "IPv6"
        }
    }
}
```

