**Example 1: 查询用户站点信息列表**



Input: 

```
tccli teo DescribeZones --cli-unfold-argument  \
    --Limit 20 \
    --Filters.0.Fuzzy False \
    --Filters.0.Values example.com \
    --Filters.0.Name zone-name \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Zones": [
            {
                "ZoneId": "zone-27q0p0bali16",
                "ZoneName": "example.com",
                "OriginalNameServers": [
                    "ns1.example.com.",
                    "ns2.example.com."
                ],
                "NameServers": [
                    "ns1.teodns.com.",
                    "ns2.teodns.com."
                ],
                "VanityNameServers": {
                    "Switch": "on",
                    "Servers": [
                        "ns1.example.com",
                        "ns2.example.com"
                    ]
                },
                "VanityNameServersIps": [
                    {
                        "Name": "ns1.example.com",
                        "IPv4": "1.1.1.1"
                    }
                ],
                "Status": "active",
                "Type": "full",
                "Paused": false,
                "CnameSpeedUp": "enabled",
                "CnameStatus": "finished",
                "Tags": [
                    {
                        "TagKey": "test",
                        "TagValue": "example"
                    }
                ],
                "Resources": [],
                "ModifiedOn": "2020-09-22T00:00:00+00:00",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "Area": "mainland",
                "ActiveStatus": "active"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fd9d86df-b7e8-4469-b928-18cb7fd1d341"
    }
}
```

