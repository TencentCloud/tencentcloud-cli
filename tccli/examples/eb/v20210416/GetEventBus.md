**Example 1: 获取事件集**

获取事件集

Input: 

```
tccli eb GetEventBus --cli-unfold-argument  \
    --EventBusId eb-l65vlc2
```

Output: 
```
{
    "Response": {
        "AddTime": "2022-12-12T20:09:46+08:00",
        "ClsLogsetId": "",
        "ClsTopicId": "",
        "Description": "",
        "EventBusId": "eb-0gdrbv5q",
        "EventBusName": "default",
        "ModTime": "2022-12-12T20:09:46+08:00",
        "PayMode": "",
        "LogTopicId": "xxx",
        "SaveDays": "1",
        "EnableStore": true,
        "LinkMode": "Disorder",
        "RequestId": "ffd4aae2-c29e-40a8-b18c-037a17ed810c",
        "Type": "Cloud"
    }
}
```

