**Example 1: 查询所有防护分区**



Input: 

```
tccli teo DescribeZoneDDoSPolicy --cli-unfold-argument  \
    --ZoneId zone-xxqr76cy
```

Output: 
```
{
    "Response": {
        "ShieldAreas": [
            {
                "TcpNum": 0,
                "EntityName": "xx",
                "ZoneId": "xx",
                "Application": [
                    {
                        "Status": "xx",
                        "AccelerateType": "xx",
                        "Host": "xx"
                    }
                ],
                "PolicyId": 0,
                "Entity": "xx",
                "Type": "xx",
                "UdpNum": 0
            }
        ],
        "Domains": [
            {
                "Status": "xx",
                "AccelerateType": "xx",
                "Host": "xx"
            }
        ],
        "RequestId": "xx",
        "AppId": 123456
    }
}
```

