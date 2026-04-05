**Example 1: sql知识创建**

sql知识创建

Input: 

```
tccli wedata CreateChatSqlKnowledge --cli-unfold-argument  \
    --WorkspaceId asdf \
    --RoomKey afaf \
    --KnowledgeType asdfa \
    --SqlQueryInfo.Name sdfa \
    --SqlQueryInfo.Content fa \
    --SqlQueryInfo.Comment asdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "sdfs"
        },
        "RequestId": "f6b58d0e-7e96-4fe9-a0b5-12fa96a0b848"
    }
}
```

