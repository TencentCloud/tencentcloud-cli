**Example 1: 检查集成节点名称是否存在**



Input: 

```
tccli wedata CheckIntegrationNodeNameExists --cli-unfold-argument  \
    --TaskId 1232314 \
    --Name tfsaest \
    --WorkspaceId tesfsft123 \
    --Id 12123
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": false
        },
        "RequestId": "9a558082-60e3-47ae-8992-2f17b649e231"
    }
}
```

