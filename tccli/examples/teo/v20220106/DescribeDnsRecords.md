**Example 1: dns_records**



Input: 

```
tccli teo DescribeDnsRecords --cli-unfold-argument  \
    --Direction xx \
    --ZoneId xx \
    --Limit 0 \
    --Filters.0.Fuzzy True \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 0 \
    --Order xx \
    --Match xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "Records": [
            {
                "Status": "xx",
                "Priority": 0,
                "ModifiedOn": "2020-09-22T00:00:00+00:00",
                "Name": "xx",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "ZoneId": "xx",
                "Content": "xx",
                "Cname": "xx",
                "Mode": "xx",
                "Ttl": 0,
                "Locked": true,
                "Type": "xx",
                "Id": "xx",
                "ZoneName": "xx"
            }
        ]
    }
}
```

