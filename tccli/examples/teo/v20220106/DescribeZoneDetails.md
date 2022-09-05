**Example 1: 查询某个站点的详细信息**



Input: 

```
tccli teo DescribeZoneDetails --cli-unfold-argument  \
    --Id zone-27q0p0bali16
```

Output: 
```
{
    "Response": {
        "Id": "zone-27q0p0bali16",
        "Name": "example.com",
        "Status": "active",
        "ModifiedOn": "2020-09-22T00:00:00+00:00",
        "Tags": [
            {
                "TagKey": "test",
                "TagValue": "test"
            }
        ],
        "NameServers": [
            "ns1.teodns.com",
            "ns2.teodns.com"
        ],
        "VanityNameServers": {
            "Switch": "on",
            "Servers": [
                "ns1.example.com",
                "ns2.example.com"
            ]
        },
        "CreatedOn": "2020-09-22T00:00:00+00:00",
        "OriginalNameServers": [
            "ns1.example.com",
            "ns2.example.com"
        ],
        "Paused": true,
        "CnameSpeedUp": "enabled",
        "Resources": [
            {
                "EnableTime": "2020-09-22T00:00:00+00:00",
                "Status": "normal",
                "ExpireTime": "2020-09-22T00:00:00+00:00",
                "PlanId": "edgeone-27q0p0bali15",
                "Sv": [
                    {
                        "Value": "12",
                        "Key": "sv_a"
                    }
                ],
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "PayMode": 0,
                "AutoRenewFlag": 0,
                "Id": "edgeone-27q0p0bali18"
            }
        ],
        "RequestId": "9cc50b24-7dc5-44f4-96ce-95825d53ff2f",
        "Type": "full",
        "VanityNameServersIps": [
            {
                "Name": "ns1.example.com",
                "IPv4": "1.1.1.1"
            }
        ],
        "CnameStatus": "finished",
        "Area": "global"
    }
}
```

