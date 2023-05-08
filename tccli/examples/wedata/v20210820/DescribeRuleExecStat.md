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
            "AlarmCnt": 1,
            "LastTotalCntRatio": 0.0,
            "LastTriggerCnt": 1,
            "AlarmCntRatio": 0.0,
            "TotalCntRatio": 0.0,
            "TriggerCnt": 1,
            "TriggerCntRatio": 0.0,
            "LastPipelineCntRatio": 0.0,
            "PipelineCntRatio": 0.0,
            "TotalCnt": 1,
            "PipelineCnt": 1,
            "LastTriggerCntRatio": 0.0,
            "LastTotalCnt": 1,
            "LastAlarmCntRatio": 0.0,
            "LastAlarmCnt": 1,
            "LastPipelineCnt": 1
        },
        "RequestId": "xx"
    }
}
```

