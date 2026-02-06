**Example 1: 查看应用引用的共享知识库列表**

查看应用引用的共享知识库列表

Input: 

```
tccli lke ListReferShareKnowledge --cli-unfold-argument  \
    --AppBizId 1927192****14054336
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DocTotal": 0,
                "EmbeddingModel": "",
                "KnowledgeBizId": "1927192****14054336",
                "KnowledgeDescription": "test共享知识库",
                "KnowledgeName": "test共享知识库",
                "KnowledgeType": 0,
                "OwnerStaffId": "",
                "QaExtractModel": "",
                "UpdateTime": "0"
            }
        ],
        "RequestId": "2abb80ba-9d4b-48a9-bd47-129c7a07c119"
    }
}
```

