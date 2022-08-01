**Example 1: 获取解析记录列表**



Input: 

```
tccli privatedns DescribePrivateZoneRecordList --cli-unfold-argument  \
    --ZoneId zone-123456 \
    --Limit 2 \
    --Offset 0 \
    --Filters.0.Name Value \
    --Filters.0.Values 3 b \
    --Filters.1.Name RecordType \
    --Filters.1.Values A AAAA
```

Output: 
```
{
    "Response": {
        "RequestId": "8a4ea9cc-b1df-f8f8-ffe7efbe98f9ff85",
        "TotalCount": 5,
        "RecordSet": [
            {
                "RecordId": "66",
                "ZoneId": "zone-123456",
                "SubDomain": "b",
                "RecordType": "A",
                "RecordValue": "3.3.3.3",
                "TTL": 600,
                "MX": 0,
                "Status": "enabled",
                "Extra": "weight:100",
                "CreatedOn": "2020-11-16 17:16:24",
                "UpdatedOn": "2020-11-16 17:16:24",
                "Weight": 100,
                "Enabled": 0
            },
            {
                "RecordId": "65",
                "ZoneId": "zone-123456",
                "SubDomain": "mail",
                "RecordType": "MX",
                "RecordValue": "5.5.5.5",
                "TTL": 600,
                "MX": 10,
                "Status": "enabled",
                "Extra": null,
                "CreatedOn": "2020-11-16 17:14:02",
                "UpdatedOn": "2020-11-16 17:14:02",
                "Weight": null,
                "Enabled": 0
            }
        ]
    }
}
```

