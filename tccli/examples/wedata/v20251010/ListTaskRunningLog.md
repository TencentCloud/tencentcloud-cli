**Example 1: 示例1**



Input: 

```
tccli wedata ListTaskRunningLog --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --TaskId ta-f30950e8 \
    --JobId tg-d250b756 \
    --EndTime 1769070661054 \
    --StartTime 1768984261054 \
    --Container taskmanager \
    --Limit 3000 \
    --Offset 23000
```

Output: 
```
{
    "Response": {
        "Data": {
            "ListOver": false,
            "LogContentList": [
                {
                    "ContainerName": "container",
                    "Log": "2026-01-22 03:41:01.373 [Z][SchemaRegistry-Coordinator] INFO  org.apache.flink.configuration.GlobalConfiguration [] - Loading configuration property: classloader.resolve-order, child-first",
                    "PkgId": "1a7d269f-4694-48ae-a257-d4939fde2934",
                    "PkgLogId": "1a7d269f-4694-48ae-a257-d4939fde2934",
                    "Time": "1769024461373"
                }
            ],
            "NextOffset": "26000"
        },
        "RequestId": "95c962df-1745-47a3-885c-f926658bddc9"
    }
}
```

