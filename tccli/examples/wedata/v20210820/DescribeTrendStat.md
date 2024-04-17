**Example 1: 规则触发趋势情况**



Input: 

```
tccli wedata DescribeTrendStat --cli-unfold-argument  \
    --ProjectId 1554778168856817664 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "StatDate": "2023-10-01",
                "AlarmCnt": 1,
                "PipelineCnt": 1
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

