**Example 1: 通过账号下任意指定站点查询源站防护控制域**

可任意选择一个账户下的站点来查询源站防护各种不同控制域的 IP 网段信息。

Input: 

```
tccli teo DescribeAvailableOriginACLFamily --cli-unfold-argument  \
    --ZoneId zone-2w0bpv1wlag8 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "OriginACLFamilyInfos": [
            {
                "ActiveTime": "2025-08-15T00:00:00+08:00",
                "EntireAddresses": {
                    "IPv4": [
                        "113.13.111.0/24"
                    ],
                    "IPv6": [
                        "240d:c010:c2:3::/64"
                    ]
                },
                "OriginACLFamily": "emc",
                "Version": "emc-0.0.2-20250814"
            }
        ],
        "TotalCount": 4,
        "RequestId": "ddc1548a-a1d3-464d-a4d8-377ef6b5ed1f"
    }
}
```

