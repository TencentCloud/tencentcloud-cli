**Example 1: 成功**

成功

Input: 

```
tccli adp DescribeAppTriggerSummaryList --cli-unfold-argument  \
    --AppId 2075415763781738240 \
    --PageNumber 1 \
    --PageSize 30 \
    --Query 定时
```

Output: 
```
{
    "Response": {
        "TotalCount": "1",
        "TriggerList": [
            {
                "AppId": "2075415763781738240",
                "ExecuteType": 1,
                "FailedCount": "0",
                "LastSessionId": "t77186f546780488d82db80e5f3587308",
                "Status": 1,
                "SuccessCount": "2",
                "TriggerId": "ddbfec0a-44c3-4d93-a6f5-f5bf9a0fcb2d",
                "TriggerName": "定时触发",
                "TriggerStatus": {
                    "ScheduledStatus": {
                        "LastFireTime": "2026-07-12T18:00:10+08:00",
                        "NextFireTime": "2026-07-13T18:00:00+08:00",
                        "PolicySummary": "18:00"
                    }
                },
                "TriggerType": 1,
                "UnreadRunLogCount": "2"
            }
        ],
        "RequestId": "e4d4d33d-5c6e-4395-819c-c537de13fbfc"
    }
}
```

