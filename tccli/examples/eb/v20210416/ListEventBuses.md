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
                "Description": "abc",
                "AddTime": "2020-09-22T00:00:00+00:00",
                "EventBusName": "abc",
                "EventBusId": "abc",
                "Type": "abc",
                "PayMode": "abc",
                "ConnectionBriefs": [
                    {
                        "Type": "abc",
                        "Status": "abc"
                    }
                ],
                "TargetBriefs": [
                    {
                        "TargetId": "abc",
                        "Type": "abc"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

