**Example 1: 获取事件集列表**

获取事件集列表

Input: 

```
tccli eb ListEventBuses --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventBuses": [
            {
                "ModTime": "2020-09-22T00:00:00+00:00",
                "Description": "desc",
                "AddTime": "2020-09-22T00:00:00+00:00",
                "EventBusName": "eb",
                "EventBusId": "eb-id",
                "Type": "type",
                "PayMode": "pay",
                "ConnectionBriefs": [
                    {
                        "Type": "type",
                        "Status": "status"
                    }
                ],
                "TargetBriefs": [
                    {
                        "TargetId": "target",
                        "Type": "type"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "reqid-xxx"
    }
}
```

