**Example 1: sql知识更新**

sql知识更新

Input: 

```
tccli wedata UpdateChatSqlKnowledge --cli-unfold-argument  \
    --WorkspaceId sss \
    --RoomKey dffsdf \
    --KnowledgeKey sdfs \
    --KnowledgeType df \
    --SqlQueryInfo.Name sdfs \
    --SqlQueryInfo.Content fa \
    --SqlQueryInfo.Comment afa
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "sdfs"
        },
        "RequestId": "c47b8555-166d-4757-820a-8c424e84dcba"
    }
}
```

