**Example 1: 查找事件实例**



Input: 

```
tccli wedata DescribeEventCases --cli-unfold-argument  \
    --ProjectId 1253824234232 \
    --Category  \
    --PageNumber 1 \
    --PageSize 10 \
    --EventName test_day_event \
    --EventType  \
    --EventSubType  \
    --EventBroadcastType  \
    --Status  \
    --CreationTimeStart  \
    --CreationTimeEnd  \
    --EventTriggeredTimeStart  \
    --EventTriggeredTimeEnd  \
    --LogTimeStart  \
    --LogTimeEnd  \
    --Dimension 
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CaseId": "7b55e80c3a7949428c34b02ab82b09b7",
                    "Description": null,
                    "Dimension": "20240409",
                    "EventBroadcastType": null,
                    "EventName": "test_event_mico",
                    "EventSubType": "DAY",
                    "EventTriggerTimestamp": "2024-04-11T06:45:06.198Z",
                    "EventType": "TIME_SERIES",
                    "LogTimestamp": "2024-04-11T07:37:40.410Z",
                    "Status": "CONSUMING",
                    "TTL": 30,
                    "TimeUnit": "DAYS"
                }
            ],
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 20,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "ed042b6e-e2de-4425-9868-b994d5d18fd8"
    }
}
```

