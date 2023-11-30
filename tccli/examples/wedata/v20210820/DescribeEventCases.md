**Example 1: 待消费**



Input: 

```
tccli wedata DescribeEventCases --cli-unfold-argument  \
    --ProjectId abc \
    --Category abc \
    --PageNumber 1 \
    --PageSize 1 \
    --EventName abc \
    --EventType abc \
    --EventSubType abc \
    --EventBroadcastType abc \
    --Status abc \
    --CreationTimeStart abc \
    --CreationTimeEnd abc \
    --EventTriggeredTimeStart abc \
    --EventTriggeredTimeEnd abc \
    --LogTimeStart abc \
    --LogTimeEnd abc \
    --Dimension abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "TotalPage": 1,
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 1,
            "Items": [
                {
                    "CaseId": "abc",
                    "EventName": "abc",
                    "EventType": "abc",
                    "EventSubType": "abc",
                    "EventBroadcastType": "abc",
                    "TTL": 1,
                    "TimeUnit": "abc",
                    "Dimension": "abc",
                    "Status": "abc",
                    "EventTriggerTimestamp": "abc",
                    "LogTimestamp": "abc",
                    "Description": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 获取事件**

获取事件

Input: 

```
tccli wedata DescribeEventCases --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Category all \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "获取事件实例出错"
        },
        "RequestId": "dd4c9f45-1b85-488f-8fcd-73ae8c1fa37d"
    }
}
```

