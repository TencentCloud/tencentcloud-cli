**Example 1: dns_records**



Input: 

```
tccli teo DescribeDnsRecords --cli-unfold-argument  \
    --Direction desc \
    --ZoneId zone-20hyebgyfsko \
    --Limit 0 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values record-3d5dg39c \
    --Filters.0.Name record-id \
    --Offset 0 \
    --Order created_on \
    --Match all
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "DnsRecords": [
            {
                "Status": "active",
                "Priority": 0,
                "ModifiedOn": "2020-09-22T00:00:00+00:00",
                "DnsRecordName": "test.example.com",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "ZoneId": "zone-20hyebgyfsko",
                "Content": "110.242.68.66",
                "Cname": "test.example.com.cdn.acc.xyz",
                "Mode": "dns_only",
                "TTL": 0,
                "Locked": true,
                "DnsRecordType": "A",
                "DnsRecordId": "record-3d5dg39c",
                "ZoneName": "example.com",
                "DomainStatus": [
                    "lb"
                ]
            }
        ]
    }
}
```

