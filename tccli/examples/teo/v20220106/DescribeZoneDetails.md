**Example 1: 查询某个站点的详细信息**



Input: 

```
tccli teo DescribeZoneDetails --cli-unfold-argument  \
    --Id xx
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "ModifiedOn": "2020-09-22T00:00:00+00:00",
        "Name": "xx",
        "Tags": [
            {
                "TagKey": "xx",
                "TagValue": "xx"
            }
        ],
        "NameServers": [
            "xx"
        ],
        "VanityNameServers": {
            "Switch": "xx",
            "Servers": [
                "xx"
            ]
        },
        "CreatedOn": "2020-09-22T00:00:00+00:00",
        "OriginalNameServers": [
            "xx"
        ],
        "Paused": true,
        "CnameSpeedUp": "xx",
        "RequestId": "xx",
        "Type": "xx",
        "Id": "xx",
        "VanityNameServersIps": [
            {
                "Name": "xx",
                "IPv4": "xx"
            }
        ],
        "CnameStatus": "xx"
    }
}
```

