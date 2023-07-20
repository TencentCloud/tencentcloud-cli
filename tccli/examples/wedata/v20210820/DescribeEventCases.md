**Example 1: 成功获取事件实例**

成功获取事件实例

Input: 

```
tccli wedata DescribeEventCases --cli-unfold-argument  \
    --ProjectId 1460963739345731584 \
    --Category current \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CaseId": "9eb045788691c9e901869c4858950000",
                    "Description": "手动触发",
                    "Dimension": "20230301",
                    "EventBroadcastType": "SINGLE",
                    "EventName": "stack_text_event",
                    "EventTriggerTimestamp": "2023-03-01T08:27:12.398Z",
                    "EventType": "TIME_SERIES",
                    "LogTimestamp": "2023-03-24T07:09:47.051Z",
                    "Status": "ACTIVE",
                    "TTL": null,
                    "TimeUnit": "DAYS"
                }
            ],
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "21318b6f-b2c9-46f3-be55-17747991c87b"
    }
}
```

