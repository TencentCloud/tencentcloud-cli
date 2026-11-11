**Example 1: 查询Dspm访问拓扑概览**



Input: 

```
tccli csip DescribeDspmAccessTopologySummary --cli-unfold-argument  \
    --MemberId mem-6wfo0fzks3
```

Output: 
```
{
    "Response": {
        "SourceIpCount": 3,
        "AccountCount": 2,
        "DbCount": 65,
        "TableCount": 740,
        "AccessCountLast7Days": 38302536,
        "AccessCountLast30Days": 38302536,
        "TableCombinationCount": 756,
        "DataIncomplete": false,
        "LastCalcTime": "2026-09-24 11:23:31",
        "RequestId": "6f2c1d7e-3b45-4a18-9c02-8ed5f1a37b90"
    }
}
```

