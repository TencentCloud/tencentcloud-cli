**Example 1: 创建知识**

创建知识

Input: 

```
tccli wedata UpdateChatKnowledge --cli-unfold-argument  \
    --WorkspaceId sdaf \
    --RoomKey asdf \
    --KnowledgeBaseKey afaf \
    --KnowledgeList.0.Noun sdf \
    --KnowledgeList.0.Explanation asdf \
    --KnowledgeList.0.KnowledgeKey dsf
```

Output: 
```
{
    "Response": {
        "Data": {
            "KnowledgeId": "",
            "KnowledgeKey": ""
        },
        "RequestId": "b7409482-e36d-4548-b2f6-ae72eadcd922"
    }
}
```

