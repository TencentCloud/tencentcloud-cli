**Example 1: 查询用户站点信息列表**



Input: 

```
tccli teo DescribeZones --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Zones": [
            {
                "Id": "zone-27q0p0bali16",
                "Name": "example.com",
                "OriginalNameServers": [
                    "ns1.example.com.",
                    "ns2.example.com."
                ],
                "NameServers": [
                    "ns1.teodns.com.",
                    "ns2.teodns.com."
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
                "CreatedOn": "2020-09-22T00:00:00+00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fd9d86df-b7e8-4469-b928-18cb7fd1d341"
    }
}
```

