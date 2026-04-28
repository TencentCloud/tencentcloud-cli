**Example 1: 按照公网IP查询封堵列表**

查询封堵解封列表。

Input: 

```
tccli antiddos DescribeDDoSBlockRecords --cli-unfold-argument  \
    --StartTime 2026-04-05T11:30:00+08:00 \
    --EndTime 2026-04-21T11:15:00+08:00 \
    --Filters.0.Name Resource \
    --Filters.0.Values 43.136.33.201 \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BlockRecords": [
            {
                "BlockTime": "2026-04-21T10:53:00+08:00",
                "Resource": "43.136.33.201",
                "Status": "Blocked"
            }
        ],
        "TotalCount": 4,
        "UnblockQuotaInfo": {
            "QuotaEndTime": "2026-04-22T00:00:00+08:00",
            "QuotaStartTime": "2026-04-21T00:00:00+08:00",
            "TotalQuota": 3,
            "UsedQuota": 3
        },
        "RequestId": "b450f3fd-6f30-4e2d-84d6-35e5c0afd25d"
    }
}
```

