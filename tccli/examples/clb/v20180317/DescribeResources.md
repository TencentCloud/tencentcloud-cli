**Example 1: 查询用户在当前地域支持可用区列表和资源列表**

查询用户在当前地域支持可用区列表和资源列表

Input: 

```
tccli clb DescribeResources --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "ZoneResourceSet": [
            {
                "LocalZone": false,
                "EdgeZone": false,
                "SlaveZone": null,
                "MasterZone": "ap-guangzhou-1",
                "IPVersion": "IPv4",
                "ZoneRegion": "ap-guangzhou",
                "ResourceSet": [
                    {
                        "Isp": "BGP",
                        "Type": [
                            "BGP"
                        ]
                    },
                    {
                        "Isp": "CMCC",
                        "Type": [
                            "CMCC"
                        ]
                    }
                ],
                "ZoneResourceType": "SHARED"
            }
        ],
        "RequestId": "d09b91ba-a81e-4ca3-b423-c64e60127c64"
    }
}
```

