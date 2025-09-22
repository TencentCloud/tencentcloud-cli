**Example 1: 异步终止任务实例**



Input: 

```
tccli wedata KillTaskInstancesAsync --cli-unfold-argument  \
    --ProjectId 2428908825624145920 \
    --InstanceKeyList '20250828163920570_2025-08-28 16:40:00'
```

Output: 
```
{
    "Response": {
        "Data": {
            "AsyncId": "c2d687cf-f0a9-4357-bada-942bf43e33b7"
        },
        "RequestId": "5df7b239-f109-4c53-8aca-d9ef390d33bd"
    }
}
```

