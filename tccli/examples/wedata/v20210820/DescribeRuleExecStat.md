**Example 1: 规则运行情况**



Input: 

```
tccli wedata DescribeRuleExecStat --cli-unfold-argument  \
    --ProjectId 1 \
    --BeginDate 1645155262 \
    --EndDate 1645155262
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCnt": 1,
            "LastTotalCnt": 1,
            "TotalCntRatio": 0,
            "LastTotalCntRatio": 0,
            "TriggerCnt": 1,
            "LastTriggerCnt": 1,
            "TriggerCntRatio": 0,
            "LastTriggerCntRatio": 0,
            "AlarmCnt": 1,
            "LastAlarmCnt": 1,
            "AlarmCntRatio": 0,
            "LastAlarmCntRatio": 0,
            "PipelineCnt": 1,
            "LastPipelineCnt": 1,
            "PipelineCntRatio": 0,
            "LastPipelineCntRatio": 0
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

