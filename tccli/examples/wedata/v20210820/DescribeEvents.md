**Example 1: 例子**

例子

Input: 

```
tccli wedata DescribeEvents --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "EventsResponse": [
                {
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
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "abc"
    }
}
```

