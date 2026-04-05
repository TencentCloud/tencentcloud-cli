**Example 1: 示例1**



Input: 

```
tccli wedata ListTaskLog --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --TaskId ta-973386cf \
    --EndTime 378 \
    --StartTime 87827
```

Output: 
```
{
    "Response": {
        "Data": {
            "LogContentList": [
                {
                    "Log": "Task:ta-ad218e6d is running. if not running, please wait a moment.",
                    "PkgId": "pkg",
                    "Time": "15"
                }
            ],
            "NextOffset": "1"
        },
        "RequestId": "66400444-31a6-42e8-9ae9-766886372d1e"
    }
}
```

