**Example 1: 创建事件集**



Input: 

```
tccli eb CreateEventBus --cli-unfold-argument  \
    --EventBusName test
```

Output: 
```
{
    "Response": {
        "EventBusId": "eb-xxxxxxxx",
        "RequestId": "e3d43926-c2cd-49f2-97f0-53db21e6fcea"
    }
}
```

**Example 2: 创建事件集1**



Input: 

```
tccli eb CreateEventBus --cli-unfold-argument  \
    --EventBusName test \
    --Description test-desc
```

Output: 
```
{
    "Response": {
        "EventBusId": "eb-l65vlc2u",
        "RequestId": "b3103b8d-77a6-4b55-b42f-a25e2dc453a9"
    }
}
```

