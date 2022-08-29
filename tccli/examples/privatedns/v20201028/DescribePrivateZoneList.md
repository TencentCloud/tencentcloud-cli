**Example 1: 获取私有域列表**



Input: 

```
tccli privatedns DescribePrivateZoneList --cli-unfold-argument  \
    --Limit 200 \
    --Offset 0 \
    --Filters.0.Name ZoneId \
    --Filters.0.Values zone-xxxx \
    --Filters.1.Name Domain \
    --Filters.1.Values a.com \
    --Filters.2.Name Remark \
    --Filters.2.Values aaaaaaaa \
    --Filters.3.Name Vpc \
    --Filters.3.Values vpc-16bc7l43 \
    --Filters.4.Name Tag \
    --Filters.4.Values tak_key:tag_value
```

Output: 
```
{
    "Response": {
        "RequestId": "8a4ea9cc-b1df-f8f8-ffe7efbe98f9ff85",
        "TotalCount": 5,
        "PrivateZoneSet": [
            {
                "ZoneId": "zone-123456",
                "OwnerUin": 11111111111111,
                "Domain": "a.com",
                "CreatedOn": "2020-05-28 16:28:10",
                "UpdatedOn": "2020-07-16 02:52:29",
                "RecordCount": 6,
                "Remark": null,
                "VpcSet": [
                    {
                        "Region": "xx",
                        "UniqVpcId": "xx"
                    }
                ],
                "AccountVpcSet": [
                    {
                        "UniqVpcId": "vpc-q1111115",
                        "Region": "ap-guangzhou",
                        "Uin": "123456789"
                    }
                ],
                "Status": "ENABLED",
                "DnsForwardStatus": "DISABLED",
                "Tags": [],
                "IsCustomTld": false,
                "CnameSpeedupStatus": "DISABLED"
            },
            {
                "ZoneId": "zone-123456",
                "OwnerUin": 1111111111111,
                "Domain": "a.com",
                "CreatedOn": "2020-07-09 19:15:21",
                "UpdatedOn": "2020-07-09 19:15:21",
                "RecordCount": 0,
                "Remark": null,
                "VpcSet": [],
                "AccountVpcSet": [],
                "Status": "ENABLED",
                "DnsForwardStatus": "DISABLED",
                "Tags": [
                    {
                        "TagKey": "tagKey",
                        "TagValue": "tagValue"
                    }
                ],
                "IsCustomTld": true,
                "CnameSpeedupStatus": "DISABLED"
            }
        ]
    }
}
```

