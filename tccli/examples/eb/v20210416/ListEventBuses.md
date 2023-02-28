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
                "Description": "xx",
                "AddTime": "2020-09-22T00:00:00+00:00",
                "EventBusName": "xx",
                "EventBusId": "xx",
                "Type": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

