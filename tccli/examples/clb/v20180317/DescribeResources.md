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
        "ZoneResourceSet": [
            {
                "MasterZone": "ap-guangzhou",
                "SlaveZone": null,
                "IPVersion": "IPv6",
                "ResourceSet": [
                    {
                        "Isp": "BGP",
                        "Type": [
                            "BGP"
                        ],
                        "TypeSet": [],
                        "AvailabilitySet": []
                    }
                ],
                "ZoneRegion": "ap-guangzhou",
                "LocalZone": false,
                "EdgeZone": false,
                "ZoneResourceType": "SHARED",
                "Egress": "center_egress1"
            },
            {
                "MasterZone": "ap-guangzhou",
                "SlaveZone": null,
                "IPVersion": "IPv6_Nat",
                "ResourceSet": [
                    {
                        "Isp": "BGP",
                        "Type": [
                            "BGP"
                        ],
                        "TypeSet": [],
                        "AvailabilitySet": []
                    }
                ],
                "ZoneRegion": "ap-guangzhou",
                "LocalZone": false,
                "EdgeZone": false,
                "ZoneResourceType": "SHARED",
                "Egress": "center_egress1"
            },
            {
                "MasterZone": "ap-guangzhou-2",
                "SlaveZone": null,
                "IPVersion": "IPv4",
                "ResourceSet": [
                    {
                        "Isp": "BGP",
                        "Type": [
                            "BGP"
                        ],
                        "TypeSet": [],
                        "AvailabilitySet": []
                    },
                    {
                        "Isp": "INTERNAL",
                        "Type": [
                            "INTERNAL"
                        ],
                        "TypeSet": [],
                        "AvailabilitySet": []
                    }
                ],
                "ZoneRegion": "ap-guangzhou",
                "LocalZone": false,
                "EdgeZone": false,
                "ZoneResourceType": "SHARED",
                "Egress": "center_egress1"
            }
        ],
        "TotalCount": 3,
        "RequestId": "e0d11bcf-c3fa-45b8-b438-a4b642dbaad6"
    }
}
```

