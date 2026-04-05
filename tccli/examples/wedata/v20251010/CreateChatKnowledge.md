**Example 1: 创建知识**

创建知识

Input: 

```
tccli wedata CreateChatKnowledge --cli-unfold-argument  \
    --WorkspaceId sdfds \
    --KnowledgeBaseKey sdfsd \
    --RoomKey sdf \
    --KnowledgeList.0.Noun sdf \
    --KnowledgeList.0.Explanation sdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "KnowledgeIds": [],
            "KnowledgeKeys": []
        },
        "RequestId": "41dfca0a-ba86-4f22-b93c-f48e9d0b18f2"
    }
}
```

