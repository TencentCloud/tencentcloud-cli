**Example 1: 查询用户在当前地域支持可用区列表和资源列表**



Input: 

```
tccli clb DescribeResources --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "ZoneResourceSet": [
            {
                "LocalZone": false,
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
                ]
            }
        ],
        "RequestId": "d09b91ba-a81e-4ca3-b423-c64e60127c64"
    }
}
```

