**Example 1: 注册事件监听者**

注册事件监听者

Input: 

```
tccli wedata RegisterDsEventListener --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Key 20250228113937526 \
    --Type REST_API \
    --EventName umin5 \
    --EventProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreationTs": "2025-02-28T03:45:25.011Z",
            "EventName": "umin5",
            "EventProjectId": "1460947878944567296",
            "Key": "20250228113937526",
            "PropertiesList": null,
            "TaskInfo": null,
            "Type": "REST_API"
        },
        "RequestId": "76e6951b-8e0f-4734-a4dc-ac3e6506cc08"
    }
}
```

