**Example 1: 获取事件集列表**



Input: 

```
tccli eb ListEventBuses --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventBuses": [
            {
                "AddTime": "2021-04-28T23:34:19+08:00",
                "Description": "",
                "EventBusId": "eb-l65vlc2u",
                "EventBusName": "test",
                "ModTime": "2021-04-28T23:34:19+08:00",
                "Type": "Custom"
            }
        ],
        "RequestId": "116a59b2-4d31-4d17-966e-6ee65f7401f5",
        "TotalCount": 1
    }
}
```

