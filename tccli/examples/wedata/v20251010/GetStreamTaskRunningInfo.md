**Example 1: 示例1**



Input: 

```
tccli wedata GetStreamTaskRunningInfo --cli-unfold-argument  \
    --TaskId dsafj \
    --WorkspaceId dsafj \
    --NodeId dsafj \
    --DatasourceType dsafj
```

Output: 
```
{
    "Response": {
        "Data": {
            "CollectionNum": "7664",
            "DatabaseNum": "7664",
            "IncrementalPhase": {
                "EmitEventTimeLag": "7664",
                "EndTime": "7664",
                "FinishedChunkNum": "7664",
                "StartTime": "7664",
                "State": "7664",
                "TableNum": "7664",
                "TopicNum": "7664",
                "TotalChunkNum": "7664"
            },
            "SchemaNum": "7664",
            "SnapshotPhase": {
                "EmitEventTimeLag": "7664",
                "EndTime": "7664",
                "FinishedChunkNum": "7664",
                "StartTime": "7664",
                "State": "7664",
                "TableNum": "7664",
                "TopicNum": "7664",
                "TotalChunkNum": "7664"
            },
            "SourceDataType": "7664",
            "TableNum": "7664",
            "TopicNum": "7664"
        },
        "RequestId": "1dc444a1-7533-477c-939b-b71c286718aa"
    }
}
```

