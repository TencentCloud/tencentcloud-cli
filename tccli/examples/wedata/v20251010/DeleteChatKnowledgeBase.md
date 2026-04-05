**Example 1: 删除知识库**

删除知识库

Input: 

```
tccli wedata DeleteChatKnowledgeBase --cli-unfold-argument  \
    --WorkspaceId asdf \
    --RoomKey sdfd \
    --KnowledgeBaseKey sdfds
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "sdfds"
        },
        "RequestId": "25e2d36c-3827-4824-b519-4da773d744c1"
    }
}
```

