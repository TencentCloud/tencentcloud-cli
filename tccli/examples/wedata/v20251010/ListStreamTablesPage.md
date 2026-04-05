**Example 1: 示例1**



Input: 

```
tccli wedata ListStreamTablesPage --cli-unfold-argument  \
    --ConnectionType dge \
    --WorkspaceId dge \
    --ConnectionId dge
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "TableName": "table01"
                }
            ],
            "NextPageToken": "token"
        },
        "RequestId": "a7572907-bb85-4a23-b6fa-248a0336afb2"
    }
}
```

