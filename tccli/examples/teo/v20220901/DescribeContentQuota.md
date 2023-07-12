**Example 1: 查询配额**



Input: 

```
tccli teo DescribeContentQuota --cli-unfold-argument  \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-ajj243-afjkj245-af",
        "PrefetchQuota": [
            {
                "Batch": 2000,
                "Daily": 10000,
                "DailyAvailable": 10000,
                "Type": "prefetch_url"
            }
        ],
        "PurgeQuota": [
            {
                "Batch": 2000,
                "Daily": 10000,
                "DailyAvailable": 10000,
                "Type": "purge_url"
            },
            {
                "Batch": 2000,
                "Daily": 10000,
                "DailyAvailable": 10000,
                "Type": "purge_prefix"
            },
            {
                "Batch": 2000,
                "Daily": 10000,
                "DailyAvailable": 10000,
                "Type": "purge_host"
            },
            {
                "Batch": 2000,
                "Daily": 10000,
                "DailyAvailable": 10000,
                "Type": "purge_all"
            }
        ]
    }
}
```

