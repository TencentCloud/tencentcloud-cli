**Example 1: 例子**

例子

Input: 

```
tccli wedata DescribeEventDetail --cli-unfold-argument  \
    --EventId 1 \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": 1,
            "InstanceId": "abc",
            "EventTime": "2020-09-22T00:00:00+00:00",
            "EventName": "abc",
            "EventStatus": "abc",
            "EventType": "abc",
            "IsAlarm": "abc",
            "ProjectId": "abc",
            "BelongTo": "abc",
            "BaselineId": 1,
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "UpdateTime": "2020-09-22T00:00:00+00:00",
            "AppId": "abc",
            "UserUin": "abc",
            "OwnerUin": "abc"
        },
        "RequestId": "abc"
    }
}
```

