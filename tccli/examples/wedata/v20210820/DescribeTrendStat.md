**Example 1: 规则触发趋势情况**



Input: 

```
tccli wedata DescribeTrendStat --cli-unfold-argument  \
    --ProjectId 1 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AlarmCnt": 1,
                "StatDate": "2022-01-01",
                "PipelineCnt": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

